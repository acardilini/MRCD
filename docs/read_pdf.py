import PyPDF2
import sys

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for i in range(len(reader.pages)):
                text += reader.pages[i].extract_text()
            print("Successfully extracted text. Length:", len(text))
            
            # Find references to Figure 1
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if 'Figure 1' in line or 'Fig. 1' in line or 'Fig 1' in line:
                    print(f"Match found at line {i}:")
                    print('\n'.join(lines[max(0, i-5):min(len(lines), i+6)]))
                    print("-" * 40)
                    
    except Exception as e:
        print("Error reading PDF:", e)

if __name__ == "__main__":
    read_pdf("Rothgerber 2020 Meat Related Cognitive Dissonance.pdf")
