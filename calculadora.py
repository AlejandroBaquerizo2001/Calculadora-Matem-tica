import sympy as sp
import numpy as np
from sympy import symbols, diff, integrate, solve, Eq, limit, sin, cos, tan, exp, log, sqrt

def calcular_derivada():
    x = symbols('x')
    funcion = input("Ingresa la función en términos de x (ej: x**2 + sin(x)): ")
    expr = sp.sympify(funcion)
    derivada = diff(expr, x)
    print(f"La derivada de {funcion} es: {derivada}")

def calcular_integral():
    x = symbols('x')
    funcion = input("Ingresa la función en términos de x (ej: x**2 + 1): ")
    expr = sp.sympify(funcion)
    integral = integrate(expr, x)
    print(f"La integral de {funcion} es: {integral} + C")

def calcular_integral_definida():
    x = symbols('x')
    funcion = input("Ingresa la función en términos de x (ej: x**2): ")
    a = float(input("Límite inferior (a): "))
    b = float(input("Límite superior (b): "))
    expr = sp.sympify(funcion)
    integral = integrate(expr, (x, a, b))
    print(f"La integral definida de {funcion} desde {a} hasta {b} es: {integral}")

def resolver_ecuacion():
    x = symbols('x')
    ecuacion = input("Ingresa la ecuación en términos de x (ej: x**2 - 4 = 0): ")
    expr = sp.sympify(ecuacion.split('=')[0] + '-' + ecuacion.split('=')[1])
    soluciones = solve(expr, x)
    print(f"Las soluciones son: {soluciones}")

def calcular_limite():
    x = symbols('x')
    funcion = input("Ingresa la función en términos de x (ej: sin(x)/x): ")
    punto = input("Ingresa el punto al que tiende x (ej: 0, oo para infinito): ")
    if punto == 'oo':
        punto = sp.oo
    else:
        punto = float(punto)
    expr = sp.sympify(funcion)
    lim = limit(expr, x, punto)
    print(f"El límite de {funcion} cuando x tiende a {punto} es: {lim}")

def evaluar_funcion():
    x = symbols('x')
    funcion = input("Ingresa la función en términos de x (ej: x**2 + 3*x + 2): ")
    valor = float(input("Ingresa el valor de x para evaluar: "))
    expr = sp.sympify(funcion)
    resultado = expr.subs(x, valor)
    print(f"f({valor}) = {resultado}")

def menu():
    print("\n--- CALCULADORA MATEMÁTICA ---")
    print("1. Calcular derivada")
    print("2. Calcular integral indefinida")
    print("3. Calcular integral definida")
    print("4. Resolver ecuación")
    print("5. Calcular límite")
    print("6. Evaluar función en un punto")
    print("7. Salir")

def main():
    while True:
        menu()
        opcion = input("\nSelecciona una opción (1-7): ")
        
        if opcion == '1':
            calcular_derivada()
        elif opcion == '2':
            calcular_integral()
        elif opcion == '3':
            calcular_integral_definida()
        elif opcion == '4':
            resolver_ecuacion()
        elif opcion == '5':
            calcular_limite()
        elif opcion == '6':
            evaluar_funcion()
        elif opcion == '7':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()