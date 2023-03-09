'''https://www.practicepython.org/exercise/2014/05/21/15-reverse-word-order.html'''

# Write a program (using functions!) that asks the user for a long string 
# containing multiple words. Print back to the user the same string,
# except with the words in backwards order.

def sentence_reverser(sentence:str) -> str :
    return ' '.join(a for a in sentence.split()[::-1])

SENTENCE = 'Hello, please reverse me.'

print(sentence_reverser(SENTENCE))