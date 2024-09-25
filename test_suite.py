from query_parser import parse_query, print_output


# check if querying a specific rank returns the correct result
def rank_equality_test():
    test_input = '"8"'
    expected = "Pulp Fiction"
    result = print_output(parse_query('rank == ' + test_input))

    if expected == result:
        print("PASSED rank_equality_test")
    else:
        print("FAILED rank_equality_test")

    return

# check if querying rank not equal returns all movies except the one specified
def rank_not_equal_test():
    test_input = '"8"'
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" \
               "Schindler's List\nThe Lord of the Rings: The Return of the King\n" \
               "The Lord of the Rings: The Fellowship of the Ring\nIl buono, il brutto, il cattivo\nForrest Gump\n" \
               "Fight Club\nInception\nThe Lord of the Rings: The Two Towers\nThe Empire Strikes Back\nThe Matrix\n" \
               "Goodfellas\nOne Flew Over the Cuckoo's Nest\nSe7en\nShichinin no samurai\nIt's a Wonderful Life\n" \
               "The Silence of the Lambs\nCidade de Deus\nSaving Private Ryan\nLa vita e bella\nThe Green Mile\n" \
               "Interstellar\nStar Wars\nTerminator 2: Judgment Day\nBack to the Future"
    result = print_output(parse_query('rank != ' + test_input))

    if expected == result:
        print("PASSED rank_not_equal_test")
    else:
        print("FAILED rank_not_equal_test")

    return

# check if rank > works
def rank_greater_than_test():
    test_input = '"8"'
    expected = "The Lord of the Rings: The Fellowship of the Ring\nIl buono, il brutto, il cattivo\nForrest Gump\n" \
               "Fight Club\nInception\nThe Lord of the Rings: The Two Towers\nThe Empire Strikes Back\nThe Matrix\n" \
               "Goodfellas\nOne Flew Over the Cuckoo's Nest\nSe7en\nShichinin no samurai\nIt's a Wonderful Life\n" \
               "The Silence of the Lambs\nCidade de Deus\nSaving Private Ryan\nLa vita e bella\nThe Green Mile\n" \
               "Interstellar\nStar Wars\nTerminator 2: Judgment Day\nBack to the Future"
    result = print_output(parse_query('rank > ' + test_input))

    if expected == result:
        print("PASSED rank_greater_than_test")
    else:
        print("FAILED rank_greater_than_test")

    return

# check if rank >= works
def rank_greater_than_equal_test():
    test_input = '"8"'
    expected = "Pulp Fiction\n" \
               "The Lord of the Rings: The Fellowship of the Ring\nIl buono, il brutto, il cattivo\nForrest Gump\n" \
               "Fight Club\nInception\nThe Lord of the Rings: The Two Towers\nThe Empire Strikes Back\nThe Matrix\n" \
               "Goodfellas\nOne Flew Over the Cuckoo's Nest\nSe7en\nShichinin no samurai\nIt's a Wonderful Life\n" \
               "The Silence of the Lambs\nCidade de Deus\nSaving Private Ryan\nLa vita e bella\nThe Green Mile\n" \
               "Interstellar\nStar Wars\nTerminator 2: Judgment Day\nBack to the Future"
    result = print_output(parse_query('rank >= ' + test_input))

    if expected == result:
        print("PASSED rank_greater_than_equal_test")
    else:
        print("FAILED rank_greater_than_equal_test")

    return

# check if rank < works
def rank_less_than_test():
    test_input = '"8"'
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King"
    result = print_output(parse_query('rank < ' + test_input))

    if expected == result:
        print("PASSED rank_less_than_test")
    else:
        print("FAILED rank_less_than_test")

    return

# check if rank <= works
def rank_less_than_equal_test():
    test_input = '"8"'
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King\nPulp Fiction"
    result = print_output(parse_query('rank <= ' + test_input))

    if expected == result:
        print("PASSED rank_less_than_equal_test")
    else:
        print("FAILED rank_less_than_equal_test")

    return

# check if rank of works
def rank_of_test():
    test_input = '"Interstellar"'
    expected = "27"
    result = print_output(parse_query('rank of ' + test_input))

    if expected == result:
        print("PASSED rank_of_test")
    else:
        print("FAILED rank_of_test")

    return

