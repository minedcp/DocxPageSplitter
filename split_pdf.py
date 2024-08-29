import os
from PyPDF2 import PdfReader, PdfWriter

def split_pdf(input_pdf_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Open the input PDF file
    reader = PdfReader(input_pdf_path)
    
    # Iterate over each page and save it as a new PDF
    for i in range(len(reader.pages)):
        writer = PdfWriter()
        writer.add_page(reader.pages[i])
        
        # Define the output path for each page
        output_pdf_path = os.path.join(output_folder, f"page_{i+1}.pdf")
        
        # Write the single page to a new PDF file
        with open(output_pdf_path, "wb") as output_pdf:
            writer.write(output_pdf)
        
        print(f"Page {i+1} saved as {output_pdf_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python split_pdf.py <input_pdf_path> <output_folder>")
    else:
        input_pdf_path = sys.argv[1]
        output_folder = sys.argv[2]
        split_pdf(input_pdf_path, output_folder)
        print(f"PDF has been split into individual pages in {output_folder}")
