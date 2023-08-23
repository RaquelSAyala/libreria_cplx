# Librería de Operaciones con Números Complejos

Este proyecto proporciona una librería de funciones para realizar operaciones con números complejos en Python. Las funciones se implementan utilizando tuplas para representar números complejos, y se evita el uso del tipo de datos de números complejos incorporado de Python.

## Funciones

- `suma_cplx(c1, c2)`: Realiza la suma de dos números complejos.
- `resta_cplx(c1, c2)`: Realiza la resta entre dos números complejos.
- `mult_cplx(c1, c2)`: Realiza la multiplicación de dos números complejos.
- `div_cplx(c1, c2)`: Realiza la división de dos números complejos.
- `modulo_cplx(c)`: Calcula el módulo de un número complejo.
- `conjugado_cplx(c)`: Calcula el conjugado de un número complejo.
- `polar_a_cart(polar)`: Convierte una representación polar a una representación cartesiana.
- `cart_a_polar(cartesian)`: Convierte una representación cartesiana a una representación polar.
- `fase_cplx(c)`: Calcula la fase de un número complejo.

## Uso

Puedes utilizar estas funciones para realizar operaciones con números complejos en tu código. Aquí tienes un ejemplo de cómo podrías usarlas:

```python
import math
from complex_operations import *

complejo1 = (3, 2)
complejo2 = (-5, 5.2)

resultado_suma = suma_cplx(complejo1, complejo2)
resultado_resta = resta_cplx(complejo1, complejo2)
resultado_mult = mult_cplx(complejo1, complejo2)
resultado_div = div_cplx(complejo1, complejo2)
modulo = modulo_cplx(complejo1)
conjugado = conjugado_cplx(complejo1)
polar = (5, math.pi/4)  # Radio y ángulo en radianes
resultado_polar_a_cart = polar_a_cart(polar)
cartesiano = (3, 4)
resultado_cart_a_polar = cart_a_polar(cartesiano)
fase = fase_cplx(complejo1)

print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_mult)
print("División:", resultado_div)
print("Módulo:", modulo)
print("Conjugado:", conjugado)
print("Polar a Cartesiano:", resultado_polar_a_cart)
print("Cartesiano a Polar:", resultado_cart_a_polar)
print("Fase:", fase)
