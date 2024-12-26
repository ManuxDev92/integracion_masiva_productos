import pandas as pd
import shutil
import os

# Rutas de las carpetas y archivos
ruta_excel = "rutal del archivo excel con el nombre de las imagenes"
ruta_imagenes = "rutal de las imagenes"
ruta_productos = "ruta a donde se moveran las imagenes segun su SKU"

# Leemos el archivo Excel
df = pd.read_excel(ruta_excel)

# Recorremos cada fila del DataFrame
for index, row in df.iterrows():
    nombre_imagen = f"{row['Nombre de la imagen']}.png"  # Agregamos el formato .png
    sku = row['SKU']
    
    # Caminamos por las subcarpetas dentro de la carpeta de imágenes
    for root, dirs, files in os.walk(ruta_imagenes):
        for file in files:
            if file == nombre_imagen:
                ruta_origen = os.path.join(root, file)
                ruta_destino = os.path.join(ruta_productos, str(sku), file)
                os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
                shutil.move(ruta_origen, ruta_destino)
                print(f"Movida: {ruta_origen} -> {ruta_destino}")
