import os
from openpyxl import Workbook

# Ruta de la carpeta que contiene las imágenes
directorio_imagenes = 'ruta de la carpeta'

# Crear un nuevo libro de Excel
libro = Workbook()
hoja = libro.active
hoja.title = "Listado de Imágenes"

# Buscar imágenes en la carpeta y subcarpetas
imagenes = []
for root, _, files in os.walk(directorio_imagenes):
    for file in files:
        if file.endswith('.png'):
            # Agregar el nombre sin la extensión
            imagenes.append(os.path.splitext(file)[0])

# Agregar los nombres de las imágenes al archivo Excel
for i, nombre in enumerate(imagenes, start=1):
    hoja.cell(row=i, column=1, value=nombre)

# Guardar el archivo Excel en la misma ruta
ruta_excel = os.path.join(directorio_imagenes, 'listado_imagenes_faltantes.xlsx')
libro.save(ruta_excel)

print(f"El archivo Excel se ha guardado en: {ruta_excel}")
