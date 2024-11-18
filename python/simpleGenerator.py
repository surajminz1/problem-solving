# Generator:
# Write code to demo simple generator function

# simple generator function
def simple_generator():
    yield 1
    yield 2
    yield 3

def main():

    # generator object
    x = simple_generator()

    # Use next to iterate over a generator object
    print(next(x))
    print(next(x))
    print(next(x))
    
if __name__ == "__main__":
    main()