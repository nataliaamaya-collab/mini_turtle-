# 🐢 Mini-Turtle — Versión Funcional(modularidad)

Este proyecto implementa una versión modular de un pequeño sistema de dibujo  llamado **Mini-Turtle**, basado en funciones que simulan movimientos hacia la derecha y hacia abajo.

El objetivo es demostrar:

✅ 1. Modularidad
Que el  código esté ordenado y separado en partes, no todo mezclado en un solo archivo.
Como tener:
* una parte que hace la lógica,
* otra parte que muestra lo que el usuario puede usar.
  
✅ 2. Separación entre lógica interna y la interfaz pública.

Que lo que está dentro del paquete (tu código) esté bien organizado, y que el usuario solo vea lo que  quieres que use.

✅ 3. Crear un paquete Python (mini_turtle).

Significa que el código debe estar organizado como una carpeta especial, para que Python pueda importarla.

✅ 4. Archivo pyproject.toml
Este archivo sirve para que Python entienda cómo está organizado tu paquete.

Es como una cédula del proyecto:
* nombre
* versión
* quién lo hizo
* qué archivos incluye

✅ 5. Función adicional `reiniciar()` 

para resetear la posición
Solo hay  que agregar una función que vuelva la posición a 0.
Como cuando se reinicia  un juego y el personaje vuelve al inicio.

## 📦 Estructura del Proyecto

mini_turtle/
│
├── mini_turtle/
│ ├── init.py
│ ├── drawer_logic.py
│
├── main.py

🧠 Descripción del Paquete

Este paquete incluye:

adelante(n) → Dibuja una línea horizontal hacia la derecha

abajo(n) → Desciende verticalmente

reiniciar() → Regresa la posición horizontal a 0

Todas estas funciones se importan directamente desde mini_turtle gracias al archivo __init__.py, que define la interfaz pública del módulo.

Las tres funciones se importan directamente desde el paquete:
---

```python
from mini_turtle import adelante, abajo, reiniciar
```

## 🧠 ¿Qué hace cada archivo?

### **drawer_logic.py**
Contiene la lógica interna del dibujo:
- `adelante(n)`
- `abajo(n)`
- `reiniciar()`
- variable interna `posicion_x
  

### **__init__.py**
Expone la interfaz pública del paquete:
```python
from .drawer_logic import adelante, abajo, reiniciar
```

### **main.py**
Script de prueba que:

* Importa las funciones del paquete

* Dibuja una escalera

* Usa reiniciar()

* Dibuja otra figura

**codigo del proyecto**

```python
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
```

<img width="619" height="579" alt="Captura de pantalla 2025-12-09 214335" src="https://github.com/user-attachments/assets/bc70fc3e-a419-4aeb-bc17-1aba294b7eb8" />


  
📝### **Contenido del Repositorio**

Este repositorio incluye:

* El paquete mini_turtle

* Las funciones implementadas en programación funcional

* Un archivo main.py para probar el paquete

* Este archivo README.md explicativo


