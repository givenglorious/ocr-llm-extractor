import pymupdf
import pytesseract
from  PIL import Image


class DataLoader: #Pascal Code
    def __init__(self,path:str):
        self.path = path    
  
    def file_format(self) -> str:
        if self.path.lower().endswith('.pdf'):
            return self.extract_pdf()
        elif self.path.lower().endswith(('.jpg', '.jpeg', '.png')):
            return self.extract_image()
        else:
            raise ValueError("Unsupported file format. Please provide a PDF or image file.")
        
    def extract_pdf(self) -> str:
        doc = pymupdf.open(self.path)
        text = "\n".join(page.get_text() for page in doc)
        doc.close()
        return text
    
    def extract_image(self) -> str: 
        img = Image.open(self.path) 
        return pytesseract.image_to_string(img) 
    