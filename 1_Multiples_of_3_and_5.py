#Problem 1: Multiples of 3 and 5::

def main():
    sum = 0
    _range = input("range=")

    for i in range(1, _range):
        if(i%3 == 0 or i%5 == 0):
            sum = sum + i

    print sum

if __name__ == '__main__':
    main()
