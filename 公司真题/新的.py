def count_substr_by_formula(string):
    '''
    This function is used to calculate
    number of all possible substring of
    a string by a formula.
    '''

    substring = 0
    # length of the given string
    n = len(string)

    substring = n * (n + 1) // 2

    return substring

    # Time Complexity : O(1) {constant order}


def general_method(string):
    '''
    This function is used to calculate
    number of all possible substring of
    a string by using nested for loops.
    '''

    substring = 0
    n = len(string)
    # List to store all the calculated substrings
    substr = []

    for i in range(n):
        for j in range(i, n):
            substr.append(string[i:j])

    substring = len(substr)

    return substring

    # Time Complexity : O(n*n)


# Main Code
if __name__ == '__main__':
    string = 'ababaaabb'

    print('Total number of substring = %d' % count_substr_by_formula(string))
    print('Total number of substring = %d' % general_method(string))

