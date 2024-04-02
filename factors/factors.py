import math

def factorize(num):
    factors = []
    # Find factors using trial division method
    for i in range(2, int(math.sqrt(num)) + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors

def factorize_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            num = int(line.strip())
            factors = factorize(num)
            # Output factorization in the required format
            print(f"{num}={'*'.join(map(str, factors[:2]))}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python factors.py <file>")
        sys.exit(1)
    filename = sys.argv[1]
    factorize_file(filename)

