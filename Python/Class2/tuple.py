fruit = "banana";
# fruit[2] = "7"; No puedo hacer esto, es inmutable

fruits = ("banana", "tomate", "anana");
# fruit[0] = "lechuga"; Tampoco puedo hacer esto

print(type(fruits),fruits);

fruits = list(fruits);

print(type(fruits), fruits);

fruits = tuple(fruits);
print(type(fruits), fruits);

fruits = str(list(fruits));
print(type(fruits), fruits);

# fruits = tuple(fruits);
# print(type(fruits), fruits); # Boom :
