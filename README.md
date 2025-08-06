# 📦 Sistema de Gestión de Inventario

> Un sistema completo de gestión de inventario desarrollado en Python con enfoque en buenas prácticas de programación y diseño orientado a objetos.

## 🎯 Descripción

Este proyecto es un sistema de gestión de inventario desarrollado como ejercicio práctico para fortalecer habilidades en:
- 🐍 Programación en Python
- 📊 Estructura de datos
- 📁 Manejo de archivos
- 🏗️ Diseño orientado a objetos

El sistema permite gestionar productos de manera eficiente, registrar movimientos de entrada y salida, y mantener un control actualizado del stock en tiempo real.

## ✨ Funcionalidades

### 🛍️ Gestión de Productos
- ➕ **Registro de productos**: Agregar nuevos productos con información completa
- ✏️ **Actualización**: Modificar datos de productos existentes
- 🔍 **Consulta**: Visualizar información detallada de productos
- 🗑️ **Eliminación**: Remover productos del sistema

### 📈 Control de Inventario
- 📥 **Entradas**: Registrar compras, devoluciones y ajustes positivos
- 📤 **Salidas**: Registrar ventas, mermas y ajustes negativos
- 📊 **Estado del stock**: Consulta en tiempo real del inventario
- 🔎 **Búsqueda avanzada**: Por nombre o código de producto

### 💾 Persistencia de Datos
- 📄 Almacenamiento en formato JSON
- 🔄 Conservación de datos entre ejecuciones
- 🚫 Sin dependencias de bases de datos externas

## 🛠️ Tecnologías Utilizadas

| Tecnología | Versión | Propósito |
|------------|---------|-----------|
| 🐍 Python | 3.6+ | Lenguaje principal |
| 📄 JSON | - | Almacenamiento de datos |
| 🎨 POO | - | Paradigma de programación |

## 📋 Requisitos del Sistema

- Python 3.6 o superior
- Permisos de lectura/escritura en el directorio del proyecto

## 🚀 Instalación y Uso

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/tu-usuario/sistema-inventario.git
```

### 2️⃣ Navegar al directorio
```bash
cd sistema-inventario
```

### 3️⃣ Ejecutar el programa
```bash
python main.py
```

### 4️⃣ Usar la interfaz
Sigue las opciones del menú interactivo en la consola para gestionar tu inventario.

> **💡 Nota**: El archivo `inventario.json` se creará automáticamente en la primera ejecución.

## 📁 Estructura del Proyecto

```
sistema-inventario/
│
├── 🐍 main.py                 # Punto de entrada del programa
├── 📦 inventario.py           # Clase principal de gestión
├── 🏷️  producto.py            # Modelo de producto
├── 📊 movimiento.py           # Registro de movimientos
├── 📂 data/
│   └── 📄 inventario.json     # Almacenamiento persistente
├── 📖 README.md               # Documentación del proyecto
└── 📜 LICENSE                 # Licencia del proyecto
```

## 👥 Colaboradores

<table>
  <tr>
    <td align="center">
      <strong>🧑‍💻 JaIro Herrera Romero</strong><br>
      <sub>Estudiante de Ingeniería en TI</sub>
    </td>
    <td align="center">
      <strong>🧑‍💻 Alejandro Bolaños Chinchilla</strong><br>
      <sub>Estudiante de Ingeniería en TI</sub>
    </td>
  </tr>
</table>

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para cambios importantes:

1. 🍴 Haz fork del proyecto
2. 🌿 Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🔄 Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la **Licencia MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

<div align="center">

**⭐ Si este proyecto te fue útil, no olvides darle una estrella ⭐**

**🔗 [Otros proyectos](https://github.com/AlejandroXV5/Practica-Torre-de-Hanoi.git)**

</div>
