# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

vegetables = ["rucula", "tomate", "lechuga", "acelga"];

print(vegetables);
print(len(vegetables));
print(str(type(vegetables)));

print('-'*10);

print(vegetables[0]); # Elemento 0
print(vegetables[1:]) # Primer elemento en adelante
print(vegetables[2:]) # Segundo elemento en adelante
print(vegetables[0:10000]) # Python es magico y anda
print(vegetables[:]) # Copia todos los elementos en memoria ponele
print(vegetables[1:3][::-1]) # Invierte la lista

print('-'*10);

vegetables.append("berenjena") # Agrega a la lista
other_vegetables = ["brocoli", "coliflor", "lechuga"];

print(vegetables + other_vegetables);

vegetables.extend(other_vegetables);

print(vegetables);

print('-'*10);

a = [*vegetables, *other_vegetables];
print(a);

b = [vegetables, other_vegetables];
print(b);

c = ["d", *vegetables[1:3], "f", *other_vegetables]
print(c);

print('-'*10);
for vegetable in vegetables:
    print(vegetable);
    
print('-'*10);
print(vegetables.pop());
print(vegetables.pop());
print(vegetables.pop());
print(vegetables.pop(0));
print(vegetables);

vegetables.remove("acelga");

print(vegetables);

print('-'*10);

new_list = vegetables; # Referencia
vegetables.append("acelga");

print(vegetables == new_list, vegetables, new_list)
print(id(vegetables), id(new_list));


new_list = vegetables[:]; # Copia
new_list.pop();

print(vegetables == new_list, vegetables, new_list)
print(id(vegetables), id(new_list));

# Otras formas copia lista
# new_list = vegetables.copy();
# new_list = list(vegetables);
# new_list = [+vegetables];
