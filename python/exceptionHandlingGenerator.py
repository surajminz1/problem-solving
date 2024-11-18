# Generator:
# write code to handle exceptions within a generator using standard try-except blocks

def error_handling_generator():
    try:
        yield 1
        yield 2
        raise ValueError("An error occurred")
        yield 3
    except ValueError as e:
        print(e)

def main():
    gen = error_handling_generator()
    print(next(gen))
    print(next(gen))
    print(next(gen))  # This will trigger the exception        

if __name__ == "__main__":
    main()