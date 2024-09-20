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
    if docs is not None:
        rtn_str = ""
        for doc in docs:
            rtn_str += doc.to_dict().get('title') + "\n"
        return rtn_str
    else:
        return f"Could not find {value} in database"


def get_field_from_firestore(field, title):
    docs = (movie_database.collection("Movies").where(filter=FieldFilter('title', '==', title)).stream())
    if docs is not None:
        for doc in docs:
            return doc.to_dict().get(field)
    else:
        return f"Could not find {title} in database"


def get_info_from_firestore(title):
    docs = (movie_database.collection("Movies").where(filter=FieldFilter('title', '==', title)).stream())
    if docs is not None:
        for doc in docs:
            return f"Rank: {doc.to_dict().get('rank')}\nYear: {doc.to_dict().get('year')}\nRating: {doc.to_dict().get('rating')}\nDuration: {doc.to_dict().get('duration')}\nGenre: {doc.to_dict().get('genre')}\nDirector: {doc.to_dict().get('director')}"
    else:
        return f"Could not find {title} in database"
