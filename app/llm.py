import os
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

client = OpenAI(api_key=os.getenv("GROQ_API_KEY"),
                base_url="https://api.groq.com/openai/v1")

def generate_answer(question, context):
    prompt = f"""
you are a helpful assitance answering question based on provided context

context:
{context}

question:
{question}

Answer the question using only the information provided in the context.
If the answer cannot be found in the context, say:
"I don't know based on the provided information."""

    response = client.responses.create(
        model= "openai/gpt-oss-20b",
        input= prompt)
         
    return response.output_text

if __name__ == "__main__":

    question = "Which is the first tourist accommodation of Swan Lagoon?"

    context = """
    "The Swan's Nest Caravan Park": First tourist accommodation,
    established 1955 by the O'Malley family.
    """

    answer = generate_answer(question, context)

    print("Answer:")
    print(answer)