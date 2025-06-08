from pydantic import BaseModel
from typing import List
import wikipediaapi
import re
class InstitutionDetails(BaseModel):
    founder: str
    founded_year: int
    branches: List[str]
    employee_count: int
    summary: str
def get_details(name: str) -> InstitutionDetails:
    wiki = wikipediaapi.Wikipedia(language='en', user_agent='InstitutionInfoFetcher/1.0 (contact@example.com)')
    page = wiki.page(name)

    if not page.exists() or not page.text.strip():
        raise ValueError(f"No Wikipedia page found or content empty for '{name}'.")
    text = page.text
    founder = re.search(r"(?:founded|established|started|managed) by ([^\n\.]+)", text, re.I)
    year = re.search(r"(?:founded|established|started) (?:in )?(\d{4})", text, re.I)
    employees = re.search(r"(?:faculty|staff|employees)[^\d]*(\d{2,5})", text, re.I)
    branches = re.findall(r"branches in ([\w\s]+)", text, re.I)

    return InstitutionDetails(
        founder=founder.group(1).strip() if founder else "Unknown",
        founded_year=int(year.group(1)) if year else 0,
        branches=branches,
        employee_count=int(employees.group(1)) if employees else 0,
        summary=page.summary[:500] if page.summary else "No summary available."
    )
name = "JSSATEB"
details = get_details(name)
print(details.model_dump_json(indent=1))
