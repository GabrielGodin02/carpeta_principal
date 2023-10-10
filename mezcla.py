import PySimpleGUI as sg
import os
import fitz  # Importa la biblioteca PyMuPDF (Fitz)

def extract_doc_number(pdf_document):
    try:
        # Extrae el número de identificación del metadato del PDF
        doc_number = pdf_document.metadata['author']
        return doc_number
    except Exception as e:
        return None

def merge_pdfs(pdf_folder1, pdf_folder2, output_folder):
    # Obtener la lista de archivos PDF de ambas carpetas
    pdf_files1 = [f for f in os.listdir(pdf_folder1) if f.endswith('.pdf')]
    pdf_files2 = [f for f in os.listdir(pdf_folder2) if f.endswith('.pdf')]

    # Crear un diccionario para organizar los PDF por número de documento
    pdf_dict = {}

    # Procesar archivos de la primera carpeta
    for pdf_file in pdf_files1:
        try:
            pdf_document = fitz.open(os.path.join(pdf_folder1, pdf_file))
            doc_number = extract_doc_number(pdf_document)
            if doc_number:
                if doc_number not in pdf_dict:
                    pdf_dict[doc_number] = []
                pdf_dict[doc_number].append(pdf_document)
        except Exception as e:
            print(f"Error al procesar {pdf_file}: {str(e)}")

    # Procesar archivos de la segunda carpeta
    for pdf_file in pdf_files2:
        try:
            pdf_document = fitz.open(os.path.join(pdf_folder2, pdf_file))
            doc_number = extract_doc_number(pdf_document)
            if doc_number:
                if doc_number not in pdf_dict:
                    pdf_dict[doc_number] = []
                pdf_dict[doc_number].append(pdf_document)
        except Exception as e:
            print(f"Error al procesar {pdf_file}: {str(e)}")

    # Mezclar los PDFs según el número de documento y guardarlos
    for doc_number, pdf_documents in pdf_dict.items():
        output_file = os.path.join(output_folder, f"{doc_number}.pdf")
        output_document = fitz.open()  # Crea un nuevo documento para la mezcla
        for pdf_document in pdf_documents:
            output_document.insert_pdf(pdf_document)
        output_document.save(output_file)
        output_document.close()

# Diseño de la interfaz gráfica
layout = [
    [sg.Text('Seleccione la carpeta 1 de PDFs:'), sg.InputText(key='folder1'), sg.FolderBrowse()],
    [sg.Text('Seleccione la carpeta 2 de PDFs:'), sg.InputText(key='folder2'), sg.FolderBrowse()],
    [sg.Text('Carpeta de salida:'), sg.InputText(key='output_folder', size=(40, 1)), sg.FolderBrowse()],
    [sg.Button('Mezclar PDFs'), sg.Button('Salir')]
]

window = sg.Window('Mezclador de PDFs por número de documento', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Salir':
        break
    elif event == 'Mezclar PDFs':
        folder1 = values['folder1']
        folder2 = values['folder2']
        output_folder = values['output_folder']

        if not folder1 or not folder2 or not output_folder:
            sg.popup('Por favor, seleccione las carpetas y la carpeta de salida.')
        else:
            merge_pdfs(folder1, folder2, output_folder)
            sg.popup('PDFs mezclados exitosamente. Verifique la carpeta de salida.')

window.close()




