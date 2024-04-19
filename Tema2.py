name = input("Iveskite savo varda: ")
age = int(input("Kiek jum yra metu? "))

print(f"Sveiki, {name}, Jus esate gimes {2024 - age}")

sentence = input("Write a sentence: ")
print(sentence[::-1])
print(sentence[::2])

number1 = float(input("Choose a number: "))
number2 = float(input("Choose another number: "))
print(f"Atimtis: {number1} - {number2} = {number1 - number2}")
print(f"Daugyba: {number1} * {number2} = {number1 * number2}")
print(f"Dalyba: {number1} / {number2} = {number1 / number2}")
print(f"Sudetis: {number1} + {number2} = {number1 + number2}")

mylist = [5, 15, 45, 99, 78]
print(sum(mylist))

# Importuojami visi operatoriai iš operatoriaus modulio
from operator import *

# Sukuriamas sąrašas su penkiais skaičiais
mylist = [5, 15, 45, 99, 78]
# Pradinė sandauga nustatoma kaip 1
m = 1
# Einama per kiekvieną skaičių sąraše
for item in mylist:
    # Kiekvienas sąrašo elementas padauginamas su dabartine sandauga ir rezultatas priskiriamas sandaugai m
    m = mul(item, m)
# Išspausdinama galutinė sandauga
print(m)


def multlist(mylist):
    # Inicializuojama kintamasis result su pradine reiksme 1
    result = 1
    # Einama per kiekviena sąrašo elemento x
    for x in mylist:
        # Kiekvienas sąrašo elementas padauginamas su dabartine rezultato reikšme ir rezultatas priskiriamas kintamajam result
        result = result * x
    # Grąžinama sandauga visų sąrašo elementų
    return result


# Sukuriamas sąrašas su penkiais skaičiais
mylist = [5, 15, 45, 99, 78]
# Iškviečiama funkcija multlist su mylist kaip argumentu ir išspausdinamas grąžintas rezultatas
print(multlist(mylist))

import numpy

mylist = [5, 15, 45, 99, 78]

result1 = numpy.prod(mylist)
print(result1)

mylist = [1, 5, 98, 512, 6451, 11, 21]

print(max(mylist))

# Sukuriamas sąrašas
mylist = ["Minde", "Bananas", "Tevas", "Juozas"]
# Sukuriamas tuščias string'as su vienu tarpų simboliu tarp jų
sudeta = " "
# Einama per kiekvieną sąrašo elementą
for item in mylist:
    # Prie esamo sudeta string'o pridedamas dabartinis sąrašo elementas ir tarpas
    sudeta += item + " "
# Atspausdinamas sujungtas string'as
print(sudeta)

mylist = ["Minde", "Bananas", "Tevas", "Juozas"]
mylist1 = [1, 5, 9, 8, 4]
sudeta = mylist + mylist1

print(sudeta)

mynumbers = []

number = input("gimme a number: ")
number1 = input("gimme a second number: ")
number2 = input("gimme a third number: ")
mynumbers.append(number)
mynumbers.append(number1)
mynumbers.append(number2)

print(max(mynumbers))

mynumbers = []

while True:
    try:
        number = input("Enter a number: ")
        number = float(number)  # Convert input to float
        mynumbers.append(number)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue

    if len(mynumbers) >= 3:
        break

print("Maximum number:", max(mynumbers))

# Parašykite python programą, kuri paprašytų vartotojo įvesti vardą, pavardę, amžių
# Įrašykite šias reikšmes į dict duomenų struktūrą ir ją išspausdinkite.
data_list = {
    "name": "",
    "lastname": "",
    "age": ""}
input_data_name = str(input("Please enter your name: "))
input_data_lastname = str(input("Please enter your lastname: "))
input_data_age = str(input("Please enter your age: "))
data_list.update({"name": f"{input_data_name}"})
data_list.update({"lastname": f"{input_data_lastname}"})
data_list.update({"age": f"{input_data_age}"})
print(data_list)

