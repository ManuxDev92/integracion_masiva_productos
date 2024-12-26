import os
import pandas as pd

# Cargar el archivo Excel
file_path = 'ruta del archivo'
product_data = pd.read_excel(file_path)

# Ruta donde deseas crear las carpetas
output_folder = 'ruta de la carpeta'

# Crear cada carpeta con el SKU correspondiente
for sku in product_data['SKU']:
    folder_path = os.path.join(output_folder, str(sku))
    os.makedirs(folder_path, exist_ok=True)

print("Carpetas creadas exitosamente.")