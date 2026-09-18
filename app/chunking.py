from typing import List
from document_loader import documents
import langchain
from langchain_text_splitters import RecursiveCharacterTextSplitter


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 30,
    length_function = len
)
all_chunks=[]
id=0

for document in documents:
   filename= document['file_name']
   text = document['text']

   chunks= text_splitter.split_text(text)

   for chunk in chunks:
      all_chunks.append({
         "filename":filename,
         "chunk":chunk,
         "chunk_id": id
      })
      id+=1

print(all_chunks)

#character based chunking
"""def chunk_text(documents, chunk_size:int):

    chunks= []
    start = 0
    id=0
    

    for document in documents:
        filename =document['file_name']
        text= document['text']

        for i in range(0,len(text), chunk_size):

         chunk= text[i:i+chunk_size]
         chunks.append({
            "filename":filename,
            "chunk":chunk,
            "chunk_id":id
            
         })
         id += 1
         
        
    return chunks """


#character based chunking with overlap
"""def chunk_overlap(documents, chunk_size:int, overlap:int):
   chunks=[]
   id=0

   for document in documents:
      filename= document["file_name"]
      text = document["text"]
      start = 0

      while start < len(text):
         end = start + chunk_size
         chunk = text[start:end]
         chunks.append({
            "filename": filename,
            "chunk_id": id,
            "text": chunk
         })
         id +=1
         start= end - overlap
   return chunks"""



#chunks= chunk_overlap(documents, 200,35 )
#print (chunks)




