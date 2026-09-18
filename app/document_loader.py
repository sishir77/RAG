
import pymupdf
from pathlib import Path


def load_pdfs(folder_path) :
    documents=[]

    pdf_files= Path(folder_path).glob("*.pdf")

    for pdf_file in pdf_files:
        pdf= pymupdf.open(pdf_file)

        text = ""

        for page in pdf:
            text+= page.get_text()

        pdf.close()

        documents.append({
            "file_name": pdf_file.name,
            "text": text
        })

    return documents

#test the function

documents = load_pdfs(r"D:\RAG\data")

"""for document in documents:
    print(f"File:{document['file_name']}")
    print(f"Text:{document["text"][:500]}")
    print("-" *50)"""






    
        


              