import zipfile
import os

def agregar_archivo_al_zip(zipf, archivo, relpath):
    """Agrega un archivo a un archivo ZIP conservando la estructura de carpetas."""
    zipf.write(archivo, relpath)

def comprimir_carpeta():
    carpeta_seleccionada = input("Ingrese la ruta de la carpeta que desea comprimir: ")
    if not os.path.exists(carpeta_seleccionada):
        print("La carpeta ingresada no existe.")
        return
    
    nombre_archivo = 'carpeta_comprimida.zip'
    with zipfile.ZipFile(nombre_archivo, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for foldername, subfolders, filenames in os.walk(carpeta_seleccionada):
            for filename in filenames:
                archivo = os.path.join(foldername, filename)
                relpath = os.path.relpath(archivo, carpeta_seleccionada)
                agregar_archivo_al_zip(zipf, archivo, relpath)
    
    # Calcular el tamaño original y el tamaño del archivo comprimido
    tamano_original = sum(os.path.getsize(os.path.join(root, file)) for root, dirs, files in os.walk(carpeta_seleccionada) for file in files) / (1024 * 1024)  # MB
    tamano_comprimido = os.path.getsize(nombre_archivo) / (1024 * 1024)  # MB
    
    print(f'Tamaño original: {tamano_original:.2f} MB')
    print(f'Tamaño comprimido: {tamano_comprimido:.2f} MB')

comprimir_carpeta()
