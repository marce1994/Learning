def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return value

a = intTryParse(input("Ingrese el primer valor: "));
b = intTryParse(input("Ingrese el segnudo valor: "));

print(type(a), type(b), type(a)==type(b));
