def rec_pow(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * rec_pow(base, exponent - 1)

def main():
        b = int(input("Enter a base: "))
        e = int(input("Enter an exponent: "))
        print(f"The answer is {rec_pow(b, e)}")


if __name__ == '__main__':
    main()