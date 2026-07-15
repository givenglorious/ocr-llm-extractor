from batch import process_loader
from excel import file_to_excel

if __name__ == "__main__":
    folder = "data/"  
    results = process_loader(folder)
    file_to_excel(results)
    
    
    
