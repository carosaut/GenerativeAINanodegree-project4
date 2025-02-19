import re
import string
from contractions import fix

from utils.ai import ai_generator

### Takes the buyer preference and the property description. Uses ai_generator() to enhance the description based on buyer preferences, using the prompt below.###

def augement_description(buyer_preference, property):
    prompt = f"""I will provide you with the exact details of a property and a statement of preferences from a buyer.  
Your task is to rewrite the property description in a way that highlights the features most relevant to the buyer. However, you must strictly follow these instructions:  

- Do not alter any factual details of the property, including the number of bedrooms, bathrooms, property size, or any other features provided.  
- Do not add or infer any new information that is not explicitly included in the property description. Only use the data provided.  
- Do not make assumptions about the property or the buyer’s needs that are not directly stated.  
- Focus solely on emphasizing the features that align with the buyer's preferences without introducing anything not already present in the original description.  
- Provide only the rewritten description with no title, introduction, or commentary.  

Property description: {property}  
Buyer preference: {buyer_preference}"""

    result = ai_generator(prompt)

    return result


### Cleans up a string to make it better for embedding, while still retaining meaning ### 
def clean_query(query):
    
    query = query.strip()  # Trim spaces
    query = fix(query)  # Expand contractions
    query = query.lower()  # make lower case
    query = re.sub(r'\s+', ' ', query)  # Normalise spaces

    return query

