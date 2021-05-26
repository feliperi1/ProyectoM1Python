import calculadora_indices as calc
peso=float(input("Ingrese el peso de la persona en kilogramos:"))
altura=float(input("Ingrese la altura de la persona en centimetros:"))
edad=int(input("Ingrese la edad de la persona:"))
v_genero=int(input("Ingrese 5 si el genero es masculino o de lo contrario ingrese -161:"))
v_actividad=float(input("Ingrese 1.2 si hace poco o ningun ejercicio a la semana, 1.375 si hace ejercicio 1 a 3 dias a la semana, 1.55 si hace ejercicio 3 a 5 dias a la semana, 1.725 si hace ejercicio 6 a 7 dias a la semana o 1.9 si hace ejercicio mañanas y tardes todos los dias a las semanas:"))

print(str(calc.calcular_calorias_en_actividad(peso,altura,edad,v_genero,v_actividad))+" cal")
