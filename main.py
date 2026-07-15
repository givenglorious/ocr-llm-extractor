
from pipeline import extract_food_shop
from loader import DataLoader  
from schemas import FoodShop 
from pydantic import BaseModel

def process_receipt_file(file_path: str) -> FoodShop:
    loader = DataLoader(file_path)
    receipt_text = loader.file_format()
    food_shop_data = extract_food_shop(receipt_text)
    return food_shop_data

def print_food_shop_data(food_shop: FoodShop):
    print(f"Nama Toko: {food_shop.nama_toko}\n")
    print(f"No Telepon: {food_shop.no_telepon}\n")
    print(f"Tanggal: {food_shop.tanggal}\n")
    print(f"Jam: {food_shop.jam}\n")
    print("Daftar Menu:")
    for item in food_shop.daftar_menu:
        print(f"  - {item.name}: {item.quantity} x {item.price} = Rp.{item.quantity * item.price:,.2f}",end="\n")
        
if __name__ == "__main__":
    file_path = "data/sbtd2.jpeg",  
    food_shop_data = process_receipt_file(file_path)
    print_food_shop_data(food_shop_data)