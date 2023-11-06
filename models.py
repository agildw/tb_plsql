from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from database import engine

Base = declarative_base()

class Produk(Base):
    __tablename__ = 'Produk'

    plu = Column(Integer, primary_key=True)
    nama_produk = Column(String(50))
    hpp = Column(Integer)
    harga_produk = Column(Integer)

class Promosi(Base):
    __tablename__ = 'Promosi'

    kode_promo = Column(String(7), primary_key=True)
    nama_promo = Column(String(50))
    potongan = Column(Float(4, 4))

class Produk_Promo(Base):
    __tablename__ = 'Produk_Promo'

    plu = Column(Integer, ForeignKey('Produk.plu'), primary_key=True)
    kode_promo = Column(String(7), ForeignKey('Promosi.kode_promo'), primary_key=True)

Base.metadata.create_all(engine)