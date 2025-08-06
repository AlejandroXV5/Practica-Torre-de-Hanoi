# 🗼 Torres de Hanói con Inteligencia Artificial

> Implementación gráfica del clásico juego Torres de Hanói con sistema de IA para demostración automática y múltiples niveles de dificultad.

## 🎯 Descripción

Este proyecto implementa una versión gráfica e interactiva del famoso juego **Torres de Hanói**, desarrollado como práctica académica para aplicar conceptos de:

- 🤖 **Inteligencia Artificial** - Algoritmos de resolución automática
- 🎮 **Programación de Juegos** - Interfaz gráfica interactiva
- 🏗️ **Estructuras de Control** - Manejo de flujo de programa
- 📊 **Estructuras de Datos** - Implementación eficiente de algoritmos

## 🎮 Características del Juego

### 🎲 Modalidades de Juego
- **👤 Modo Jugador**: Resuelve el rompecabezas manualmente
- **🤖 Modo Demostración**: Observa cómo la IA resuelve el juego automáticamente

### 🎚️ Niveles de Dificultad
| Nivel | Discos | Dificultad | Movimientos Mínimos |
|-------|--------|------------|-------------------|
| 🟢 Fácil | 3 discos | Principiante | 7 movimientos |
| 🟡 Medio | 6 discos | Intermedio | 63 movimientos |
| 🔴 Difícil | 8 discos | Avanzado | 255 movimientos |

### 🧠 Sistema de IA Inteligente
- **Múltiples estrategias**: La IA utiliza diferentes rutas de solución
- **Rotación de algoritmos**: Cada demostración muestra una estrategia diferente
- **Contador de rutas**: Indica qué estrategia se está ejecutando
- **Optimización progresiva**: Desde la solución más eficiente hasta la más compleja

## 📋 Reglas del Juego

El objetivo es mover todos los discos de la varilla inicial a otra varilla siguiendo estas reglas:

1. 🔄 **Solo un disco por vez**: Únicamente puedes mover un disco en cada jugada
2. 📏 **Orden de tamaño**: Un disco grande nunca puede ir sobre uno más pequeño
3. 🔝 **Solo el disco superior**: Solo puedes tomar el disco que está en la parte superior de cada varilla

## 🎛️ Controles

### 👤 Modo Jugador
- 🖱️ **Mouse**: Interacción completa con los discos (clic y arrastrar)
- ⌨️ **Teclado**: No se utiliza en modo jugador

### 🤖 Modo Demostración
- ⏸️ **Enter o Escape**: Cancelar demostración y volver al menú principal
- ✅ **Confirmación**: El sistema pedirá confirmación antes de salir

## 🚀 Instalación y Uso

### Prerrequisitos
- Python 3.6 o superior
- Bibliotecas gráficas (especificadas en requirements.txt)

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/AlejandroXV5/Practica-Torre-de-Hanoi.git
```

### 2️⃣ Navegar al directorio
```bash
cd Practica-Torre-de-Hanoi
```

### 3️⃣ Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4️⃣ Ejecutar el juego
```bash
python main.py
```

## 📊 Funcionalidades

### 🎯 Sistema de Puntuación
- ⏱️ **Tiempo de juego**: Cronómetro automático
- 🔢 **Contador de movimientos**: Seguimiento de cada jugada
- 📈 **Estadísticas finales**: Resumen al completar el juego

### 🎨 Interfaz Gráfica
- 🖼️ **Visualización clara**: Discos y varillas fáciles de identificar
- 🎭 **Animaciones suaves**: Movimientos fluidos de los discos
- 🎨 **Diseño intuitivo**: Interfaz amigable para el usuario

### 🤖 Algoritmos de IA
- 📚 **Múltiples estrategias**: Diferentes enfoques de resolución
- 🔄 **Rotación automática**: Cambia de estrategia en cada demostración
- 📊 **Optimización**: Desde soluciones óptimas hasta alternativas creativas

## 🏗️ Arquitectura del Proyecto

```
Practica-Torre-de-Hanoi/
│
├── 🐍 main.py                 # Punto de entrada principal
├── 🎮 game.py                 # Lógica principal del juego
├── 🤖 ai_solver.py            # Algoritmos de inteligencia artificial
├── 🎨 gui.py                  # Interfaz gráfica de usuario
├── 📊 game_state.py           # Manejo del estado del juego
├── 🗼 tower.py                # Clase de las torres/varillas
├── 💿 disk.py                 # Clase de los discos
├── 📋 menu.py                 # Sistema de menús
├── 📂 assets/                 # Recursos gráficos
│   ├── 🖼️ images/
│   └── 🔊 sounds/
├── 📖 docs/                   # Documentación del proyecto
├── 🧪 tests/                  # Pruebas unitarias
├── 📄 requirements.txt        # Dependencias del proyecto
└── 📖 README.md
```

## 👥 Equipo de Desarrollo

<table>
  <tr>
    <td align="center">
      <strong>🧑‍💻 JaIro Herrera Romero</strong><br>
      <sub>Estudiante de Ingeniería en TI</sub><br>
      <sub>Desarrollo de IA y Algoritmos</sub>
    </td>
    <td align="center">
      <strong>🧑‍💻 Alejandro Bolaños Chinchilla</strong><br>
      <sub>Estudiante de Ingeniería en TI</sub><br>
      <sub>Interfaz Gráfica y UX</sub>
    </td>
  </tr>
</table>

## 🎓 Contexto Académico

Este proyecto fue desarrollado como parte del curso de **Programación con Inteligencia Artificial**, con los siguientes objetivos académicos:

- ✅ Aplicación de algoritmos de IA para resolución de problemas
- ✅ Implementación de interfaces gráficas interactivas
- ✅ Manejo de estructuras de datos complejas
- ✅ Desarrollo de sistemas con múltiples modalidades de uso
- ✅ Práctica de versionado con Git y documentación técnica

## 📚 Referencias Técnicas

- 🔗 [Algoritmo Clásico de Torres de Hanói](https://es.wikipedia.org/wiki/Torres_de_Han%C3%B3i)
- 🔗 [Introducción a IA](http://dmi.uib.es/~abasolo/intart/1-introduccion.html#1.2)
- 🔗 [Visualización del Problema](https://cdn.kastatic.org/ka-cs-algorithms/hanoi-5-init.png)

## 🤝 Contribuciones

Este es un proyecto académico, pero las sugerencias y mejoras son bienvenidas:

1. 🍴 Fork del repositorio
2. 🌿 Crear rama para nueva característica
3. 💾 Commit de cambios
4. 📤 Push a la rama
5. 🔄 Crear Pull Request

## 📄 Licencia

Proyecto desarrollado con fines académicos bajo supervisión universitaria.

---

<div align="center">

**🎮 ¡Disfruta resolviendo las Torres de Hanói! 🗼**

**⭐ Si te gustó el proyecto, no olvides darle una estrella ⭐**

[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge&logo=github)](https://github.com/AlejandroXV5/Practica-Torre-de-Hanoi.git)

</div>