# check if title == returns the title
def title_comparison_test():
    test_input = '"The Dark Knight"'
    expected = "The Dark Knight"
    result = print_output(parse_query('title == ' + test_input))

    if expected == result:
        print("PASSED title comparison test")
    else:
        print("FAILED title comparison test")

    return

# check that title > is not accepted
def title_greater_than_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title > ' + test_input))

    if expected == result:
        print("PASSED title_greater_than_test")
    else:
        print("FAILED title_greater_than_test")

    return

# check that title >= is not accepted
def title_greater_than_equal_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title >= ' + test_input))

    if expected == result:
        print("PASSED title_greater_than_equal_test")
    else:
        print("FAILED title_greater_than_equal_test")

    return

# check that title < is not accepted
def title_less_than_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title < ' + test_input))

    if expected == result:
        print("PASSED title_less_than_test")
    else:
        print("FAILED title_less_than_test")

    return

# check that title <= is not accepted
def title_less_than_equal_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title <= ' + test_input))

    if expected == result:
        print("PASSED title_less_than_equal_test")
    else:
        print("FAILED title_less_than_equal_test")

    return

# check that title of is not accepted
def title_of_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title of ' + test_input))

    if expected == result:
        print("PASSED title of test")
    else:
        print("FAILED title of test")

    return

# check that year = works
def year_equality_test():
    test_input = '"1999"'
    expected = "The Green Mile\nFight Club\nThe Matrix"
    result = print_output(parse_query('year == ' + test_input))

    if expected == result:
        print("PASSED year_equality_test")
    else:
        print("FAILED year_equality_test")

    return

