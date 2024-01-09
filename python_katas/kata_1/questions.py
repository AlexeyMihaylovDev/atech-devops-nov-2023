def sum_of_element(elements):
    s = 0
    for num in elements:
        s = s + num
    return s


def versing(word):
    # 1 Kata
    #
    # Given a string 'word', if its length is at least 3, add 'ing' to its end.
    # Unless it already ends in 'ing', in which case add 'ly' instead.
    # If the string length is less than 3, leave it unchanged.
    #
    # e.g.
    # teach -> teaching
    # do -> do
    # swimming -> swimmingly
    #
    # :param word: str
    # :return: Return the resulting string.



    return None


def words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words.

    For example:
    words_concatenation(['take', 'me', 'home']) returns 'take me home'

    :param words: list of str
    :return: Return the resulting string.
    """
    def words_concatenation(words):
        """
        1 Kata

        Given a list of words, write a program that concatenates the words.

        For example:
        words_concatenation(['take', 'me', 'home']) returns 'take me home'

        :param words: list of str
        :return: Return the resulting string.
        """
 
    return None


def reverse_words_concatenation(words):
    """
    1 Kata

    Given a list of words, write a program that concatenates the words in a reverse way

    For example:
    reverse_words_concatenation(['take', 'me', 'home']) returns 'home me take'

    :param words: list of str
    :return: Return the resulting string.
    """
    return None


def is_unique_string(some_str):
    for char in some_str:
        count = 0
        for letter in some_str:
            if letter == char :
                count+=1             
        if count > 1 :
            result = False
            break
        else:
            result = True          
    return result
    
    
def list_diff(elements):
    result = []
    result.append("None")
    #result[1] = {'None'}
    for i in range(1, len(elements)):
        try:
            result.append(int(elements[i] - elements[i-1]))
        except ValueError:
            result = "your sting have char"
            break
    return result
    

def prime_number(num):
    flag = False
    if num == 1:
        return False
    elif num > 1:
        # check for factors
        if (num % 2) == 0:
                flag = False
        else:
            flag = True
                # break out of loop
    # check if flag is True
    return flag


def palindrome_num(num):
    temp = num
    rev = 0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True
    else:
        return False
    

def pair_match(men, women):
    """
    3 Kata

    This function gets two dictionaries of the type:
    {
        "<name>": <age>
    }

    Where <name> is a string name, and <age> is an integer representing the age
    The function returns a pair of names (tuple), of from men dict, the other from women dict,
    where their absolute age differences is the minimal

    e.g.
    men = {"John": 20, "Abraham": 45}
    women = {"July": 18, "Kim": 26}

    The returned value should be a tuple ("John", "July") since:

    abs(John - Kim) = abs(20 - 26) = abs(-6) = 6
    abs(John - July) = abs(20 - 18) = abs(2) = 2
    abs(Abraham - Kim) = abs(45 - 26) = abs(19) = 19
    abs(Abraham - July) = abs(45 - 18) = abs(27) = 27

    :param men: dict mapping name -> age
    :param women: dict mapping name -> age
    :return: tuple (men_name, women_name) such their age absolute difference is the minimal
    """
    return None


def bad_average(a, b, c):
    """
    1 Kata

    This function gets 3 numbers and calculates the average.
    There is a mistake in the following implementation, you are required to fix it

    :return:
    """
    return a + b + c / 3


def best_student(grades):
    """
    1 Kata

    This function gets a dict of students -> grades mapping, and returns the student with the highest grade

    e.g.
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    will return "Natan"

    :param grades: dict of name -> grade mapping
    :return: str. some key from the dict
    """
    return None


def print_dict_as_table(some_dict):
    """
    1 Kata

    Prints dictionary keys and values as the following format. For:
    {
        "Ben": 78,
        "Hen": 88,
        "Natan": 99,
        "Efraim": 65,
        "Rachel": 95
    }

    The output will be:

    Key     Value
    -------------
    Ben     78
    Hen     88
    Natan   99
    Efraim  65
    Rachel  95

    :param some_dict:
    :return:
    """
    return None


def merge_dicts(dict1, dict2):
    
    return {**dict1 , **dict2}


def seven_boom(n):
    result = []
    N = 7
    sum = 0
    while N <= n:
        result.append(N)
        N +=7
    return result


def caesar_cipher(str_to_encrypt):
    """
    2 Kata

    This function encrypts the given string according to caesar cipher (a - d, b - e, ..., y - b, z - c etc...).
    Spaces remain as they are. You can assume the string contain a-z and A-Z chars only.

    e.g.
    Fly Me To The Moon -> Iob Ph Wr Wkh Prrq

    :return:
    """
    return None


def sum_of_digits(digits_str):
    """
    1 Kata

    Calculates the sum of digits in a string (you can assume the input is a string containing numeric digits only)

    e.g.
    '2524' -> 13
    '' -> 0
    '00232' -> 7


    :param digits_str: str of numerical digits only
    :return: int representing the sum of digits
    """
    result = 0 
    for num in digits_str:
        isInt = True
        try:
            int(num)
            result = result + int(num)
        except ValueError:
            isInt = False
            result = "your sting have char"
            break
    return result


if __name__ == '__main__':
    # print('\nsum_of_element:\n--------------------')
    # print(sum_of_element([1, 2, 3, 4, 5, 6]))

    # print('\nverbing:\n--------------------')
    # print(versing('walk'))
    # print(versing('swimming'))
    # print(versing('do'))

    # print('\nwords_concatenation:\n--------------------')
    # print(words_concatenation(['take', 'me', 'home']))

    # print('\nreverse_words_concatenation:\n--------------------')
    # print(reverse_words_concatenation(['take', 'me', 'home']))

    # print('\nis_unique_string:\n--------------------')
    # print(is_unique_string('aasdssdsederd'))
    # print(is_unique_string('12345tgbnh'))

    #print('\nlist_diff:\n--------------------')
    #print(list_diff([1, 2, 3, 8, 77, 0]))

    #print('\nprime_number:\n--------------------')
    #print(prime_number(13))
    #print(prime_number(22))

    # print('\npalindrome_num:\n--------------------')
    # print(palindrome_num(12221))
    # print(palindrome_num(577))
    # print(palindrome_num(686))

    # print('\npair_match:\n--------------------')
    # print(pair_match(
    #     {
    #         "John": 20,
    #         "Abraham": 45
    #     },
    #     {
    #         "July": 18,
    #         "Kim": 26
    #     }
    # ))

    # print('\nbad_average:\n--------------------')
    # print(bad_average(1, 2, 3))

    # print('\nbest_student:\n--------------------')
    # print(best_student({
    #     "Ben": 78,
    #     "Hen": 88,
    #     "Natan": 99,
    #     "Efraim": 65,
    #     "Rachel": 95
    # }))

    # print('\nprint_dict_as_table:\n--------------------')
    # print(print_dict_as_table({
    #     "Ben": 78,
    #     "Hen": 88,
    #     "Natan": 99,
    #     "Efraim": 65,
    #     "Rachel": 95
    # }))

    print('\nmerge_dicts:\n--------------------')
    print(merge_dicts({'a': 1}, {'b': 2}))

    #print('\nseven_boom:\n--------------------')
    #print(seven_boom(14))

    # print('\ncaesar_cipher:\n--------------------')
    # print(caesar_cipher('Fly Me To The Moon'))
    #print(type(int("7")))
    # print('\nsum_of_digits:\n--------------------')
    # print(sum_of_digits('1223432'))
    # print(sum_of_digits('v122343sad2'))
    