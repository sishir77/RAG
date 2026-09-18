from chunking import all_chunks
from sentence_transformers import sentence_transformer


model = sentence_transformer("all-MiniLM-L6-v2")

Emdeddings=[]
def emdeddings():
    for chunk in all_chunks:
        "filename"= chunk['filename']
        "text"= chunk["chunk"]
        "embed_id"= chunk["chunk_id"]

        emdeddings = model.encode("text")

        for embed in emdeddings:
            Emdeddings.append(embed)


emdeddings()



