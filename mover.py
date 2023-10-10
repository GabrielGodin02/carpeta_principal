import os
import shutil

# Ruta de la carpeta principal que contiene carpetas numeradas
carpeta_principal = 'C:/Users/spike/OneDrive/Documentos/carpeta_principal/CARPETASUBCARPETA'

# Ruta de la carpeta con archivos PDF
carpeta_pdf = 'C:/Users/spike/OneDrive/Documentos/carpeta_principal/CARPETAPDF'

# Escanea las subcarpetas numeradas
for subdir, _, _ in os.walk(carpeta_principal):
    # Obtén el número de identificación de la subcarpeta
    numero_identificacion = os.path.basename(subdir)

    # Escanea la carpeta con archivos PDF
    for archivo_pdf in os.listdir(carpeta_pdf):
        # Comprueba si el nombre del archivo PDF contiene el número de identificación
        if numero_identificacion in archivo_pdf:
            # Ruta completa del archivo PDF
            ruta_pdf = os.path.join(carpeta_pdf, archivo_pdf)

            # Ruta completa de la subcarpeta de destino
            carpeta_destino = os.path.join(carpeta_principal, numero_identificacion)

            # Mueve el archivo PDF a la subcarpeta correspondiente
            shutil.move(ruta_pdf, carpeta_destino)
            print(f"Se movió {archivo_pdf} a {carpeta_destino}")
