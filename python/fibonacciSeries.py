# Print fibonacci series

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    for i in range (0, 10):
        f = fib(i)
        print(str(f)+ " " + str(f * f))
        
if __name__ == "__main__":
    main()