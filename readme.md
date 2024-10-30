# Organizador Académico

## 📚 Descripción del Proyecto

Este proyecto es un **Trabajo Integrador** cuyo objetivo es desarrollar un sistema de **Organizador Académico**, que permite gestionar de manera eficiente la información relacionada con alumnos, materias y profesores de una institución educativa. Este sistema fue creado para optimizar la gestión de estudiantes, asignaturas y notas, evitando los errores y retrasos comunes que se generan al manejar esta información de manera manual.

El sistema ofrece una interfaz interactiva para registrar estudiantes, asignarles materias, agregar notas y calcular promedios. Además, cuenta con funcionalidades avanzadas, como herencia para diferentes tipos de estudiantes, encapsulamiento para proteger datos sensibles, y polimorfismo para ajustar el cálculo de promedios de alumnos becados.

## 🛠️ Tecnologías Utilizadas
- **Lenguaje**: Python 3
- **Paradigmas**: (POO)

## ✨ Características del Sistema

### 1. 🏗️ Estructura Básica
- **Clases Principales**: `Alumno`, `Materia`, `Profesor`.
- **Atributos de Alumno**: Nombre, Apellido, DNI , lista de Materias.
- **Atributos de Materia**: Nombre, lista de Notas.
- **Atributos de Profesor**: Nombre, Apellido, lista de Materias asignadas.

### 2. 👨‍🎓 Tipos de Alumnos
- **Alumno Regular**: No recibe beneficios adicionales en el cálculo de su promedio.
- **Alumno Becado**: Su promedio se ajusta con un incremento del 10%.

### 3. ⚙️ Funcionalidades
- **Agregar Alumnos**: Registra alumnos regulares o becados, permitiendo definir si reciben beca.
- **Asignar Materias**: Permite asignar materias a los alumnos.
- **Agregar Notas**: Permite agregar notas a cada materia del alumno.
- **Cálculo de Promedios**: Calcula los promedios de las notas de cada materia para cada alumno. Para los alumnos becados, aplica un incremento adicional(10%).
- **Agregar Profesores y Asignar Materias**: Registra profesores y asigna materias específicas a cada uno.


## 🚀 Instrucciones de Uso
1. **Ejecutar el archivo `tp_integrador.py`** para iniciar el sistema.
2. **Seleccionar una opción del menú interactivo** para agregar alumnos, materias, notas, profesores, o mostrar información.
3. **Seguir las indicaciones en pantalla** para ingresar la información requerida.

## 💡 Comentarios y Buenas Prácticas
- Se han agregado comentarios en el código, facilitando su comprensión y mantenimiento.
- Se han utilizado conceptos de Programación Orientada a Objetos (POO) como herencia, encapsulamiento y polimorfismo para mejorar la organización y la reutilización del código.

## 📞 Contacto
Para más información sobre este proyecto, puedes contactar en LinkedIn: [Fernando Carballo](https://www.linkedin.com/in/fercarballo/).