# Pabandykite sukurti dict struktūrą, kurioje turite panaudoti visas jums žinomas duomenų struktūras ir tipus.
user_info = {
    "Name": "Mindaugas",
    "Place of birth": "Utena",
    "Has drivers lisence": True,
    "Lived citys": ("Kaunas", "Ukmerge", "Utena"),
    "professions": ["Laisvo oro direktorius", "Veiperis", "Bananas"]}
print(user_info)

# Sukurkite programą, kuri iš sakinių, kuriuos jus įvedėt, sukurtų dict, kuriame keys reikštų raides
# o values šių raidžių dažnumą tuose sakiniuose. Programa turi reikalauti, kad vartotojas įvestų ne mažiau kaip 3 sakinius.

dic_sentence = {}
sentences = [input("Please enter a sentence: ") for _ in range(3)]

for sentence in sentences:
    for count in sentence:
        if count.isalpha():
            count = count.lower()
            dic_sentence[count] = dic_sentence.get(count, 0) + 1
print("Letter frequencies: ")
for letter, freq in dic_sentence.items():
    print(f"{letter} {freq}")

# Sukurkite studentų vardų ir jų pažymėjimų žodyną:
#
# Studentų vardus saugokite kaip raktus, o jų pažymėjimus - kaip reikšmes žodyne.
# Apskaičiuokite visų studentų vidutinį pažymėjimą:
#
# Naudokite sum() ir len() funkcijas apskaičiuoti bendrą ir pažymėjimų skaičių, atitinkamai
# o tada bendrąjį skaičių padalinkite iš skaičiaus, kad gautumėte vidurkį.
# Pašalinti studentus, kuriems pažymėjimai mažesni nei 80, iš žodyno:
#
# Naudokite set, kad sukurtumėte studentų vardų rinkinį, kurių pažymėjimai yra mažesni nei 80.
#
# Pažiūrėti, ar konkretus studentas egzistuoja žodyne:
#
# Įveskite studento vardą iš vartotojo.
# Naudokite in operatorių, norėdami patikrinti, ar studento vardas egzistuoja žodyne.
# Spausdinkite pranešimą, rodantį, ar studento vardas yra rastas, ar ne.


students_bellow_80 = set()
students_average_grade = {}
students = {
    "mindaugas": [8, 9, 10, 10, 9, 10, 10, 9, 10, 8],
    "evelina": [9, 9, 9, 9, 10, 10, 9, 10, 10, 10],
    "tomas": [10, 8, 10, 8, 8, 8, 9, 10, 10, 5],
    "domantas": [8, 10, 2, 5, 7, 10, 9, 10, 10, 8],
    "antanas": [8, 10, 2, 5, 7, 10, 9, 10, 5, 8]
}

# Patikriname ir surandame studentus, kurių bendras pažymių suma mažesnė nei 80
for student, grades in students.items():
    total_grades = sum(grades)
    average = total_grades / len(grades)
    if total_grades < 80:
        students_bellow_80.add(student)
    if average > 8:
        students_average_grade[student] = average

# Ištriname studentus, kurių bendra pažymių suma mažesnė nei 80
for student in students_bellow_80:
    del students[student]

# Patikriname studento informaciją duomenų bazėje
student_check_database = input("Enter a student name: ").lower()
if student_check_database in students:
    print(f"Student {student_check_database} is in the database.")
else:
    print("Student is not in the database")

print("Students with grades above 8:")
print(students_average_grade)

# Leiskite naudotojui įvesti vardą, pavardę ir amžių
# Išspausdinkite, ar naudotojas gali patekti į internetinį kazino, ar ne
# 21 metai yra amžiaus riba.
# Sukurkite duomenų bazę (privilegijuotų naudotojų sąrašas)
# išspausdinkite konkretų pranešimą su asmeniniu pasveikinimu
# jei naudotojas yra privilegijuotas,arba tik "Sveiki atvykę" kitu atveju.


