from sentence_transformers import SentenceTransformer
import pandas as pd
import hickle as hkl



CSV_FILE = "who_covid_19_qa.csv"
model = SentenceTransformer('bert-base-nli-mean-tokens')

data = pd.read_csv(CSV_FILE)

print(data["question"])

sentences = data["question"].to_list()
sentence_embeddings = model.encode(sentences)

print(len(sentence_embeddings))
print(len(sentence_embeddings[0]))

hkl.dump(sentence_embeddings, 'who_covid_19_question_embedding.hkl', mode='w', compression='gzip')