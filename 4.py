!pip install cohere gensim 
import cohere 
import gensim.downloader as api 
co=cohere.Client("iKCV07rBnBU5uYH40gPabT4cFY8DkEiZnZgxtIrr") 
print("Loading word embeddings...") 
model=api.load("glove-wiki-gigaword-100") 
print("Model loaded successfully.") 
prompt = "write an essay on natural disaster" 
def get_first_enriched_prompt(prompt, topn=3): 
    for word in prompt.split(): 
        try: 
            similar_words = model.most_similar(word.strip('.,!?').lower(), topn=topn) 
            for sim, _ in similar_words: 
                enriched=prompt.replace(word, sim) 
                return enriched 
        except: 
            continue 
    return None 
def get_response(text): 
    try: 
        return co.chat(model="command-r", message=text).text.strip() 
    except Exception as e: 
        return f"Error: {e}" 
print(f"\nOriginal Prompt:\n{prompt}\nResponse: \n {get_response(prompt)}") 
enriched_prompt = get_first_enriched_prompt(prompt) 
if enriched_prompt: 
    print(f"\nEnriched Prompt: \n{enriched_prompt}\nResponse: \n{get_response (enriched_prompt)}") 
else: 
    print("\nNo enriched prompt could be generated.")
