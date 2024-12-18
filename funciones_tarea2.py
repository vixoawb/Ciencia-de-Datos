def promedio(lista):
    """
  Calcula el promedio de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      float: El promedio de los valores en la lista.
  """
    suma = sum(lista)
    return suma / len(lista)


def mediana(lista):
    """
  Determina la mediana de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      int o float: La mediana de los valores en la lista.
  """
    listOrd = sorted(lista)
    n = len(listOrd)
    mitad = n // 2

    if n % 2 == 0:
        return (listOrd[mitad - 1] + listOrd[mitad]) / 2
    else:
        return listOrd[mitad]


def moda(lista):
    """
  Encuentra los valores más frecuentes (modas) en una lista.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      list: Lista con los valores que tienen mayor frecuencia.
  """
    frecc = {}
    for elem in lista:
        frecc[elem] = frecc.get(elem, 0) + 1

    frecc_max = max(frecc.values())
    return [key for key, value in frecc.items() if value == frecc_max]


def rango(lista):
    """
  Calcula el rango de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      int o float: La diferencia entre el valor máximo y el mínimo.
  """
    return max(lista) - min(lista)


def varianza(lista):
    """
  Calcula la varianza de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      float: La varianza de los datos.
  """
    promValue = promedio(lista)
    return sum((x - promValue) ** 2 for x in lista) / len(lista)


def desviacion_estandar(lista):
    """
  Calcula la desviación estándar de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      float: La desviación estándar de los datos.
  """
    return varianza(lista) ** 0.5


def rango_intercuartilico(lista):
    """
  Calcula el rango intercuartílico de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      float: La diferencia entre el tercer cuartil (Q3) y el primer cuartil (Q1).
  """
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)

    Q1 = mediana(lista_ordenada[:n // 2])
    Q3 = mediana(lista_ordenada[(n + 1) // 2:])
    return Q3 - Q1


def dvmedab(lista):
    """
  Calcula la desviación mediana absoluta de una lista de números.

  Ingresa:
      lista (list): Lista de valores numéricos.

  Retorna:
      float: La desviación mediana absoluta.
  """
    mediana_valor = mediana(lista)
    diferencias = [abs(x - mediana_valor) for x in lista]
    mad = mediana(diferencias)
    return mad


def covarianza(x, y):
    """
  Calcula la covarianza entre dos listas de números.

  Ingresa:
      x (list): Primera lista de valores numéricos.
      y (list): Segunda lista de valores numéricos.

  Retorna:
      float: La covarianza entre las dos listas.
  """
    if len(x) != len(y):
        raise ValueError("Las listas deben tener la misma longitud")
    promX = promedio(x)
    promY = promedio(y)
    return sum((xi - promX) * (yi - promY) for xi, yi in zip(x, y)) / len(x)


def coeficiente_correlacion(x, y):
    """
  Calcula el coeficiente de correlación entre dos listas de números.

  Ingresa:
      x (list): Primera lista de valores numéricos.
      y (list): Segunda lista de valores numéricos.

  Retorna:
      float: El coeficiente de correlación (r) entre las dos listas.
  """
    return covarianza(x, y) / (desviacion_estandar(x) * desviacion_estandar(y))
