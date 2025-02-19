from fastapi import (
    APIRouter
)
import json
from utils.ai import ai_generator, embedding_generator
from utils.db import collection
from utils.search_helper import augement_description, clean_query
from utils.prompts import property_generator_prompt

router = APIRouter()

### generates listsings and adds to chromadb collection. Listings are not persistant need to be created each time application is started ###

@router.post('/generate-listings')
async def Generate_listing():
    
    ### 10 listings generaated using ai_generator() ###

    list_of_listings = [ai_generator(property_generator_prompt) for _ in range(10)]

    ### embeddings collected for each listing, then listing and embeddings added to chromadb collection ###

    try:
        for i, text in enumerate(list_of_listings):
            embedding = embedding_generator(text)  # Convert text to embedding
            
            collection.add(
                ids=[str(i)],  # Unique ID for each entry
                embeddings=[embedding],
                metadatas=[{"listing": text}]  # Optional metadata
            )
        
    except Exception as e:
        print(f"Error: {e}")

    return {"message": "complete"}
    
### Search of chromadb collection for most relevant properties to the buyer, returning n number of results. A personalised description is added to the result, tailored to the buyers preferences ### 

@router.get('/buyer_search')
async def Buyer_search(buyer_query: str, n_results: int = 3):
    try:

        ### Buyer query entered in natural language in the front end. It's then cleaned up embedded and used to search collection for the 3 closest matched properties ### 
        ### I've been using postman to test to have been entering queries as query parameters called "buyer_query" ###

        buyer_query = clean_query(buyer_query)
        query_embedding = embedding_generator(buyer_query)

        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        matched_listings = []

        ### For each returned result, the property description is extracted and used to generate a personalised description using augement_description(). ###
        #### This is added to the result and returned alongside the original description, the rest of the listing, and the vector match score from the search of the chromadb collection ###
        
        for i in range(len(results["ids"][0])):
            listing_dict = json.loads(results["metadatas"][0][i]["listing"])
            listing_dict["Personalised Description"] = augement_description(buyer_query, listing_dict)
            
            new_listing = {
                "listing": listing_dict,
                "score": results["distances"][0][i]
            }

            matched_listings.append(new_listing)

        return {"results": matched_listings}

    except Exception as e:
        return {"error": str(e)}


