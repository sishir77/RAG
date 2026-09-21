from embeddings import embedded_chunks
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-V2")

def semantic_search(query):
    query_embeddings= model.encode(query)

    result=[]
    for chunks in embedded_chunks:
        chunk_embeddings = chunks["embedding"]

        score = cosine_similarity(
            [query_embeddings],
            [chunk_embeddings]
        )[0][0]

        result.append({
            "filename":chunks['filename'],
            "chunk_id": chunks['chunk_id'],
            "chunk": chunks['chunk'],
            "score": score
        })

    result.sort(
        key=lambda x:x['score'],
        reverse=True
    )

    return result

if __name__=="__main__":

    question = input("Ask your question:" )

    results = semantic_search(question)

    for result in results[:3]:
        print("/n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  _ _ _ _ _ _ _")
        print("score:", result["score"])
        print("filename:", result["filename"])
        print("chunk_id:", result["chunk_id"] )
        print("text:", result["chunk"])

        


    

        

