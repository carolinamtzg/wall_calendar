# Desarrollar una clase en Python llamada WallCalendar que simule un calendario de pared
# el cual se puede inicializar con un número específico de años, meses y días.
from controls import es_año_bisiesto, dia_de_la_semana

class WallCalendar():
  def __init__(self, anno, mes, dia):
    # validar que cada valor es correcto:
    self.validar_anno(anno) # validar año
    self.validar_mes(mes) # validar mes
    self.validar_dia_del_mes(anno,mes,dia) # validar mes

    self.anno = anno
    self.mes = mes
    self.dia = dia

  def nombre_mes(self, mes):
    meses = ["enero", "febrero", "marzo", "abril",
            "mayo", "junio", "julio", "agosto",
            "septiembre", "octubre", "noviembre", "diciembre"]

    return meses[mes - 1]
  
  def validar_dia_del_mes(self, anno, mes, dia):
    # Meses que tienen 30 dias: abril, junio, septiembre y noviembre.
    mes_de_30_dias = mes in [4,6,9,11]
    numero_de_dias_valido = dia >= 1 and dia <= 30
    if mes_de_30_dias and numero_de_dias_valido:
      return dia
    if mes_de_30_dias and not numero_de_dias_valido:
      raise ValueError(f"{self.nombre_mes(mes)} tiene 30 días.")

    # si es febrero y año bisiesto:
    es_febrero = mes == 2
    bisiesto = es_año_bisiesto(anno)
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
    else:
      # mes con 31 dias:
      if dia >= 1 and 31:
        return dia
      else:
        raise ValueError(f"{self.nombre_mes(mes)} tiene 31 días.")
      
  def dia_de_la_semana(self, anno, mes, dia):
    return dia_de_la_semana(anno, mes, dia)
  
  #verificar si el año es desde 1 en adelante:
  def validar_anno(self, anno):
    if anno <= 1:
      raise ValueError("El año debe ser mayor o igual de 1")
    
  #validar mes:
  def validar_mes(self, mes):
    if mes < 1 or mes > 12:
      raise ValueError("Número de mes no válido")
  
# Una vez inicializado
# el calendario debe almacenar internamente una fecha válida basada en los cálculos anteriores.
  def mostrar_fecha(self):
    return f"{dia_de_la_semana(self.anno, self.mes, self.dia)}, {self.dia} de {self.nombre_mes(self.mes)} de {self.anno:04d}"
  
  # avance la fecha del calendario en un día.
  # Este método debe ajustar automáticamente el mes y el año si es necesario.
  def avanzar_un_dia(self):
    # es este el ultimo dia del mes? 
    # si lo es, incremento el mes y el dia pasa a ser 1
    self.dia += 1
    if self.dia > 30:
      self.dia = 1
      self.mes += 1

    # Si es febrero y bisiesto:
    if self.mes == 2 and es_año_bisiesto(self.anno):
      if self.dia > 29:
        self.dia = 1
        self.mes += 1

    # si es feb y NO es bisiesto:
      elif self.mes == 2 and not es_año_bisiesto(self.anno):
        if self.dia > 28:
          self.dia = 1
          self.mes += 1

    # mes con 31 dias:
    if self.dia > 31:
      self.dia = 1
      self.mes += 1

    # es este el ultimo mes del año?
    # si lo es, incremento el año, y mes y dia pasan a ser 1
    if self.mes > 12:
      self.mes = 1
      self.anno += 1


fecha = WallCalendar(2024,2,13)
print(fecha.mostrar_fecha())
fecha.avanzar_un_dia()
print(fecha.mostrar_fecha())