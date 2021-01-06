while True:
    string = input()
    d_string = string[::-1]

    if string == d_string:
        print(string + " is a palindrome.")
    else:
        print(string + " is not a palindrome.")