vip_users = {"Tomas", "Tadas", "Martynas", "Antanas"}

name = input("Enter your name: ").capitalize()
lastname = input("Enter your lastname: ")
age = int(input("Enter your age: "))

if age < 21:
    print("You need to be at least 21 years old to enter casino :( ")
elif name in vip_users:
    print(f"Welcome back {name}. Enjoy the finest gambling experience. ")
else:
    print("Welcome back!")

# Leiskite naudotojui įvesti du skaičius. Išspausdinkite, kuris iš jų didesnis už kitą,arba ar jie lygūs.

number1 = input("Please enter a number: ")
number2 = input("Please enter a second number: ")

if number1 == number2:
    print(f"{number1} and {number2} are equal!")
elif number1 < number2:
    print(f"{number1} is greater than {number2}!")
elif number1 > number2:
    print(f"{number1} is less than {number2}!")

# Parašykite nedidelę skaičiuotuvo programą, kuri leistų naudotojui įvesti du skaičius ir simbolį
# ir tada atlikti operaciją bei išspausdinti atsakymą.


import time

print("Welcome to my shitty calculator!")
time.sleep(0.5)
while True:
    number1 = float(input("Please enter first number: "))
    symbol = str(input("Choose a symbol (*) (-) (+) (/) (**): "))
    number2 = float(input("Please enter second number: "))
    if symbol == "*":
        print(f"{number1} * {number2} = {number1 * number2}")
    elif symbol == "-":
        print(f"{number1} - {number2} = {number1 - number2}")
    elif symbol == "*":
        print(f"{number1} + {number2} = {number1 + number2}")
    elif symbol == "*":
        print(f"{number1} / {number2} = {number1 / number2}")
    elif symbol == "**":
        print(f"{number1} / {number2} = {number1 ** number2}")
    break

# Sukurkite skaičių nuo 1 iki 10 spėjimo žaidimą su atsitiktinių skaičių biblioteka

import random
import time

lucky_number = random.randint(1, 100)
print("Welcome to my shitty guessing game!")
time.sleep(0.5)
while True:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess == lucky_number:
        print("you got it right!")
        break
    elif user_guess < lucky_number:
        print("Feels bad man... right number is a bit highier")
    else:
        print("Feels bad man... right number is a bit lower")

# Sukurkite Python list su įvairiausiais tipo objektais. Išspausdinkite visus tipus.

my_list = ["mindaugas", 23, 1.83, ]

print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))

# Sukurkite Python list su įvairiausiais tipo objektais. Išspausdinkite visus tipus.
# Atspausdinkite visus šiuos objektus ir jų tipus , atskirtus "|" simboliu.
my_list = ["mindaugas", 23, 1.83, ]

print(type(my_list[0]))
print(type(my_list[1]))
print(type(my_list[2]))

for item in my_list:
    print(item, end=" | ")

# Sukurkit list su float tipo duomenimis, turinčius 3 skaitmenis po kablelio
# Sukurkite kitą list su visomis reikšmėmis, suapvalintomis iki 2 ženklų po kablelio
# Atspausdinkit abiejus list.

numbers = [5.542, 8.541, 9.542, 2.789, 5.561]
numbers1 = []

for item in numbers:
    roundnumber = round(item, 2)
    numbers1.append(roundnumber)
print(numbers)
print(f"rounded numbers are: {numbers1} ")

# Sukurkite list su mokinių vardais ir juos surūšiuokite, rezultatą išspausdinkite į terminalą.

students = ["Martynas", "Onute", "Petriukas", "Kaziukas", "Briedis", "Albertas", "Stanislovas"]

sorted_students = sorted(students)

print(sorted_students)

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

# Sukurkite kintamuosius, kuriuose reprezentuotų vartotojo vardą ir slaptažodį
# Pradėkite begalinį ciklą, leidžiantį įvesti vartotojo vardą ir slaptažodį
# Jei duomenys teisingi, sustabdykite begalinį ciklą ir išspausdinkite pasisveikinimo pranešimą.


