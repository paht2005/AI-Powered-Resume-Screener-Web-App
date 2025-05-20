# copyright [2025] [Phat Nguyen Cong] (Github: https://github.com/paht2005)

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")

def score_resume(resume_text, job_description):
    embeddings = model.encode([resume_text, job_description])
    score = cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
    return round(score * 100, 2)

def highlight_matching_skills(resume_text, job_description):
    jd_words = set(job_description.lower().split())
    highlighted = []
    for word in resume_text.split():
        if word.lower().strip(",.()") in jd_words:
            highlighted.append(f"<span class='highlight'>{word}</span>")
        else:
            highlighted.append(word)
    return " ".join(highlighted)
