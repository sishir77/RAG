from embeddings import embedded_chunks
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from database import collection

model = SentenceTransformer("all-MiniLM-L6-v2")

def similarity_search(query, k=3):
    query_embeddings = model.encode(query)

    result = collection.query(
        query_embeddings=  [query_embeddings],
        n_results= k 
    )
    

    #unpack the single query result
    ids, metadatas, documents,distances =(
        result['ids'][0],
        result['metadatas'][0],
        result["documents"][0],
        result['distances'][0]
        

    )
    results=[]

    for id, metadata, document, distance in zip(ids, metadatas, documents,distances):
        results.append({
            "id": id,
            "filename": metadata['filename'],
            "distance": distance,
            "document": document
        })
    return results

#manual semantic search
"""def semantic_search(query):
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

   return result"""
if __name__=="__main__":

    question = input("Ask your question:" )

    results = similarity_search(question)

    for i,result in enumerate(results, start=1):

        print(
        "------------------------------------------------")
        print(f"\nresult {i}")
        print("\n----------------------------------------------")
        print("\n")
        print(f"Filename:{result['filename']}")
        print(f"id:{result['id']}")
        print(f"distance:{result['distance']}")
        print(f"\ndocuments:{result['document']}")