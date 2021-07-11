def is_palindrome(word):
    print (word[::-1])
    if (word[::-1] == word):
        print ("its a palindrome")
    else:
        print ("Its not a palindrome")
is_palindrome("malayalam")