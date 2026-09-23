import chromadb
from  embeddings import embedded_chunks

client = chromadb.PersistentClient(path="./chromadb")
collection = client.get_or_create_collection(name="my_data")

collection.add(
    ids = [str(a['chunk_id']) for a in embedded_chunks],
    documents = [a['chunk'] for a in embedded_chunks],
    metadatas=[{"filename":a["filename"]} for a in embedded_chunks],
    embeddings=[a['embedding'] for a in embedded_chunks]
)
   
if __name__=="__main__":
   print(collection)
   print ("total records:",collection.count())

