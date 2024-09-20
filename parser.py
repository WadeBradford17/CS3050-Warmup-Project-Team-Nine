from interface import get_title_from_firestore, get_field_from_firestore, get_info_from_firestore, load_movies

fields = ['title', 'rating', 'year', 'duration', 'director', 'genre', 'viewers', 'rank']
operators = ['==', '>', '<', '>=', '<=', '!=', 'of']
joiners = ['||', '&&']
keywords = ['help', 'quit']
valid_eq_check = ['title', 'director', 'genre', 'viewers']
valid_comp_check = ['year', 'rank', 'rating', 'duration']
valid_belonging_check = ['rating', 'year', 'duration', 'director', 'genre', 'viewers', 'rank']
eq_operators = ['==', '!=']
comp_operators = ['==', '>', '<', '>=', '<=', '!=']
movies = load_movies()


def is_valid_num(num):
    if num.replace('.', '', 1).isdigit():
        return True
    return False


def get_user_input(input):
    if '"' not in input or input.index('"') == input.rfind('"'):
        return "Invalid Query"
    return input[input.index('"') + 1:input.rfind('"')]


def parse_query(query):
    if query in keywords:
        if query == 'help':
            return "Help Menu"
        else:
            exit(0)

    for joiner in joiners:
        if f' {joiner} ' in query:
            sliceIndex = query.index(f' {joiner} ')
            if (sliceIndex + 4 > len(query)):
                return "Invalid Query"
            firstQuery = query[0:sliceIndex]
            secondQuery = query[sliceIndex + 4:len(query)]
            if firstQuery not in keywords and secondQuery not in keywords:
                if parse_query(firstQuery) != "Invalid Query" and parse_query(secondQuery) != "Invalid Query":
                    if ' of ' not in firstQuery and ' of ' not in secondQuery:
                        return parse_query(firstQuery) + f' {joiner} ' + parse_query(secondQuery)
                    else:
                        return "Can't conjoin an 'of' check"
                else:
                    return "Invalid Query"
            else:
                return "Invalid Query"

    for operator in operators:
        if f' {operator} ' in query:
            sliceIndex = query.index(f' {operator} ')
            if (sliceIndex + 4 > len(query)):
                return "Invalid Query"
            firstTerm = query[0:sliceIndex]
            secondTerm = query[sliceIndex + 4:len(query)]
            input = get_user_input(query)
            if input == "Invalid Query" and secondTerm != 'all':
                return "Invalid Query"
            if firstTerm in valid_eq_check and operator in eq_operators:
                if firstTerm != 'title':
                    return get_title_from_firestore(firstTerm, operator, input)
                else:
                    return get_info_from_firestore(input)
            elif firstTerm in valid_comp_check and operator in comp_operators:
                if not is_valid_num(input):
                    return "Invalid Query"
                return get_title_from_firestore(firstTerm, operator, input)
            elif firstTerm in valid_belonging_check and operator == 'of':
                if secondTerm == 'all':
                    rtn_str = ""
                    for movie in movies:
                        rtn_str += get_field_from_firestore(firstTerm, movie)
                    return rtn_str
                else:
                    return get_field_from_firestore(firstTerm, input)

    return "Invalid Query"


if __name__ == '__main__':
    contQueries = True
    while(contQueries):
        query = input("> ")
        print(parse_query(query))
    exit(0)