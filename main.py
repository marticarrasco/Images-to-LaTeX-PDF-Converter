import os
import subprocess

def create_pdf_with_images_fixed(directory, title="Exercicis sistema dièdric", author="Martí Carrasco", date="Gener 2024"):
    # Prepare LaTeX document content
    latex_document = r'''\documentclass{article}
\usepackage[utf8]{inputenc}
\usepackage{graphicx}
\usepackage{float} % Added for better figure placement
\usepackage{hyperref}

\title{''' + title + r'''}
\author{''' + author + r'''}
\date{''' + date + r'''}

\begin{document}

\maketitle

'''
    # List all images in the directory
    images = [img for img in os.listdir(directory) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    # Display images that will be added
    print("Images to be added:")
    for i, img in enumerate(images, start=1):
        print(f"{i}. {img}")

    # Add images to the LaTeX document
    for i, img in enumerate(images, start=1):
        latex_document += r'\begin{figure}[H]' + '\n' # Changed to [H] to force placement
        latex_document += r'\centering' + '\n'
        latex_document += r'\includegraphics[width=\textwidth]{' + img + '}\n'
        latex_document += r'\end{figure}' + '\n\n'

    # End of the document
    latex_document += r'\end{document}'

    # Write to a .tex file
    tex_file_path = os.path.join(directory, "document.tex")
    with open(tex_file_path, "w", encoding="utf-8") as file:
        file.write(latex_document)

    # Compile the LaTeX document to PDF
    try:
        subprocess.run(["pdflatex", "-output-directory", directory, tex_file_path], check=True)
        print(f"PDF and LaTeX document created successfully in {directory}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the PDF: {e}")

# Get the current directory where the script is located
current_directory = os.getcwd()

# Call the function with the current directory
create_pdf_with_images_fixed(current_directory)
