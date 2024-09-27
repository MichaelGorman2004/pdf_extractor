import PyPDF2
import os

def extract_pdf_pages(input_path, output_path, start_page, end_page):
    # Ensure the page numbers are valid
    start_page = max(1, start_page)
    end_page = max(start_page, end_page)

    # Open the input PDF
    with open(input_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        # Ensure end_page is not beyond the last page
        end_page = min(end_page, len(reader.pages))
        
        # Create a PDF writer object
        writer = PyPDF2.PdfWriter()
        
        # Add the specified pages to the writer
        for page_num in range(start_page - 1, end_page):
            writer.add_page(reader.pages[page_num])
        
        # Write the output PDF
        with open(output_path, 'wb') as output_file:
            writer.write(output_file)

def main():
    # Get user input
    input_path = input("Enter the path to the input PDF file: ").strip()
    
    # Validate input file
    while not os.path.isfile(input_path):
        print("Invalid file path. Please try again.")
        input_path = input("Enter the path to the input PDF file: ").strip()
    
    output_path = input("Enter the path for the output PDF file: ").strip()
    
    # Get page range
    while True:
        try:
            start_page = int(input("Enter the start page number: "))
            end_page = int(input("Enter the end page number: "))
            if start_page > 0 and end_page >= start_page:
                break
            else:
                print("Invalid page range. Start page must be positive and end page must be greater than or equal to start page.")
        except ValueError:
            print("Please enter valid numbers for page range.")
    
    # Extract pages
    try:
        extract_pdf_pages(input_path, output_path, start_page, end_page)
        print(f"Successfully created {output_path} with pages {start_page} to {end_page}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
