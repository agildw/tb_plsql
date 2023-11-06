from database import create_session
import models

def main():
    session =create_session()
    data = session.query(models.Produk).all()
    for item in data:
        print(item.plu, item.nama_produk, item.hpp, item.harga_produk)

    # insert data
    produk = models.Produk(plu=123, nama_produk='Buku', hpp=10000, harga_produk=20000)
    session.add(produk)
    session.commit()

if __name__ == '__main__':
    main()