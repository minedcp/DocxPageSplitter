
# PDF Page Splitter

## Description
**PDF Page Splitter** is a Python script designed to split a multi-page PDF into individual PDF files, each containing a single page. This tool is perfect for anyone looking to break down a large PDF document into separate, manageable files.

## Features
- Automatically splits each page of a PDF into a new PDF file.
- Saves each page as a separate PDF in the specified output directory.
- Simple and easy to use with minimal setup.

## Requirements
- Python 3.x
- `PyPDF2` library

## Installation
To use this script, you'll need to have Python installed. Additionally, you'll need to install the `PyPDF2` library:

```bash
pip install PyPDF2
```

## Usage
1. Clone or download this repository.
2. Open a terminal and navigate to the project directory.
3. Run the script with your PDF file as input and specify an output directory:

   ```bash
   python split_pdf.py <input_pdf_path> <output_folder>
   ```

   Replace `<input_pdf_path>` with the path to your multi-page PDF file, and `<output_folder>` with the path to the directory where you want the split pages to be saved.

## Example
If you have a PDF named `document.pdf` with 10 pages, you can split it like this:

```bash
python split_pdf.py document.pdf split_pages
```

This will create a folder named `split_pages` containing 10 separate PDF files:

```
split_pages/
├── page_1.pdf
├── page_2.pdf
├── page_3.pdf
...
└── page_10.pdf
```

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to fork the project and submit pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
