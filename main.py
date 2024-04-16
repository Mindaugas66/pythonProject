# Parašykite programą, kuri leistų vartotojui įrašyti bet kokį kintamąjį
# skaičių ir jį suapvalinti iki tam tikro skaičiaus po kablelio.

while True:
    user_input = input("Enter a float number with 3 digits after the decimal point: ")
    try:
        number = float(user_input)
        if len(user_input.split('.')[1]) == 3:
            break
        else:
            print("Please enter a float number with exactly 3 digits after the decimal point.")
    except IndexError:
        print("Please enter a valid float number.")

print(f"Rounded number of: {user_input} is: {round(number, 2)}")