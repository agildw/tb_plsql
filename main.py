from database import create_session
import models
from typing import Union
from fastapi import FastAPI

app = FastAPI()
session = create_session()


@app.get("/")
def read_root():
    return {"message": "This is the root of the API"}

# menampilkan semua data produk
@app.get("/produk")
def read_produk():
    data = session.query(models.Produk).all()
    return data

@app.post('/produk')
def create_produk(plu: int, nama_produk: str, hpp: int, harga_produk: int):
    try:
        # buat pengecekan apakah produk sudah ada


        # add data
        produk = models.Produk(plu=plu, nama_produk=nama_produk, hpp=hpp, harga_produk=harga_produk)
        session.add(produk)
        session.commit()
        return produk
    except Exception as e:
        print(e)
        if 'Duplicate entry' in str(e):
            return {'error': 'PLU sudah ada'}
        else:
            return {'error': str(e)}
    

# menampilkan data promosi
@app.get("/promosi")
def read_promosi():
    data = session.query(models.Promosi).all()
    return data

# menampilkan data produk promosi
@app.get("/produk-promo")
def read_produk_promosi():
    data = session.query(models.Produk_Promo).all()
    return data