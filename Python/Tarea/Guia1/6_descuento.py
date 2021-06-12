descuento = 35;
precio = float(input("Ingrese precio medicamento: "));

print(
    "Precio",f'${precio}',
    "Descuento",f'${precio*(descuento/100)}',
    "Total",f'${precio*((100-descuento)/100)}'
);
