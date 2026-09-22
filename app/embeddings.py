from chunking import all_chunks
from sentence_transformers import SentenceTransformer


model = SentenceTransformer("all-MiniLM-L6-v2")

embedded_chunks=[]
def embeddings():
    for chunk in all_chunks:
        filename= chunk['filename']
        text= chunk["chunk"]
        embed_id= chunk["chunk_id"]

        embedding = model.encode(text)

        embedded_chunks.append({
        "filename": filename,
        "chunk": text,
        "chunk_id": embed_id,
        "embedding": embedding
        })

embeddings()
        


if __name__=="__main__":
    print("Total embedded chunks:", len(embedded_chunks))

    print("First embedded chunk:")
    print(embedded_chunks[0])

    print("Embedding length:")
    print(len(embedded_chunks[0]["embedding"]))
    


  