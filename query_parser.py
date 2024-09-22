import re

from firebase_interface import get_title_from_firestore, get_field_from_firestore, get_info_from_firestore, load_movies

fields = ['title', 'rating', 'year', 'duration', 'director', 'genre', 'viewers', 'rank']
operators = ['==', '>', '<', '>=', '<=', '!=', 'of']
joiners = ['||', '&&']
keywords = ['help', 'quit']
valid_eq_check = ['title', 'director', 'genre', 'viewers']
valid_comp_check = ['year', 'rank', 'rating', 'duration']
valid_belonging_check = fields
eq_operators = ['==', '!=']
comp_operators = ['==', '>', '<', '>=', '<=', '!=']
movies = load_movies()

INVALID_QUERY = ["Invalid Query"]


def is_valid_num(num):
    if num.replace('.', '', 1).isdigit():
        return True
    return False


def get_user_input(user_input):
    if '"' not in user_input or user_input.index('"') == user_input.rfind('"'):
        return INVALID_QUERY
    return user_input[user_input.index('"') + 1:user_input.rfind('"')]


def input_not_found(input_list):
    if len(input_list) == 1 and re.fullmatch(r"Could not find '.*' in database", input_list[0]):
        return True
    return False


def help_menu():
    menu = ['Queryable column keywords: title, rating, year, duration, director, genre, viewers, rank',
            'Query operators: ==, >, >=, <, <=, !=, of, all',
            'Query joiners: &&, ||',
            'Query Structure: keyword operator "input"',
            'Compound Query: keyword operator "input" joiner keyword operator "input"',
            'Note: The query input is case sensitive and the inputs must be in double quotes',
            'Example query:',
            '> director of "Star Wars"',
            'George Lucas']
    return menu


def parse_query(query):
    if query in keywords:
        if query == 'help':
            return help_menu()
        else:
            exit(0)

    for joiner in joiners:
        if f' {joiner} ' in query:
            sliceIndex = query.index(f' {joiner} ')
            if sliceIndex + 4 > len(query):
                return INVALID_QUERY
            firstQuery = query[0:sliceIndex]
            secondQuery = query[sliceIndex + 4:len(query)]
            if firstQuery not in keywords and secondQuery not in keywords:
                if parse_query(firstQuery) != INVALID_QUERY and parse_query(secondQuery) != INVALID_QUERY:
                    if ' of ' not in firstQuery and ' of ' not in secondQuery:
                        first_return = parse_query(firstQuery)
                        second_return = parse_query(secondQuery)
                        if input_not_found(first_return):
                            return first_return
                        if input_not_found(second_return):
                            return second_return
                        compound_return = []
                        if joiner == '&&':
                            for item in first_return:
                                if item in second_return:
                                    compound_return.append(item)
                        else:
                            for item in first_return:
                                if item not in compound_return:
                                    compound_return.append(item)
                            for item in second_return:
                                if item not in compound_return:
                                    compound_return.append(item)
                        return compound_return
                    else:
                        return ["Can't conjoin an 'of' check"]
                else:
                    return INVALID_QUERY
            else:
                return INVALID_QUERY

    for operator in operators:
        if f' {operator} ' in query:
            sliceIndex = query.index(f' {operator} ')
            if sliceIndex + 4 > len(query):
                return INVALID_QUERY
            firstTerm = query[0:sliceIndex]
            secondTerm = query[sliceIndex + 4:len(query)]
            input = get_user_input(query)
            if input == INVALID_QUERY:
                if secondTerm != 'all' or operator != 'of':
                    return INVALID_QUERY
            if firstTerm in valid_eq_check and operator in eq_operators:
                return get_title_from_firestore(firstTerm, operator, input)
            elif firstTerm in valid_comp_check and operator in comp_operators:
                if not is_valid_num(input):
                    return INVALID_QUERY
                return get_title_from_firestore(firstTerm, operator, float(input))
            elif firstTerm in valid_belonging_check and operator == 'of':
                if firstTerm == 'title' and secondTerm != 'all':
                    return INVALID_QUERY
                if secondTerm == 'all':
                    field_list = []
                    for movie in movies:
                        rtn_list = get_field_from_firestore(firstTerm, movie)
                        for item in rtn_list:
                            if item not in field_list:
                                field_list.append(item)
                    return field_list
                else:
                    return get_field_from_firestore(firstTerm, input)

    return INVALID_QUERY


def print_output(output_list):
    rtn_str = ""
    for item in output_list:
        rtn_str += str(item) + "\n"
    if rtn_str != "":
        return rtn_str.rstrip('\n')
    else:
        return "N/A"


if __name__ == '__main__':
    contQueries = True
    while contQueries:
        query = input("> ")
        print(print_output(parse_query(query)))
    exit(0)
