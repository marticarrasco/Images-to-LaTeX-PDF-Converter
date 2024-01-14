
# LaTeX Image to PDF Converter

This Python script automates the creation of a PDF document from images located in a specified directory, utilizing LaTeX for document formatting. It's particularly useful for compiling visual materials such as diagrams, figures, or photographs into a single, professionally formatted document.

## Features

- **Automatic Image Compilation:** Converts all images in the specified directory (supports PNG, JPG, JPEG, GIF, BMP) into a PDF document.
- **Customizable Document Settings:** Allows setting the title, author, and date of the PDF document.
- **Improved Figure Placement:** Integrates the LaTeX `float` package for better image placement within the document.
- **Error Handling:** Provides feedback in case of errors during PDF creation.

## Prerequisites

To use this script, ensure you have the following installed:
- Python 3.x
- LaTeX distribution (e.g., TeX Live, MiKTeX) with `pdflatex` command available.

## Installation

1. Clone or download this repository to your local machine.
2. Ensure you have the necessary prerequisites installed.

## Usage

1. Place the Python script in the directory containing the images you wish to compile.
2. Open a terminal in the same directory.
3. Run the script using Python:
   
   ```bash
   main.py
   ```

4. The script will automatically create a LaTeX file and compile it into a PDF with the images from the directory.

## Customization

You can customize the title, author, and date of the document by modifying the `create_pdf_with_images_fixed` function parameters:
- `directory`: Path to the directory containing the images.
- `title`: Title of the PDF document.
- `author`: Author name.
- `date`: Date of the document.

For example:

```python
create_pdf_with_images_fixed(directory="/path/to/images", title="My Image Collection", author="Your Name", date="January 2024")
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)
