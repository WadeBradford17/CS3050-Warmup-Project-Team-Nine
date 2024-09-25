from google.cloud.firestore_v1 import FieldFilter
from firebase_authentication import movie_database


# function to load all movie documents from the firebase collection
def load_movies():
    movies = []
    docs = (movie_database.collection("Movies").stream())
    for doc in docs:
        # convert each doc to dictionary and get title field
        movies.append(doc.to_dict().get('title'))

    return movies


# function to get movie title from firestore collection document
def get_title_from_firestore(field, op, value):
    titles = []

    # handling general fields excluding genre and viewers
    if field != 'genre' and field != 'viewers':
        docs = (movie_database.collection("Movies").where(filter=FieldFilter(field, op, value)).stream())
        for doc in docs:
            titles.append(doc.to_dict().get('title'))
    else:
        # handling for genre and viewers
        docs = movie_database.collection("Movies").stream()
        not_in_titles = []
        for doc in docs:
            title = doc.to_dict().get('title')
            entries = doc.to_dict().get(field)
            if entries is not None:
                # check if field contains the value based on the operator
                for entry in entries:
                    if op == '==':
                        if entry == value and title not in titles:
                            titles.append(title)
                    else:
                        if entry == value and title not in not_in_titles:
                            not_in_titles.append(title)

        if not_in_titles != []:
            docs = movie_database.collection("Movies").stream()
            for doc in docs:
                title = doc.to_dict().get('title')
                if title not in not_in_titles:
                    titles.append(title)

    # If no matching titles are found, return message
    if titles == []:
        titles.append(f"Could not find '{value:.0f}' in database")
    return titles

# function to retrieve a specific field value from a movie document
def get_field_from_firestore(field, title):
    fields = []
    docs = (movie_database.collection("Movies").where(filter=FieldFilter('title', '==', title)).stream())
    for doc in docs:
        if field == 'genre' or field == 'viewers':
            entries = doc.to_dict().get(field)
            if entries is not None:
                for entry in entries:
                    fields.append(entry)
            else:
                fields.append(None)
        else:
            fields.append(doc.to_dict().get(field))

    # handling for when no fields are found or field value is None
    if fields == []:
        fields.append(f"Could not find '{title}' in database")
    if fields == [None]:
        fields = ['N/A']

    return fields


# function to retrieve all unique values for a specified field across all movie documents
def get_unique_entries_of_collection_from_firestore(field):
    unique_entries = []
    docs = movie_database.collection("Movies").stream()
    for doc in docs:
        entries = doc.to_dict().get(field)
        if entries is not None:
            for entry in entries:
                if entry not in unique_entries:
                    unique_entries.append(entry)

    return unique_entries


# function to retrieve movie information by title
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

    # handling where no movie is found with the given title
    if movie_info == []:
        movie_info.append(f"Could not find '{title}' in database")

    return movie_info
