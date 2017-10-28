#Problem 2: Even Fibonacci numbers::

def main():
    prev_prev_value = current_value = sum = 0
    prev_value = 1
    four_million = 4000000

    while(current_value <= four_million+1):
        current_value = prev_prev_value + prev_value
        if(current_value%2 == 0):
            sum = sum + current_value
        prev_value = prev_prev_value
        prev_prev_value = current_value
    print sum

if __name__ == '__main__':
    main()
