import pandas as pd
from sentence_transformers import SentenceTransformer, util

# Load data
reqs = pd.read_csv('requirements.csv')
tests = pd.read_csv('testcases.csv')

# Load NLP model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Encode descriptions
req_embeddings = model.encode(reqs['Description'].tolist(), convert_to_tensor=True)
test_embeddings = model.encode(tests['Description'].tolist(), convert_to_tensor=True)

# Compare using cosine similarity
cosine_scores = util.pytorch_cos_sim(req_embeddings, test_embeddings)

# Match requirements with most similar test case
for i, req_text in enumerate(reqs['Description']):
    best_match_idx = cosine_scores[i].argmax()
    best_score = cosine_scores[i][best_match_idx].item()
    matched_test = tests['Description'][best_match_idx]
    print(f"Requirement {reqs['Requirement_ID'][i]}:")
    print(f"  ↳ {req_text}")
    print(f"Suggested Match: {tests['TestCase_ID'][best_match_idx]} - {matched_test}")
    print(f"Similarity Score: {best_score:.4f}")
    print("-" * 80)