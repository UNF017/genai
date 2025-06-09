from gensim.models import Word2Vec 
from gensim.parsing.preprocessing import STOPWORDS 
paragraph = [ 
'Contracts are binding agreements', 
'The plaintiff is alleging fraud', 
'The defendant was found guilty', 
'Tort law covers negligence', 
'Litigation is still ongoing', 
'Jurisdiction is exclusive in some cases', 
'Arbitration is legally binding', 
'A subpoena is mandatory to appear in court', 
'An affidavit is a sworn statement', 
'Strict liability applies in certain cases' ]
docs = [[word for word in sentence.lower().split() if word not in STOPWORDS] for sentence in paragraph] 
model = Word2Vec (sentences=docs, vector_size=3, min_count=1) 
print("Vocabulary:", model.wv.index_to_key) 
if 'contracts' in model.wv: 
    words = model.wv.most_similar('contracts', topn=5) 
    print("Similar words to 'contracts':", words) 
else: 
    print("'contracts' not found in vocabulary")
