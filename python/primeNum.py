# Find prime numbera between 100 to 200

def prime_num(j, k):
    for num in range(j, k):
        if all(num%i != 0 for i in range(2, num)):
            print(num)

def main():
    prime_num(100, 200)

if __name__ == "__main__":
    main()