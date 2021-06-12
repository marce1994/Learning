cadena_ingresada = input("Ingrese la fecha actual en formato dd/mm/yyyy: ");

separado = cadena_ingresada.split('/');

print(separado);

print(
    f'Dia: {separado[0]}', '-',
    f'Mes: {separado[1]}', '-',
    f'Anio: {separado[2]}'
);

c = cadena_ingresada;

print(
    f'Dia: {c[0]}{c[1]}', '-',
    f'Mes: {c[3]}{c[4]}', '-',
    f'Anio: {c[6]}{c[7]}{c[8]}{c[9]}'
);
