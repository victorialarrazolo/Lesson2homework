#Victoria Larrazolo lesson 2 hands on 

#part one
day="26"
month="September"
year="2002"
my_birthday= str.format("My birthday is {} {} , {}" , month, day, year)
print(my_birthday)

#part two
first="Happy"
second="Birthday"
third="To"
fourth="You"
final= first + " " + second + " " + third + " " + fourth
print(final.upper())

#part three
age= 15
if age<10:
    print("Not permitted")
elif age<15:
    print("Permitted with a parent")
elif age<18:
    print("Permitted with anyone over 18")
else:
    print("Permitted to attend alone")
    

