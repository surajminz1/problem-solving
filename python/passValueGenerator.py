# Generator:
# create a stateful generator to send value from outside and receive inside generator

def stateful_generator():
    # receive value from outside
    value = yield
    while True:
        value = yield value * 2

def main():

    # generator object
    generator = stateful_generator()

    # kick start the generator and print the processed data
    next(generator)
    # pass value to to the generator using send()
    print(generator.send(10))
        
if __name__ == "__main__":
    main()