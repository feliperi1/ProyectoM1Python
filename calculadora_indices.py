#Funcion para calcular el IMC
def calcular_IMC(peso:float,altura:float)->float:
    calculos=peso/(altura**2)
    return calculos

def calcular_porcentaje_grasa(peso:float,altura:float,edad:int,valor_genero:float)->float:
    calculos=1.2*calcular_IMC(peso,altura)+0.23*edad-5.4-valor_genero
    return calculos

def calcular_calorias_en_reposo(peso:float,altura:float,edad:int,valor_genero:float)->float:
    calculos=(10*peso)+(6.25*altura)-(5*edad)+valor_genero
    return calculos

def calcular_calorias_en_actividad(peso:float,altura:float,edad:int,valor_genero:float,valor_actividad:float)->float:
    calculos=calcular_calorias_en_reposo(peso,altura,edad,valor_genero)*valor_actividad
    return calculos

def consumo_calorias_recomendado_para_adelgazar(peso:float,altura:float,edad:int,valor_genero:float)->str:
    limite_inferior=calcular_calorias_en_reposo(peso,altura,edad,valor_genero)*0.8
    limite_superior=calcular_calorias_en_reposo(peso,altura,edad,valor_genero)*0.85
    return "Para adelgazar es recomendado que consumas entre: "+str(limite_inferior)+" y "+str(round(limite_superior,2))+" calorias al dia"

