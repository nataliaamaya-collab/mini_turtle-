from mini_turtle import adelante, abajo, reiniciar

print("DIBUJANDO ESCALERA 1\n")

escalones = int(input("¿Cuántos escalones? "))
h = int(input("¿Pasos hacia la derecha por escalón? "))
v = int(input("¿Pasos hacia abajo por escalón? "))

for i in range(escalones):
    adelante(h)
    abajo(v)

print("\nReiniciando posición...\n")
reiniciar()

print("DIBUJANDO ESCALERA 2\n")

adelante(5)
abajo(3)
