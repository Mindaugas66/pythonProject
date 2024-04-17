user_input = input("Enter number sequence: ")
number_list = [int(digit) for digit in str(user_input)]
average = sum(number_list) / len(number_list)
print(number_list)
print(f"Total average number is {int(average)}")