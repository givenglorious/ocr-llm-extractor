import os 
from main import process_receipt_file

def process_loader(folder_path:str) -> list:
    results = []
    for filename in os.listdir(folder_path):
        if not filename.lower().endswith(('.jpg', '.jpeg', '.png','pdf')):
            continue
        file_path = os.path.join(folder_path, filename)
        try:
            data = process_receipt_file(file_path)
            results.append(data)
            print(f'OK {filename}')
        except Exception as e:    
            print(f"NO {filename}")
    return results
               
               
if __name__ == "__main__":
   hasil =  process_loader('data/')
   print(f"Berhasil ke akses {len(hasil)} ")
  
    