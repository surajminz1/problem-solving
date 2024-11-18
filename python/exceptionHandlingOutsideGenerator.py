# Generator:
# write code to demo exception handing outside the generator and use generator.throw()

def gen_with_error():
    yield 1
    raise ValueError("Error inside generator")

def main():
    g = gen_with_error()
    print(next(g))
    try:
        g.throw(ValueError, "Error thrown")
    except ValueError as e:
        print(e)
        
if __name__ == "__main__":
    main()