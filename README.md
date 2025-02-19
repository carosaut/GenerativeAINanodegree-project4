Generative AI Nanodegree Project 4 - HomeMatch

Steps to run application: 
  - install requirements.txt (creating a venv is recomended) 
  - create a "config.py" file containing your openai key and base url - see below.
  - Run app.py
  - Run /generate-listings endpoint first to generate the 10 listings. The Chromadb collection is not persistant.
  - Run /buyer_search endpoint with a query paremter called "buyer_query". This should be a natural language description of what you want to search for. For example, "At least two bedrooms with a nice view and a freestanding bath" or "A comfortable three-bedroom house with a spacious kitchen and a cozy living room."
  - The return to this endpoint contains the details of the top 3 properties that match the search query. It also includes the score of the match and a "Personalised Description" based on the buyers preferences. 

Pleaase note the listings.py file is an example. When you run the application the listings.py file will be generaated with the listings you create. 

This app requires a config file called "config.py" saved in the main directory. It should have the following content:
openai_key=<YOUR OPEN AI KEY>
openai_base=<your base url>
