# create a method that takes input x and subtract 2 from it and returns the result. 
# Now using decorator change the value of x

def add(func):
    def inner(x):
        return func(x+2)
    return inner

@add
def main(x):
    return x-2
    
if __name__ == "__main__":
    print(main(5))