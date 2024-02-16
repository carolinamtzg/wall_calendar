# Practica "Creación de la Clase Dia y Wall Calendar en Python"

## Clase Dia

**Objetivo:** Desarrollar una clase Dia en Python que represente una fecha, la cual puede ser inicializada con valores por defecto (1 de enero de 1970) o con valores específicos de fecha (año, mes, día) proporcionados por el usuario. _Esta clase debe ser implementada sin utilizar ninguna librería estándar o no estándar de Python, apoyándose únicamente en cálculos numéricos para todas sus operaciones._

**Requisitos de la Clase Dia:**

- Inicialización: La clase debe poder inicializarse tanto con valores por defecto (1 de enero de 1970) como con una fecha específica proporcionada por el usuario. Debe validar que la fecha es correcta, considerando años bisiestos.

- Atributos: La clase tendrá los atributos.

  – dia: dia del mes
  – mes: numero del mes, 1 enero, 12 diciembre
  – anyo: numero del año. Siempre después de cristo (desde el 1 en adelante)
  – dia_semana: numero del dia de la semana siendo 0 el sabado y el 6 el viernes
  representada. (implementar el algoritmo de Zeller)

- Verificación de Fecha Correcta: Incluir lógica para verificar la validez de la fecha, incluyendo la correcta identificación de años bisiestos.

## Clase Wall Calendar

**Objetivo:** Desarrollar una clase en Python llamada WallCalendar que simule un calendario de pared, el cual se puede inicializar con un número específico de años, meses y días. La clase debe ajustar automáticamente los valores de meses y días para conformar una fecha válida, incluyendo la conversión de días excedentes en meses y, si es necesario, la adición de años cuando los meses excedan de 12. Esta clase también debe ser capaz de avanzar día a día y mostrar la fecha actual en formato legible.

**Requisitos de la Clase WallCalendar:**

- Inicialización: La clase debe aceptar tres argumentos en su inicialización: ano, mes, dia. La lógica de inicialización debe ajustar estos valores para formar una fecha válida, teniendo en cuenta:

  - Si el número de meses es mayor a 12, se deben añadir los años necesarios.
  - Los días deben ajustarse según el mes y año correspondiente, transformando cualquier exceso de días en los meses (y años si es necesario) subsiguientes.
  - _Almacenamiento de la Fecha:_ Una vez inicializado, el calendario debe almacenar internamente una fecha válida basada en los cálculos anteriores.
  - _Método para Mostrar la Fecha:_ Implementar un método mostrar_fecha que retorne la fecha actual del calendario en el formato “Día de la semana, día de mes de año” (por ejemplo, “Miércoles, 8 de abril de 1970”).
  - _Método para Avanzar un Día:_ Incluir un método avanza sin argumentos que avance la fecha del calendario en un día. Este método debe ajustar automáticamente el mes y el año si es necesario.
