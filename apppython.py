import tkinter as tk
from tkinter import filedialog
import os
import shutil

def seleccionar_carpeta_subcarpetas():
    carpeta_subcarpetas = filedialog.askdirectory()
    entrada_carpeta_subcarpetas.delete(0, tk.END)
    entrada_carpeta_subcarpetas.insert(0, carpeta_subcarpetas)

def seleccionar_carpeta_pdf():
    carpeta_pdf = filedialog.askdirectory()
    entrada_carpeta_pdf.delete(0, tk.END)
    entrada_carpeta_pdf.insert(0, carpeta_pdf)

def organizar_archivos():
    carpeta_subcarpetas = entrada_carpeta_subcarpetas.get()
    carpeta_pdf = entrada_carpeta_pdf.get()

    for subdir, _, _ in os.walk(carpeta_subcarpetas):
        numero_identificacion = os.path.basename(subdir)
        
        for archivo_pdf in os.listdir(carpeta_pdf):
            if numero_identificacion in archivo_pdf:
                ruta_pdf = os.path.join(carpeta_pdf, archivo_pdf)
                carpeta_destino = os.path.join(carpeta_subcarpetas, numero_identificacion)
                
                # Asegurarse de que la carpeta de destino exista, si no, crearla
                if not os.path.exists(carpeta_destino):
                    os.makedirs(carpeta_destino)

                shutil.move(ruta_pdf, carpeta_destino)
                print(f"Se movió {archivo_pdf} a {carpeta_destino}")

# Crear una ventana
ventana = tk.Tk()
ventana.title("Seleccionar Carpetas")

# Etiqueta y entrada para la carpeta con subcarpetas
etiqueta_carpeta_subcarpetas = tk.Label(ventana, text="Carpeta con subcarpetas:")
etiqueta_carpeta_subcarpetas.pack()
entrada_carpeta_subcarpetas = tk.Entry(ventana)
entrada_carpeta_subcarpetas.pack()
boton_seleccionar_carpeta_subcarpetas = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta_subcarpetas)
boton_seleccionar_carpeta_subcarpetas.pack()

# Etiqueta y entrada para la carpeta con archivos PDF
etiqueta_carpeta_pdf = tk.Label(ventana, text="Carpeta con archivos PDF:")
etiqueta_carpeta_pdf.pack()
entrada_carpeta_pdf = tk.Entry(ventana)
entrada_carpeta_pdf.pack()
boton_seleccionar_carpeta_pdf = tk.Button(ventana, text="Seleccionar Carpeta", command=seleccionar_carpeta_pdf)
boton_seleccionar_carpeta_pdf.pack()

# Botón para organizar archivos
boton_organizar = tk.Button(ventana, text="Organizar Archivos", command=organizar_archivos)
boton_organizar.pack()

# Ejecutar la aplicación
ventana.mainloop()


