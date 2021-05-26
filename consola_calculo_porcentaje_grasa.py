import calculadora_indices as calc
peso=float(input("Ingrese el peso de la persona en kilogramos:"))
altura=float(input("Ingrese la altura de la persona en metros:"))
edad=int(input("Ingrese la edad de la persona: "))
v_genero=float(input("Ingrese el 10.8 si el genero es masculino o de lo contrario cero:"))

print(str(calc.calcular_porcentaje_grasa(peso,altura,edad,v_genero))+"%")