# Generator:
# Write code to demo to create simple generator object and iterate through it using next

# fibonacci generator function
def fib_generator(num_limit):
    a, b = 0, 1
    while b < num_limit:
        yield b
        a, b = b, a + b

def main():

    # generator object
    x = fib_generator(200)

    # Use next to iterate over a generator object
    for i in x:
        print(i)
        
if __name__ == "__main__":
    main()