import time

username = "bananas"
password = "makaka"

while True:
    username_input = input("Please enter your username: ")
    time.sleep(0.2)
    password_input = input("Please enter your password: ")
    if username_input != username:
        print("Username not found in the database")
    elif password_input == password:
        print(f"Welcome back {username}")
        break
    else:
        print("Incorrect password")

# Leiskite naudotojui įvesti 10 sveikųjų skaičių
# tada spausdinkite šių įvestų skaičių sumą ir vidurkį.

number_list = []
numbers = [int(input("Please enter a number: ")) for _ in range(10)]
number_list.append(numbers)

for x in number_list:
    number_sum = sum(x)
    print(f"Your total number is: {number_sum}")
    print(f"Your total average is: {number_sum / 10}")

# Sugeneruokite dict iš 10 skaitmenų (keys): 1,2,3...10
# Kiekvienam key turėtų būti priskirta atsitiktinio sveikojo skaičiaus vertė nuo 1 iki 100.

import random

numbers = {
    "1": "",
    "2": "",
    "3": "",
    "4": "",
    "5": "",
    "6": "",
    "7": "",
    "8": "",
    "9": "",
    "10": ""}

for keys in numbers:
    numeriukas = random.randint(1, 100)
    numbers[keys] = numeriukas
print(numbers)

# Sukurkite PIN kodo nulaužimo programą
# Tarkime, PIN kodą sudaro 4 atsitiktiniai skaitmenys.
# Reikšmę galite saugoti kintamajame. Tada sukurkite ciklą, einantį per visas galimas kombinacijas
# kol rasite tą, kurią įvedėte.
import random

pincode = str(random.randint(1, 9999))
correct_pin = pincode.zfill(4)

while True:
    guess = str(random.randint(1, 9999))
    correct_guess = guess.zfill(4)
    if correct_guess == correct_pin:
        print(f"Hacking successful. Pincode is: {correct_pin}")
        break
    else:
        print(f"Trying pincode {correct_guess}...")

user_input = input("Enter number sequence: ")
number_list = [int(digit) for digit in str(user_input)]
average = sum(number_list) / len(number_list)
print(number_list)
print(f"Total average number is {int(average)}")


# Patys sukurkite bent 5 skirtingas funkcijas ir jas išbandykite.

def number_sum(a, b, c):
    return a + b + c


def number_divide(a, b, c):
    return a / b / c


def number_substract(a, b, c):
    return a - b - c


def number_multiply(a, b, c):
    return a * b * c


print(number_sum(5, 8, 9))
print(number_divide(5, 8, 9))
print(number_substract(5, 8, 9))
print(number_multiply(5, 8, 9))


# Sukurkite funkciją, kuri prie kiekvieno list nario prideda string galūnę.
def add_ending_to_list(input_list, ending):
    return [item + ending for item in input_list]


my_list = ["Makaka", "Hakuna", "Matata"]
result = add_ending_to_list(my_list, "_end")
print(result)




# Sukurkite mini python programą, kuri kaip įvestį paimtų du skaičius ir grąžintų jų sumą, atimtį, dalybą, daugybą.
def calculator(a, b, c, operation):
    if operation == "sum":
        return a + b + c
    elif operation == "sub":
        return a - b - c
    elif operation == "mult":
        return a * b * c
    elif operation == "div":
        return a / b / c
    else:
        print("unkown operation :(")


a_number = int(input("Please input a number: "))
b_number = int(input("Please input a number: "))
c_number = int(input("Please input a number: "))
operation_select = input("Please choose a operation (+) (-) (*) (/): ")

if operation_select == "+":
    print(calculator(a_number, b_number, c_number, operation="sum"))
elif operation_select == "-":
    print(calculator(a_number, b_number, c_number, operation="sub"))
elif operation_select == "*":
    print(calculator(a_number, b_number, c_number, operation="mult"))
elif operation_select == "/":
    print(calculator(a_number, b_number, c_number, operation="div"))
