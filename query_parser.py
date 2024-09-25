import re

# import firebase_admin
from firebase_interface import get_title_from_firestore, get_field_from_firestore, get_info_from_firestore, get_unique_entries_of_collection_from_firestore, load_movies

# fields, operators, joiners, and keywords are used to parse the user query
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

#is_valid_num() checks if the input is a valid number
#input: num (string)
#output: True if num is a valid number, False otherwise
def is_valid_num(num):
    if num.replace('.', '', 1).isdigit():
        return True
    return False

# get_user_input() gets the input from the user query
# input: query (string)
# output: the input from the user query
def get_user_input(query):
    if '"' not in query or query.index('"') == query.rfind('"'):
        if query[len(query) - 3:len(query)] == 'all':
            return 'all'
        return INVALID_QUERY
    return query[query.index('"') + 1:query.rfind('"')]

# input_not_found() checks if the input is not found in the database
# input: input_list (list)
# output: True if the input is not found in the database, False otherwise
def input_not_found(input_list):
    if len(input_list) == 1 and re.fullmatch(r"Could not find '.*' in database", input_list[0]):
        return True
    return False

# help_menu() returns the help menu
# output: the help menu
def help_menu():
    menu = ['Queryable column keywords: title, rating, year, duration, director, genre, viewers, rank',
            'Query operators: ==, >, >=, <, <=, !=, of, all',
            'Query joiners: &&, ||',
            'Query Structure: keyword operator "input"',
            'Compound Query: keyword operator "input" joiner keyword operator "input"',
            'Note: The query input is case sensitive and the inputs must be in double quotes',
            'Example query:',
            '> director of "Star Wars"',
            'George Lucas',
            'To see the movies availabe in the database, use the query "title of all"']
    return menu

# parse_query() parses the user query
# input: query (string)
# output: the parsed query
def parse_query(query):
    if query in keywords:
        if query == 'help':
            return help_menu()
        else:
            exit(0)
    #iterate through joiners
    for joiner in joiners:
        #check if query is a compound query
        if f' {joiner} ' in query:
            sliceIndex = query.index(f' {joiner} ')
            if sliceIndex + 4 > len(query):
                return INVALID_QUERY
            firstQuery = query[0:sliceIndex]
            secondQuery = query[sliceIndex + 4:len(query)]
            #check if the first and second query are not keywords
            if firstQuery not in keywords and secondQuery not in keywords:
                if parse_query(firstQuery) != INVALID_QUERY and parse_query(secondQuery) != INVALID_QUERY:
                    #check if the first and second query are not 'of' checks
                    if ' of ' not in firstQuery and ' of ' not in secondQuery:
                        first_return = parse_query(firstQuery)
                        second_return = parse_query(secondQuery)
                        #check if the input is not found
                        if input_not_found(first_return):
                            return first_return
                        if input_not_found(second_return):
                            return second_return
                        compound_return = []
                        #check if the joiner is '||' or '&&'
                        if joiner == '&&':
                            for item in first_return:
                                if item in second_return:
                                    compound_return.append(item)
                        #joiner is '||'
                        else:
                            #add the items from the first and second query to the compound return list
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
            
    #iterate through fields
    for field in fields:
        for operator in operators:
            #check if the operator is in the query
            if re.fullmatch(rf'{field} {operator} (".*"|all)', query):
                input = get_user_input(query)
                #check if the input is invalid
                if input == 'all' and operator != 'of':
                    return INVALID_QUERY
                if field in valid_eq_check and operator in eq_operators:
                    return get_title_from_firestore(field, operator, input)
                elif field in valid_comp_check and operator in comp_operators:
                    if not is_valid_num(input):
                        return INVALID_QUERY
                    return get_title_from_firestore(field, operator, float(input))
                #check if the field is 'of'
                elif field in valid_belonging_check and operator == 'of':
                    #check if the input is invalid
                    if field == 'title' and input != 'all':
                        return INVALID_QUERY
                    #check if the input is not found
                    if input == 'all':
                        if field == 'genre' or field == 'viewers':
                            return get_unique_entries_of_collection_from_firestore(field)
                        field_list = []
                        #iterate through movies
                        #get the field from the movie
                        #add the field to the field list if it is not already in the list
                        for movie in movies:
                            rtn_list = get_field_from_firestore(field, movie)
                            for item in rtn_list:
                                if item not in field_list:
                                    field_list.append(item)
                        return field_list
                    else:
                        return get_field_from_firestore(field, input)

    return INVALID_QUERY

# print_output() prints the output list
# input: output_list (list)
# output: the output list
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
