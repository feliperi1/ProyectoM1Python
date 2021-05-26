import calculadora_indices as calc
peso=float(input("Ingrese el peso de la persona en kilogramos:"))
altura=float(input("Ingrese la altura de la persona en centimetros:"))
edad=int(input("Ingrese la edad de la persona:"))
v_genero=int(input("Ingrese 5 si el genero es masculino o de lo contrario ingrese -161:"))

print(str(calc.calcular_calorias_en_reposo(peso,altura,edad,v_genero))+" cal")