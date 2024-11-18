# Generator:
# create a generator object that will print the multiples of 5 between the range of 0 to 5 which are also divisible by 2

def main():

    # generator object
    exp_generator = (i * 5 for i in range(5) if i%2 == 0)

    # Use next to iterate over a generator object
    for i in exp_generator:
        print(i)
        
if __name__ == "__main__":
    main()