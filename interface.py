from google.cloud.firestore_v1 import FieldFilter
from firebase_authentication import movie_database


def load_movies():
    movies = []
    docs = (movie_database.collection("Movies").stream())
    for doc in docs:
        movies.append(doc.to_dict().get('title'))
    return movies


def get_title_from_firestore(field, op, value):
    docs = (movie_database.collection("Movies").where(filter=FieldFilter(field, op, value)).stream())
    titles = []
    for doc in docs:
        titles.append(doc.to_dict().get('title'))
    if titles == []:
        titles.append(f"Could not find '{value}' in database")
    return titles


def get_field_from_firestore(field, title):
    docs = (movie_database.collection("Movies").where(filter=FieldFilter('title', '==', title)).stream())
    fields = []
    for doc in docs:
        fields.append(doc.to_dict().get(field))
    if fields == []:
        fields.append(f"Could not find '{title}' in database")
    return fields


def get_info_from_firestore(title):
    docs = (movie_database.collection("Movies").where(filter=FieldFilter('title', '==', title)).stream())
    movie_info = []
    for doc in docs:
        movie_info.append(f"Rank: {doc.to_dict().get('rank')}")
        movie_info.append(f"Year: {doc.to_dict().get('year')}")
        movie_info.append(f"Rating: {doc.to_dict().get('rating')}")
        movie_info.append(f"Duration: {doc.to_dict().get('duration')}")
        movie_info.append(f"Genre: {doc.to_dict().get('genre')}")
        movie_info.append(f"Director: {doc.to_dict().get('director')}")
    if movie_info == []:
        movie_info.append(f"Could not find '{title}' in database")
    return movie_info
