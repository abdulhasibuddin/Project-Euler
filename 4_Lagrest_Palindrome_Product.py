#Problem 4: Largest palindrome product::
#answer 906609 (993 X 913) can be found by brute forcing from top to bottom!

def main():
    palindrome_list = []
    lower_range = upper_range = 0
    num_digit = input("Number of digits = ")

    for i in range(1, num_digit+1):
        lower_range = lower_range*10 + 1
        upper_range = upper_range*10 + 9

    for i in range(upper_range, lower_range-1, -1):
        for j in range(upper_range, lower_range-1, -1):
            num = i*j
            rev_num = str(num)[::-1]
            if(str(num) == rev_num):
                palindrome_list.append(num)
    print max(palindrome_list)

if __name__ == '__main__':
    main()
