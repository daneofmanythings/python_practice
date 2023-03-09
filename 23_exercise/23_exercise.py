"https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html"

# Given two .txt files that have lists of numbers in them,
# find the numbers that are overlapping.
# One .txt file has a list of all prime numbers under 1000,
# and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be 
# divided by any other number. And yes, happy numbers are a 
# real thing in mathematics - you can look it up on Wikipedia.
# The explanation is easier with an example, which I will describe below.)


from prime_generator import seive_of_eratosthenes
from happy_generator import happy_numbers


# Global file names to write to.
PRIME_PATH = "text_files/prime_path.txt"
HAPPY_PATH = "text_files/happy_path.txt"


def generate_txt_files(upper_bound:int) -> None :
    '''Using the happy and prime generators, makes and writes files
    containing happy and prime numbers within the upper_bound parameter'''

    # Validating arguement value
    try :
        upper_bound = int(upper_bound)
    except ValueError :
        raise ValueError('upper_bound parameter must be an integer')

    # Generating the lists
    primes = seive_of_eratosthenes(upper_bound)
    happies = happy_numbers(upper_bound)

    # Writing the primes file
    with open(PRIME_PATH, 'w') as p :
        p.write(' '.join(map(str, primes)))

    #Writing the happies file
    with open(HAPPY_PATH, 'w') as h :
        h.write(' '.join(map(str, happies)))


def compare_values(collection1, collection2) -> set :
    '''Takes in two collections or generators of elements and returns a set 
    containing their intersection'''

    set1, set2 = set(collection1), set(collection2)

    return set1.intersection(set2)

def main() :
    
    generate_txt_files(1000)

    with open(PRIME_PATH, 'r') as p:
        primes = p.read()

    with open(HAPPY_PATH, 'r') as h:
        happies = h.read()

    primes = (int(num) for num in primes.split())
    happies = (int(num) for num in happies.split())

    return compare_values(primes, happies)


if __name__ == "__main__":
    print(main())
