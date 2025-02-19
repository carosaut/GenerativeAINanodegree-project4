property_generator_prompt = """Your task is to generate a fake real estate listing to test a home matching application. 

Strictly adhere to the following rules:  
- The listing should be in a python dictionary in the style and format of the examples shown below. 
- Only return the listing and do not give the dictionary a name, introduction, or any additional commentary.

Examples:

{"Neighborhood": "Green Oaks", "Price": "$800,000", "Bedrooms": "3", "Bathrooms": "2", "House Size": "2,000 sqft", "Description": "Welcome to this eco-friendly oasis nestled in the heart of Green Oaks. This charming 3-bedroom, 2-bathroom home boasts energy-efficient features such as solar panels and a well-insulated structure. Natural light floods the living spaces, highlighting the beautiful hardwood floors and eco-conscious finishes. The open-concept kitchen and dining area lead to a spacious backyard with a vegetable garden, perfect for the eco-conscious family. Embrace sustainable living without compromising on style in this Green Oaks gem.", "Neighborhood Description": "Green Oaks is a close-knit, environmentally-conscious community with access to organic grocery stores, community gardens, and bike paths. Take a stroll through the nearby Green Oaks Park or grab a cup of coffee at the cozy Green Bean Cafe. With easy access to public transportation and bike lanes, commuting is a breeze."}

{"Neighborhood": "Sunset Heights", "Price": "$1,200,000", "Bedrooms": "4", "Bathrooms": "3.5", "House Size": "3,500 sqft", "Description": "Enjoy breathtaking views from this luxurious 4-bedroom, 3.5-bathroom home in Sunset Heights. The spacious open floor plan features high ceilings, modern finishes, and a gourmet kitchen with top-of-the-line appliances. The master suite offers a private balcony overlooking the city skyline, perfect for relaxing after a long day. Entertain guests in the beautifully landscaped backyard with a pool, spa, and outdoor kitchen. Experience the ultimate in luxury living in Sunset Heights.", "Neighborhood Description": "Sunset Heights is known for its upscale restaurants, boutique shops, and vibrant nightlife. Take a short walk to the trendy Sunset Strip for a night out or explore the nearby hiking trails in the Santa Monica Mountains. With easy access to freeways and public transportation, Sunset Heights offers the perfect balance of convenience and luxury living."}

"""

