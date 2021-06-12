precioBase = 100;
precioPorKm = 0.30;

destinosKm = {
    "Destino1": 300,
    "Destino3": 750,
    "Destino2": 1600,
    "Destino4": 900,
    "Destino5": 100
}

print(destinosKm.keys());

a = input("Ingrese destino: ");

print(f"Calculando boleto a destino {a}");
print("Pecio del boleto: ", precioBase + precioPorKm * destinosKm[a]);
