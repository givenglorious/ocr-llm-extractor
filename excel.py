import pandas as pd

def file_to_excel(results: list, output_path: str = "hasil_ekstraksi.xlsx"):
    rows = []
    for shop in results:
        for item in shop.daftar_menu:
            rows.append({
                "toko": shop.nama_toko,
                "tanggal": shop.tanggal,
                "nama_barang": item.name,
                "harga_satuan": item.price,
                "jumlah": item.quantity,
                "subtotal": item.price * item.quantity,
                "kategori": item.kategori,
            })

    df = pd.DataFrame(rows)
    
    df.to_excel(output_path)
    print(f"Done {output_path}")
    
    
   

from batch import process_loader
if __name__ == "__main__" :
    file = 'data/'
    processing = process_loader(file)
    file_to_excel(processing)