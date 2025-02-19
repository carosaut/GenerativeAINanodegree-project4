from openai import OpenAI

from config import openai_key, openai_base

embed_model = "text-embedding-ada-002"
chat_model = "gpt-3.5-turbo"

client = OpenAI(
    base_url = openai_base,
    api_key = openai_key
)

def ai_generator(prompt):
    response = client.chat.completions.create(
        model=chat_model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

    
def embedding_generator(text):  
    response = client.embeddings.create(
        model=embed_model,
        input=text
    )
    return response.data[0].embedding

