import json
from firebase_authentication import movie_database

# load movie data json
with open('imdb-movie-data.json') as file:
    movies = json.load(file)

# reference to collection in Firebase
collection_ref = movie_database.collection('Movies')

# create batch
batch = movie_database.batch()

for movie in movies:
    # 'uuid' field as document ID
    doc_ref = collection_ref.document(movie['uuid'])
    # add document to batch
    batch.set(doc_ref, movie)

# upload movie documents
try:
    batch.commit()
    print(f"All movies have been added to the Firestore Movies Collection.")
except Exception as e:
    print(f"Error occurred during batch commit: {e}")
