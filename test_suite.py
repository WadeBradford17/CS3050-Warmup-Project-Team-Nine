from query_parser import parse_query, print_output


def rank_equality_test():
    test_input = '"8"'
    expected = "Pulp Fiction"
    result = print_output(parse_query('rank == ' + test_input))

    if expected == result:
        print("PASSED rank_equality_test")
    else:
        print("FAILED rank_equality_test")

    return


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


def rank_greater_than_test():
    test_input = '"8"'
    # TODO: decide which expected result is correct
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King"
    result = print_output(parse_query('rank > ' + test_input))


    if expected == result:
        print("PASSED rank_greater_than_test")
    else:
        print("FAILED rank_greater_than_test")

    return


def rank_greater_than_equal_test():
    test_input = '"8"'
    # TODO: decide which expected result is correct
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King"
    result = print_output(parse_query('rank >= ' + test_input))

    if expected == result:
        print("PASSED rank_greater_than_equal_test")
    else:
        print("FAILED rank_greater_than_equal_test")

    return


def rank_less_than_test():
    test_input = '"8"'
    # TODO: decide which expected result is correct
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King"
    result = print_output(parse_query('rank < ' + test_input))

    if expected == result:
        print("PASSED rank_less_than_test")
    else:
        print("FAILED rank_less_than_test")

    return


def rank_less_than_equal_test():
    test_input = '"8"'
    # TODO: decide which expected result is correct
    expected = "The Shawshank Redemption\nThe Godfather\nThe Dark Knight\nThe Godfather Part II\n12 Angry Men\n" + \
               "Schindler's List\nThe Lord of the Rings: The Return of the King"
    result = print_output(parse_query('rank <= ' + test_input))

    if expected == result:
        print("PASSED rank_less_than_equal_test")
    else:
        print("FAILED rank_less_than_equal_test")

    return


def rank_of_test():
    test_input = '"Interstellar"'
    expected = "27"
    result = print_output(parse_query('rank of ' + test_input))

    if expected == result:
        print("PASSED rank_of_test")
    else:
        print("FAILED rank_of_test")

    return


def title_comparison_test():
    test_input = '"The Dark Knight"'
    expected = ""  # TODO: enter expected into this test case
    result = print_output(parse_query('title == ' + test_input))

    if expected == result:
        print("PASSED title comparison test")
    else:
        print("FAILED title comparison test")

    return


def title_of_test():
    test_input = '"The Dark Knight"'
    expected = "Invalid Query"
    result = print_output(parse_query('title of ' + test_input))

    if expected == result:
        print("PASSED title of test")
    else:
        print("FAILED title of test")

    return


rank_equality_test()
rank_not_equal_test()
rank_greater_than_test()
rank_greater_than_equal_test()
rank_less_than_test()
rank_less_than_equal_test()
rank_of_test()
title_comparison_test()
title_of_test()
