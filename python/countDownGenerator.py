# Generator:
# create a generator object that will print the multiples of 5 between the range of 0 to 5 which are also divisible by 2

def count_down_generator(n):
    while n > 0:
        yield n
        n -= 1

def main():

    # generator object
    generator = count_down_generator(5)
    
    # Use next to iterate over a generator object
    for num in generator:
        print(num)
        
if __name__ == "__main__":
    main()