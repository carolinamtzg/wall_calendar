# Verificación de Fecha Correcta:
# Incluir lógica para verificar la validez de la fecha
# incluyendo la correcta identificación de años bisiestos.
# Si intentas crear una fecha tal que d = Dia(1970, 4, 31)
# debe lanzar una excepcion de tipo ValueError
# con el mensaje que desees, ya que abril solo tiene 30 días


def es_año_bisiesto(anyo):
	año = anyo
	if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
		return True
	else:
	  False

# Cálculo del Día de la Semana:
# Implementar el algoritmo de Zeller 
# dentro de la clase para determinar el día de la semana de la fecha.
		
def calcular_dia_de_la_semana(anyo, mes, dia):
	if (mes < 3):
		mes += 12
		anyo -= 1
  
	a = anyo % 100
	b = (anyo // 100)
	c =  b // 4 - 2 * b
	d = a // 4
	e = (13 * (mes + 1) // 5)
	f = (a  + c + d + e + dia) % 7
	return f
	
  
def dia_de_la_semana(anyo, mes, dia):
	dia_semana = calcular_dia_de_la_semana(anyo, mes, dia)
	nombre_dia_de_la_semana = ["Sábado", "Domingo", "Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
	return nombre_dia_de_la_semana[dia_semana]

def dias_por_mes(anyo, mes):
    mes_de_30_dias = mes in [4,6,9,11]
    if mes_de_30_dias:
      return 30
    
    es_febrero = mes == 2
    bisiesto = es_año_bisiesto(anyo)
    if es_febrero and bisiesto:
      return 28
    if es_febrero:
      return 28
    return 31

# print(dia_de_la_semana(1988,9,2), "debe ser Viernes")
# print(dia_de_la_semana(1990,9,13), "debe ser Jueves")