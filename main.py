def obtener_temperatura(dia):
    input_str = input(f"Ingrese la temperatura en grados Celsius, día {dia}:")
    # Validando que la entrada sea un número
    try:
        temperatura = float(input_str)
        return temperatura
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return None

def calcular_promedio(semana):
    # Calculando el promedio de una lista de números
    if len(semana) == 0:
        return 0
    return sum(semana) / len(semana)

def encontrar_max_min(semana):
    # Encontrando el máximo y mínimo de una lista de números junto con sus índices
    if len(semana) == 0:
        return None, None, None, None
    maximo = max(semana)
    minimo = min(semana)
    indice_maximo = semana.index(maximo)
    indice_minimo = semana.index(minimo)
    return maximo, minimo, indice_maximo, indice_minimo

def encontrar_temperaturas_por_sobre_el_promedio(semana, promedio):
    # Filtrando las temperaturas mayores que el promedio
    return [temp for temp in semana if temp > promedio]

def validar_temperatura_sobre_valor(temperatura, valor):
    # Validando que la temperatura sea mayor que un valor dado
    if temperatura > valor:
        print(f"¡Alerta! La temperatura {temperatura:.2f} grados Celsius supera el valor de {valor:.2f} grados Celsius.")

def validar_temperatura_bajo_valor(temperatura, valor):
    # Validando que la temperatura sea menor que un valor dado
    if temperatura < valor:
        print(f"¡Alerta! La temperatura {temperatura:.2f} grados Celsius está por debajo del valor de {valor:.2f} grados Celsius.")

def nombre_dia_de_la_semana(dia):
    # Asignando un nombre al día de la semana
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    return dias[dia] if 0 <= dia <= 6 else None

def main():
    temperaturas = []
    valor_alerta_maxima = 40.0  # Valor de referencia para la alerta
    valor_alerta_minima = 0.0   # Valor de referencia para la alerta

    for i in range(7):
        while True:
            nombre_dia = nombre_dia_de_la_semana(i)
            temperatura = obtener_temperatura(nombre_dia)
            if temperatura is not None:
                # Validar si la temperatura supera el valor dado
                validar_temperatura_sobre_valor(temperatura, valor_alerta_maxima)
                validar_temperatura_bajo_valor(temperatura, valor_alerta_minima)
                temperaturas.append(temperatura)
                break

    # Calculando el máximo y mínimo de la semana
    maximo, minimo, indice_maximo, indice_minimo = encontrar_max_min(temperaturas)
    nombre_dia_maximo = nombre_dia_de_la_semana(indice_maximo)
    nombre_dia_minimo = nombre_dia_de_la_semana(indice_minimo)
    print(f"La temperatura máxima de la semana es: {maximo:.2f} grados Celsius (día {nombre_dia_maximo})")
    print(f"La temperatura mínima de la semana es: {minimo:.2f} grados Celsius (día {nombre_dia_minimo})")

    # Calculando el promedio de la semana
    promedio = calcular_promedio(temperaturas)
    print(f"La temperatura promedio de la semana es: {promedio:.2f} grados Celsius")

    # Encontrando temperaturas mayores que el promedio
    temperaturas_mayores = encontrar_temperaturas_por_sobre_el_promedio(temperaturas, promedio)
    print(f"Las temperaturas mayores que el promedio son: {temperaturas_mayores}")

main()