# check that year != works as intended
def year_not_equal_test():
    test_input = '"1999"'
    expected_set = {"The Shawshank Redemption",
                    "The Godfather",
                    "The Dark Knight",
                    "The Godfather Part II",
                    "12 Angry Men",
                    "Schindler's List",
                    "The Lord of the Rings: The Return of the King",
                    "Pulp Fiction",
                    "The Lord of the Rings: The Fellowship of the Ring",
                    "Il buono, il brutto, il cattivo",
                    "Forrest Gump",
                    "Inception",
                    "The Lord of the Rings: The Two Towers",
                    "The Empire Strikes Back",
                    "Goodfellas",
                    "One Flew Over the Cuckoo's Nest",
                    "Se7en",
                    "Shichinin no samurai",
                    "It's a Wonderful Life",
                    "The Silence of the Lambs",
                    "Cidade de Deus",
                    "Saving Private Ryan",
                    "La vita e bella",
                    "Interstellar",
                    "Star Wars",
                    "Terminator 2: Judgment Day",
                    "Back to the Future"}

    result = print_output(parse_query('year != ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED year_not_equal_test")
    else:
        print("FAILED year_not_equal_test")

    return

# check that year > works
def year_greater_than_test():
    test_input = '"1999"'
    expected_set = {"The Dark Knight",
                    "The Lord of the Rings: The Return of the King",
                    "The Lord of the Rings: The Fellowship of the Ring",
                    "Inception",
                    "Cidade de Deus",
                    "Interstellar",
                    "The Lord of the Rings: The Two Towers"}

    result = print_output(parse_query('year > ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED year_greater_than_test")
    else:
        print("FAILED year_greater_than_test")

    return

# check that year >= works
def year_greater_than_equal_test():
    test_input = '"1999"'
    expected_set = {"The Dark Knight",
                    "The Lord of the Rings: The Return of the King",
                    "The Lord of the Rings: The Fellowship of the Ring",
                    "Inception",
                    "Cidade de Deus",
                    "Interstellar",
                    "The Lord of the Rings: The Two Towers",
                    "The Green Mile",
                    "Fight Club",
                    "The Matrix"}

    result = print_output(parse_query('year >= ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED year_greater_than_equal_test")
    else:
        print("FAILED year_greater_than_equal_test")

    return

# check that year < works
def year_less_than_test():
    test_input = '"1972"'
    expected_set = {"12 Angry Men",
                    "It's a Wonderful Life",
                    "Shichinin no samurai",
                    "Il buono, il brutto, il cattivo"}

    result = print_output(parse_query('year < ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED year_less_than_test")
    else:
        print("FAILED year_less_than_test")

    return

# check that year <= works
def year_less_than_equal_test():
    test_input = '"1966"'
    expected_set = {"12 Angry Men",
                    "It's a Wonderful Life",
                    "Shichinin no samurai",
                    "Il buono, il brutto, il cattivo"}

    result = print_output(parse_query('year <= ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED year_less_than_equal_test")
    else:
        print("FAILED year_less_than_equal_test")

    return

# check that year of works
def year_of_test():
    test_input = '"The Dark Knight"'
    expected = "2008"
    result = print_output(parse_query('year of ' + test_input))

    if expected == result:
        print("PASSED year of test")
    else:
        print("FAILED year of test")

    return

# check that viewers = works
def viewers_equals_test():
    test_input = '"Jasper Henderson"'
    expected_set = {"It's a Wonderful Life",
                    "The Empire Strikes Back",
                    "Saving Private Ryan",
                    "The Dark Knight",
                    "Forrest Gump",
                    "The Lord of the Rings: The Two Towers",
                    "Star Wars",
                    "The Lord of the Rings: The Return of the King",
                    "Back to the Future",
                    }

    result = print_output(parse_query('viewers == ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED viewers_equals_test")
    else:
        print("FAILED viewers_equals_test")

    return

# check that viewers of returns N/A on an empty optional
def viewers_of_shawshank_test():
    test_input = '"The Shawshank Redemption"'
    expected_set = {"N/A"}

    result = print_output(parse_query('viewers of ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED viewers_of_shawshank_test")
    else:
        print("FAILED viewers_of_shawshank_test")

    return

# check that viewers of works on an optional with viewers
def viewers_of_inception_test():
    test_input = '"Inception"'
    expected_set = {"Wade Bradford",
                    "Cam Kirn"}

    result = print_output(parse_query('viewers of ' + test_input))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED viewers_of_inception_test")
    else:
        print("FAILED viewers_of_inception_test")

    return

# check the and joiner works
def and_joiner_test():
    expected = "The Dark Knight"
    result = print_output(parse_query('year == "2008" && director == "Christopher Nolan"'))

    if expected == result:
        print("PASSED and_joiner_test")
    else:
        print("FAILED and_joiner_test")

    return

# check the or joiner works
def or_joiner_test():
    expected_set = {"The Dark Knight",
                    "12 Angry Men"}
    result = print_output(parse_query('year == "2008" || director == "Sidney Lumet"'))
    result_set = set(result.split('\n'))

    if expected_set == result_set:
        print("PASSED or_joiner_test")
    else:
        print("FAILED or_joiner_test")

    return

# check an empty input is not accepted
def empty_input_test():
    expected = "Invalid Query"
    result = print_output(parse_query(''))

    if expected == result:
        print("PASSED empty_input_test")
    else:
        print("FAILED empty_input_test")

    return

# check that an input not in quotes is not accepted
def input_not_in_quotes_test():
    expected = "Invalid Query"
    result = print_output(parse_query('year == 2008'))

    if expected == result:
        print("PASSED input_not_in_quotes_test")
    else:
        print("FAILED input_not_in_quotes_test")

    return

# check that of with and joiner is not accepted
def of_with_and_test():
    expected = "Invalid Query"
    result = print_output(parse_query('year of "Interstellar" && director == "Peter Jackson'))

    if expected == result:
        print("PASSED of_with_and_test")
    else:
        print("FAILED of_with_and_test")

    return

# check that of with or joiner is not accepted
def of_with_or_test():
    expected = "Invalid Query"
    result = print_output(parse_query('year of "Interstellar" || director == "Peter Jackson'))

    if expected == result:
        print("PASSED of_with_or_test")
    else:
        print("FAILED of_with_or_test")

    return

# check that of with no input returns correct message
def empty_of_test():
    expected = "Could not find '' in database"
    result = print_output(parse_query('year of ""'))

    if expected == result:
        print("PASSED empty_of_test")
    else:
        print("FAILED empty_of_test")

    return

# check an empty side with a joiner is not accepted
def empty_joiner_first_test():
    expected = "Invalid Query"
    result = print_output(parse_query('|| director == "Peter Jackson"'))

    if expected == result:
        print("PASSED empty_joiner_first_test")
    else:
        print("FAILED empty_joiner_first_test")

    return

# check an empty side with a joiner is not accepted
def empty_joiner_second_test():
    expected = "Invalid Query"
    result = print_output(parse_query('director == "Peter Jackson"||'))

    if expected == result:
        print("PASSED empty_joiner_second_test")
    else:
        print("FAILED empty_joiner_second_test")

    return

# check an invalid side with a joiner is not accepted
def invalid_joiner_second_test():
    expected = "Invalid Query"
    result = print_output(parse_query('director == "Peter Jackson" || director james'))

    if expected == result:
        print("PASSED invalid_joiner_second_test")
    else:
        print("FAILED invalid_joiner_second_test")

    return

# check an invalid side with a joiner is not accepted
def invalid_joiner_first_test():
    expected = "Invalid Query"
    result = print_output(parse_query('director james || director == "Peter Jackson"'))

    if expected == result:
        print("PASSED invalid_joiner_first_test")
    else:
        print("FAILED invalid_joiner_first_test")

    return

# check two joiners
def two_joiner_test():
    expected = "The Lord of the Rings: The Two Towers"
    result = print_output(parse_query('year > "2001" && director == "Peter Jackson" && rating < "9"'))

    if expected == result:
        print("PASSED two_joiner_test")
    else:
        print("FAILED two_joiner_test")

    return

# check that more text after quotes is not accepted
def more_after_quotes():
    expected = "Invalid Query"
    result = print_output(parse_query('year > "2001" dire'))

    if expected == result:
        print("PASSED more_after_quotes")
    else:
        print("FAILED more_after_quotes")

    return

# check extra quotes doesn't break it
def extra_quotes():
    expected = """Could not find '2001" dire' in database"""
    result = print_output(parse_query('director of "2001" dire"'))

    if expected == result:
        print("PASSED extra_quotes")
    else:
        print("FAILED extra_quotes")

    return

# check that comparing a string with a keyword expecting a number is handled
def not_a_number_test():
    expected = "Invalid Query"
    result = print_output(parse_query('year > "Tom"'))

    if expected == result:
        print("PASSED not_a_number_test")
    else:
        print("FAILED not_a_number_test")

    return

# check that numbers with no match are handled
def number_has_no_match_test():
    expected = """Could not find '2000' in database"""
    result = print_output(parse_query('year == "2000"'))
    print(result)
    if expected == result:
        print("PASSED number_has_no_match_test")
    else:
        print("FAILED number_has_no_match_test")

    return



rank_equality_test()
rank_not_equal_test()
rank_greater_than_test()
rank_greater_than_equal_test()
rank_less_than_test()
rank_less_than_equal_test()
rank_of_test()
title_comparison_test()
title_greater_than_test()
title_greater_than_equal_test()
title_less_than_test()
title_less_than_equal_test()
title_of_test()
year_equality_test()
year_not_equal_test()
year_greater_than_test()
year_greater_than_equal_test()
year_less_than_test()
year_less_than_equal_test()
year_of_test()
viewers_equals_test()
viewers_of_shawshank_test()
viewers_of_inception_test()
and_joiner_test()
or_joiner_test()
empty_input_test()
input_not_in_quotes_test()
of_with_and_test()
of_with_or_test()
empty_of_test()
empty_joiner_first_test()
empty_joiner_second_test()
invalid_joiner_first_test()
invalid_joiner_second_test()
two_joiner_test()
more_after_quotes()
extra_quotes()
not_a_number_test()
number_has_no_match_test()



# all movie titles set
{"The Shawshank Redemption",
 "The Godfather",
 "The Dark Knight",
 "The Godfather Part II",
 "12 Angry Men",
 "Schindler's List",
 "The Lord of the Rings: The Return of the King",
 "Pulp Fiction",
 "The Lord of the Rings: The Fellowship of the Ring",
 "Il buono, il brutto, il cattivo",
 "Forrest Gump",
 "Fight Club",
 "Inception",
 "The Lord of the Rings: The Two Towers",
 "The Empire Strikes Back",
 "The Matrix",
 "Goodfellas",
 "One Flew Over the Cuckoo's Nest",
 "Se7en",
 "Shichinin no samurai",
 "It's a Wonderful Life",
 "The Silence of the Lambs",
 "Cidade de Deus",
 "Saving Private Ryan",
 "La vita e bella",
 "The Green Mile",
 "Interstellar",
 "Star Wars",
 "Terminator 2: Judgment Day",
 "Back to the Future"}
