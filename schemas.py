from pydantic import BaseModel , Field
from typing import Optional
from datetime import date

class FoodItem(BaseModel):
    name: str
    price: int
    quantity: int
    kategori: str 

class FoodShop(BaseModel):
    nama_toko: Optional[str] = None
    nama_pelanggan: Optional[str] = None
    deskripsi: Optional[str] = None
    no_telepon: Optional[str] = None
    tanggal: date
    jam: Optional[str] = None 
    biaya_admin: Optional[int] = None
    daftar_menu: list[FoodItem] 
    
external_data = { 
        "nama_toko": "PT. Memex",
        "nama_pelanggan": "John Doe",
        "no_telepon": "08123456789",
        "tanggal": "2019-06-01",
        "jam": "10:30",
        "daftar_menu": [
            FoodItem(name="Ayam Geprek", price=50000, quantity=2,kategori="Makanan"),
            FoodItem(name="Nasi Goreng", price=30000, quantity=1,kategori = "Makanan"),
            FoodItem(name="Nasi Goreng Spesial", price=190000, quantity=1,kategori = "Makanan")
        ]
        
    }
user = FoodShop(**external_data)
print(user.daftar_menu)  

  