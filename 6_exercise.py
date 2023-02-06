'''https://www.practicepython.org/exercise/2014/03/12/06-string-lists.html'''

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

def main() :
    string = input('Enter a string to check for palindome-ity >>> ')

    return string == string[::-1]

if __name__ == '__main__' :
    print(main())