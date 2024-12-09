import fitz  # PyMuPDF
import os

# Function to convert a PDF to images in png format
def pdf_to_png(pdf_path, output_dir, zoom=4.0):
    abs_pdf_path = os.path.abspath(pdf_path)    
    pdf_document = fitz.open(abs_pdf_path)
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    png_output_dir = os.path.join(output_dir, pdf_name)
    os.makedirs(png_output_dir, exist_ok=True)
    
    # Set zoom factor for better quality (approx. 300 DPI)
    matrix = fitz.Matrix(zoom, zoom)
    
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        pix = page.get_pixmap(matrix=matrix)  # Apply the zoom factor for higher resolution
        output_image_path = os.path.join(png_output_dir, f"{pdf_name}_page_{page_num + 1}.png")
        pix.save(output_image_path)
    
    print(f"PDF {pdf_name} converted to images and saved in image docs dir")
    
# Function to convert a directory of PDFs to images in png format
def pdf_dir_to_png(pdf_dir, output_dir, zoom=4.0):
    for pdf_name in os.listdir(pdf_dir):
        pdf_path = os.path.join(pdf_dir, pdf_name)
        if pdf_name.lower().endswith('.pdf'):
            pdf_to_png(pdf_path, output_dir, zoom)


