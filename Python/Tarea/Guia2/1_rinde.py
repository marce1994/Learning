parcelas = [
    (10,10),
    (15,20)
];

a = int(input("Ingrese el largo de la tercer parcela: "));
b = int(input("Ingrese el ancho de la tercer parcela: "));

parcelas.append((a,b));

print("#"*55);

total_m2 = sum(map(lambda x: x[0] * x[1], parcelas));

print(
    f"Se cuenta con {len(parcelas)} parcelas,",
    f"por un total de {total_m2}m2."
);

print("#"*55);

rinde_por_m2_siembra = [2,3,1];

print(
    "#Primera siembra:", rinde_por_m2_siembra[0] * total_m2,
    "#Segunda siembra", rinde_por_m2_siembra[1] * total_m2,
    "#Tercera siembra", rinde_por_m2_siembra[2] * total_m2
);
