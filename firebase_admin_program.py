import json
import firebase_admin
from firebase_admin import firestore, credentials

# Before running this script, make sure to:
# 1. Install the Firestore library by running the following command in your terminal:
#    pip install google-cloud-firestore

# firebase admin sdk configuration
cred = credentials.Certificate('CS3050-Warmup-Project-Team-Nine/service_account_info.json')
firebase_admin.initialize_app(cred)

# initialize firestore db
movie_database = firestore.client()

# load movie data json
with open('imdb-movie-data.json') as file:
    movies = json.load(file)
