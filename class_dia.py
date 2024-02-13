# Desarrollar una clase Dia() en Python que represente una fecha
# la cual puede ser inicializada con valores por defecto (1 de enero de 1970)

from controls import dia_de_la_semana, es_año_bisiesto

class Dia():
  def __init__(self, anyo=1970, mes=1, dia=1):
    # validar año, dia:
    self.validar_anyo(anyo) # anyo desde el 1 en adelante
    self.validar_mes(mes) # validar mes
    self.validar_dia_del_mes(anyo,mes,dia) # validar meses y años bisiestos

    # numero del dia de la semana siendo 0 el sabado y el 6 el viernes:
    self.dia_de_la_semana = dia_de_la_semana(anyo,mes,dia)

    self.numero_del_anyo = anyo 
    self.numero_del_mes = mes
    self.dia_mes = dia
  
  def info(self):
    return f"{self.dia_de_la_semana}, {self.dia_mes} de {self.nombre_mes(self.numero_del_mes)} de {self.numero_del_anyo:04d}"
  
  def nombre_mes(self, numero_del_mes):
    meses = ["enero", "febrero", "marzo", "abril",
            "mayo", "junio", "julio", "agosto",
            "septiembre", "octubre", "noviembre", "diciembre"]
    return meses[numero_del_mes - 1]
    
  #verificar si el año es desde 1 en adelante:
  def validar_anyo(self, anyo):
    valido = anyo >= 1
    if not valido:
      raise ValueError("El año debe ser mayor o igual de 1")
    
  #validar mes:
  def validar_mes(self, mes):
    if mes < 1 or mes > 12:
      raise ValueError("Número de mes no válido")

  # verificar dias y si es año bisiesto cant dias:
  def validar_dia_del_mes(self, anyo, mes, dia):
    # Meses que tienen 30 dias: abril, junio, septiembre y noviembre.
    mes_de_30_dias = mes in [4,6,9,11]
    numero_de_dias_valido = dia >= 1 and dia <= 30
    if mes_de_30_dias and numero_de_dias_valido:
      return dia
    if mes_de_30_dias and not numero_de_dias_valido:
      raise ValueError(f"{self.nombre_mes(mes)} tiene 30 días.")

    # si es febrero y año bisiesto:
    es_febrero = mes == 2
    bisiesto = es_año_bisiesto(anyo)
    numero_dias_febrero_bisiesto_valido = dia >= 1 and dia <= 29
    if es_febrero and bisiesto and numero_dias_febrero_bisiesto_valido:
      return dia
    if es_febrero and bisiesto and not numero_dias_febrero_bisiesto_valido:
      raise ValueError(f"{self.nombre_mes(mes)} tiene 29 días.")
    
    # febrero y no es año bisiesto:
    numero_dias_febrero_valido = dia >= 1 and dia <= 28
    if es_febrero and numero_dias_febrero_valido:
      return dia
    if es_febrero and not numero_dias_febrero_valido:
      raise ValueError(f"{self.nombre_mes(mes)} solo tiene 28 días.")

    # mes con 31 dias:
    if dia >= 1 and dia <= 31:
      return dia
    
    raise ValueError(f"{self.nombre_mes(mes)} tiene 31 días.")

  def dia_de_la_semana(self, numero_del_anyo, numero_del_mes, dia_mes):
    return dia_de_la_semana(numero_del_anyo, numero_del_mes, dia_mes)
  

# Test:
d = Dia(2024,1,1)

print(d.info())


