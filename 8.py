! pip install langchain cohere langchain-community
from langchain_community.llms import Cohere
from langchain_community.document_loaders import TextLoader
from langchain.prompts import PromptTemplate
from langchain. chains import LLMChain

text= TextLoader(r"C:\Users\chand\OneDrive\Desktop\student.txt").load()[0].page_content
prompt = PromptTemplate(
    input_variables=["text"],
    template= f"Summarize this text:\n {text}\n summary:"
)
llm=Cohere(cohere_api_key="8iEDONC6GJ1UbVhnXFGpV1QjvcXqBUzoGZanKEwb",temperature=0.7)
summary=LLMChain(llm=llm,prompt=prompt).run(text=text)
print( "\nSummary : \n",summary )
