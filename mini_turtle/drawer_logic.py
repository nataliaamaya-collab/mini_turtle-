# mini_turtle/drawer_logic.py

posicion_x = 0  # Variable global usada por las funciones

def adelante(n):
    global posicion_x
    print(" " * posicion_x + "-" * n + ">")
    posicion_x += n

def abajo(n):
    global posicion_x
    for _ in range(n - 1):
        print(" " * posicion_x + "|")
    print(" " * posicion_x + "v")

def reiniciar():
    """Reinicia la posición horizontal a 0."""
    global posicion_x
    posicion_x = 0
