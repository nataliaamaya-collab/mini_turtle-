# 🐢 Mini-Turtle — Ejercicio 1 (Versión Funcional)

Este proyecto implementa una versión modular de un pequeño sistema de dibujo en consola llamado **Mini-Turtle**, basado en funciones que simulan movimientos hacia la derecha y hacia abajo.

El objetivo es demostrar:
- Modularidad
- Separación entre lógica interna y la interfaz pública
- Creación de un paquete Python distribuible (`mini_turtle`)
- Uso de un archivo `pyproject.toml`
- Función adicional `reiniciar()` para resetear la posición

---

## 📦 Estructura del Proyecto

mini_turtle/
│
├── mini_turtle/
│ ├── init.py
│ ├── drawer_logic.py
│
├── main.py

---

## 🧠 ¿Qué hace cada archivo?

### **drawer_logic.py**
Contiene la lógica interna del dibujo:
- `adelante(n)`
- `abajo(n)`
- `reiniciar()`
- variable interna `posicion_x`

### **__init__.py**
Expone la interfaz pública del paquete:
```python
from .drawer_logic import adelante, abajo, reiniciar

main.py

Script de prueba que:

* Importa las funciones del paquete

* Dibuja una escalera

* Usa reiniciar()

* Dibuja otra figura

▶️ Ejemplo de Uso (main.py)
from mini_turtle import adelante, abajo, reiniciar

print("DIBUJO 1\n")
adelante(5)
abajo(3)

reiniciar()

print("\nDIBUJO 2\n")
adelante(2)
abajo(5)

📥 Instalación en modo editable (opcional)



