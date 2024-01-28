def check_string(string1, string2):
    if string1 == string2:
        print(f"{string1} and {string2} are equal. ")
    else:
        print(f"{string1} and {string2} are not equal. ")
str1 = (1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 1, 2, 
              3, 1, 2, 1, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 1, 2, 
              3, 4, 1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 1, 2, 3, 1, 
              2, 1, 1, 2, 3, 4, 1, 2, 3)
numbers = (1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 1, 2, 3,
            1, 2, 1, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 1, 2, 3, 4,
              1, 2, 3, 1, 2, 1, 1, 2, 3, 4, 1, 2, 3, 1, 2, 1, 
              1, 2, 3, 4, 1, 2, 3)
conv = str(str1)
conv1 = str(numbers)

check_string(conv, conv1)