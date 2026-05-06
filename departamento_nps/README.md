# Departamento NPS

## Descripción

Este módulo corresponde al departamento de NPS, encargado de procesar y analizar datos de encuestas para evaluar el nivel de satisfacción de los usuarios.

## Estructura del proyecto

departamento_nps/
├── datos/
├── env_nps/
├── notebooks/
├── src/
├── .gitignore
├── README.md
├── script_prueba.py
└── requirements.txt

## Requisitos

- Python 3.x instalado  
- Gestor de paquetes pip  

## Instalación del entorno

1. Clonar el repositorio o hacer pull de los cambios.

2. Crear entorno virtual:

    python -m venv env_nps

3. Activar entorno:

    env_nps\Scripts\activate

4. Instalar dependencias:

    pip install -r requirements.txt

## Ejecución

Para validar que el entorno funciona correctamente:

python script_prueba.py

## Script de validación

El archivo `script_prueba.py` permite verificar:
    - correcta instalación de librerías  
    - funcionamiento de pandas, numpy y matplotlib  
    - generación de resultados en consola y gráfica  

## Dependencias principales

pandas==3.0.2
numpy==2.4.4
matplotlib==3.10.9

Las demás dependencias se instalan automáticamente.

## Flujo de trabajo del entorno

### Antes de hacer push

1. Crear y activar el entorno virtual  
2. Verificar versiones de Python y librerías  
3. Instalar dependencias necesarias  
4. Ejecutar script de validación  
5. Ajustar el entorno (actualizar, limpiar dependencias, resolver errores)  
6. Generar archivo requirements.txt  
7. Subir cambios al repositorio  

### Después de hacer pull

1. Actualizar repositorio  
2. Identificar archivo de dependencias del departamento  
3. Crear entorno virtual  
4. Instalar dependencias desde requirements.txt  
5. Ejecutar script de validación  
6. Resolver conflictos si existen  

## Notas para el equipo

- Cada departamento utiliza su propio entorno virtual  
- No modificar el archivo requirements.txt sin coordinación  
- No subir la carpeta del entorno (env_nps/) al repositorio  
- Mantener nombres de entornos únicos  

## Consideraciones técnicas

El uso de entornos virtuales permite aislar las dependencias del proyecto, evitando conflictos entre módulos y garantizando la reproducibilidad del entorno en diferentes equipos.

El archivo requirements.txt documenta las dependencias principales del proyecto y permite reconstruir el entorno automáticamente.

## Autor

Eunice
