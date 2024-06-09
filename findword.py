import PyPDF2
import os


def find_text_in_pdfs(pdf_folder_path, search_text):
    # List all PDF files in the provided folder
    pdf_files = [f for f in os.listdir(pdf_folder_path) if f.endswith('.pdf')]

    found_in_pdfs = []
    not_found_in_pdfs = []

    # Iterate through each PDF file
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder_path, pdf_file)

        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            found = False

            # Search for the text in each page
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()

                if search_text.lower() in text.lower():
                    found = True
                    break

            if found:
                found_in_pdfs.append(pdf_file)
            else:
                not_found_in_pdfs.append(pdf_file)

    # Print the results
    print(f"The word '{search_text}' was found in the following PDFs:")
    for pdf in found_in_pdfs:
        print(f"  - {pdf}")

    print(f"\nThe word '{search_text}' was not found in the following PDFs:")
    for pdf in not_found_in_pdfs:
        print(f"  - {pdf}")


# Provide the folder path containing your PDF files
pdf_folder_path = 'pdf'

# Ask the user for the text to search for
search_text = input("Enter the word you want to search for: ")

find_text_in_pdfs(pdf_folder_path, search_text)
