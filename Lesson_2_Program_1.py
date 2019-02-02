# Write a program, which find all the numbers between 100 and 500
# such that each digit of the number is odd and then print the numbers.
# For example, 111 is the first number between 100 and 500 which all the digits are odd.
# you may want to use for loop, and list to program this task)

num1 = 100
num_list = []

while num1 <= 500:  # while loop will execute until num1 is greater than or equal to 500

    hundreds_digit = num1 // 100        # will produce the hundreds digit of num1
    tens_digit = (num1 % 100) // 10     # will produce the tens digit of num1
    ones_digit = num1 % 10              # will produce the ones digit of num1

    hundreds_test = hundreds_digit % 2      # test to see if hundreds digit is even
    tens_test = tens_digit % 2              # test to see if tens digit is even
    ones_test = ones_digit % 2              # test to see if ones digit is even

# bool statements set to false for each digit test
    hundreds_bool = False
    tens_bool = False
    ones_bool = False


# if the mod of each digit is not equal to zero, the bool test will be set to true (tests each digit)
    if hundreds_test != 0:
        hundreds_bool = True
    else:
        hundreds_bool = False

    if tens_test != 0:
        tens_bool = True
    else:
        tens_bool = False

    if ones_test != 0:
        ones_bool = True
    else:
        ones_bool = False

    # if all digits are odd, add num1 to num_list
    if ones_bool == True and tens_bool == True and hundreds_bool == True:
        list.append(num_list, num1)
        num1 = num1 + 1

    else:
        num1 = num1 + 1

print("The list of numbers between 100 and 500 in which each digit is odd:")
print(num_list)     # print number list with all numbers in each digit

