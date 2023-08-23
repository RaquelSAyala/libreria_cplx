# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
import math

def suma_cplx(c1, c2):
    #suma de numeros complejos
    parteR = c1[0] + c2[0]
    parteI = c1[1] + c2[1]
    return (parteR, parteI)

def resta_cplx(c1, c2):
    parteR = c1[0] - c2[0]
    parteI = c1[1] - c2[1]
    return (parteR, parteI)

def mult_cplx(c1, c2):
    parteR = c1[0] * c2[0] - c1[1] * c2[1]
    parteI = c1[0] * c2[1] + c1[1] * c2[0]
    return (parteR, parteI)

def div_cplx(c1, c2):
    denom = c2[0]**2 + c2[1]**2
    c2_conjugate = (c2[0], -c2[1])
    num = mult_cplx(c1, c2_conjugate)
    parteR = num[0] / denom
    parteI = num[1] / denom
    return (parteR, parteI)

def modulo_cplx(c):
    return math.sqrt(c[0]**2 + c[1]**2)

def conjugado_cplx(c):
    return (c[0], -c[1])

def polar_a_cart(polar):
    r, theta = polar
    parteR = r * math.cos(theta)
    parteI = r * math.sin(theta)
    return (parteR, parteI)

def cart_a_polar(cartesian):
    parteR, parteI = cartesian
    r = modulo_cplx(cartesian)
    theta = math.atan2(parteI, parteR)
    return (r, theta)

def fase_cplx(c):
    return math.atan2(c[1], c[0])

