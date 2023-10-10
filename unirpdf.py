import fitz
import os
import tkinter as tk
from tkinter import filedialog

# Función para combinar los archivos PDF
def combinar_pdf():
    # Abre un cuadro de diálogo para que el usuario seleccione la carpeta de entrada
    directorio_pdf = filedialog.askdirectory()

    if not directorio_pdf:
        return

    # Nombre del archivo PDF de salida combinado
    archivo_salida = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if not archivo_salida:
        return

    # Lista para almacenar los nombres de archivo de entrada
    archivos_pdf = []

    # Recorre el directorio y obtiene los nombres de archivo PDF
    for filename in os.listdir(directorio_pdf):
        if filename.endswith(".pdf"):
            archivos_pdf.append(os.path.join(directorio_pdf, filename))

    # Ordena los archivos por nombre (puedes cambiar el orden según tus necesidades)
    archivos_pdf.sort()

    # Crea un objeto PDF
    pdf = fitz.open()

    # Combina los archivos PDF en uno solo
    for archivo in archivos_pdf:
        pdf_documento = fitz.open(archivo)
        pdf.insert_pdf(pdf_documento)

    # Guarda el archivo combinado en el archivo de salida
    pdf.save(archivo_salida)
    pdf.close()

    print(f"Se han combinado {len(archivos_pdf)} archivos PDF en '{archivo_salida}'")

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Combinar PDFs")

# Crear un botón para iniciar la combinación de PDFs
boton_combinar = tk.Button(root, text="Combinar PDFs", command=combinar_pdf)
boton_combinar.pack(pady=20)

root.mainloop()
