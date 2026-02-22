from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def check_text_similarity(website_text):
    try:
        # Load scam corpus
        with open("database/scam_text_corpus.txt", "r", encoding="utf-8") as f:
            scam_text = f.read()

        # Create TF-IDF vectors
        vectorizer = TfidfVectorizer(stop_words="english")

        tfidf_matrix = vectorizer.fit_transform([website_text, scam_text])

        # Compute cosine similarity
        similarity_score = cosine_similarity(
            tfidf_matrix[0:1], tfidf_matrix[1:2]
        )[0][0]

        print("Text Similarity Score:", round(similarity_score, 3))

        # Risk grading
        if similarity_score > 0.7:
            return 0.5
        elif similarity_score > 0.4:
            return 0.3
        elif similarity_score > 0.2:
            return 0.1
        else:
            return 0.0

    except Exception as e:
        print("Similarity error:", e)
        return 0.0