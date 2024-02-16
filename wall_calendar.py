# Desarrollar una clase en Python llamada WallCalendar que simule un calendario de pared
# el cual se puede inicializar con un número específico de años, meses y días.
from controls import es_año_bisiesto, dia_de_la_semana, dias_por_mes

class WallCalendar():
  def __init__(self, anno, mes, dia):
    self.validar_anno(anno) # validar año

    self.anno = anno
    self.mes = mes
    self.dia = dia

  def nombre_mes(self, mes):
    meses = ["enero", "febrero", "marzo", "abril",
            "mayo", "junio", "julio", "agosto",
            "septiembre", "octubre", "noviembre", "diciembre"]

    return meses[mes - 1]
  
  def ajusta_fecha(self, anno, mes, dia):
    while mes >= 12:
      anno += 1 # incrementa año
      mes -= 12 # mes pasa a ser 1
      
    while dia > dias_por_mes(anno, mes):
      dia -= dias_por_mes(anno, mes) # resta el dia de los dias x mes que hay en el mes del año
      mes += 1 # incrementa el mes
      if mes > 12: # si el mes es > 12
        anno += 1 # incrementar el año
        mes -= 12 # restar 12 meses para resetear los meses el siguiente año

    return f"{dia} de {self.nombre_mes(mes)} de {anno:04d}"
      
  def dia_de_la_semana(self, anno, mes, dia):
    return dia_de_la_semana(anno, mes, dia)
  
  #verificar si el año es desde 1 en adelante:
  def validar_anno(self, anno):
    if anno <= 1:
      raise ValueError("El año debe ser mayor o igual de 1")
  
# Una vez inicializado
# el calendario debe almacenar internamente una fecha válida basada en los cálculos anteriores.
  def mostrar_fecha(self):
    nueva_fecha = self.ajusta_fecha(self.anno, self.mes, self.dia)
    dia_de_la_semana = self.dia_de_la_semana(self.anno, self.mes, self.dia)

    return f"{dia_de_la_semana}, {nueva_fecha}"
  
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


fecha = WallCalendar(2024, 2, 15)
print(fecha.mostrar_fecha())
fecha.avanzar_un_dia()
print(fecha.mostrar_fecha())

# 1970, 3, 39 -> tendría que ser 1970,4,8