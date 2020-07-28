def main():
    resolve1()

def resolve1():
    num_multiples = 0
    for i in range(1, 1000):
        if i%15 == 0:
            num_multiples += i
        elif i%5 == 0:
            num_multiples += i
        elif i%3 == 0:
            num_multiples += i

    print(num_multiples)

if __name__ == '__main__':
    main()
