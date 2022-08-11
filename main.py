"""
Crear una aplicación de línea de comandos que permita 
1. registro
2. búsqueda
3. edición
4. eliminación
de artículos dentro de un sistema de inventario."""

import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://toni:1234@cluster0.wi9ojnj.mongodb.net/?retryWrites=true&w=majority")


db = cluster["InventarySystem"]
collection = db["articles"]


#AddingArticles-------------------------------------------------------------------

#ENTRADA = CÓDIGO PRODUCTO,	DESCRIPCIÓN,	ENTRADAS,	SALIDAS,	STOCK
#TOTAL

entrada00 = {"Codigo_de_producto":1, "Descripcion":"Espárragos", "Entradas":19, "Salidas":28,	"Stock":76}
entrada01 = {"Codigo_de_producto"2, "Descripcion":"Alcachofas", "Entradas":31,	"Salidas":39,	"Stock":72}
entrada02 = {"Codigo_de_producto":3, "Descripcion":"Pimientos del piquillo", "Entradas":16, "Salidas":14,	"Stock":57}
entrada03 = {"Codigo_de_producto":4, "Descripcion":"Tomates", "Entradas":9, "Salidas":12, "Stock":37}
entrada04 = {"Codigo_de_producto":5, "Descripcion":"Guisantes", "Entradas":11, "Salidas":6, "Stock":25}
entrada05 = {"Codigo_de_producto":6, "Descripcion":"Judías", "Entradas":7, "Salidas":6, "Stock":21}

collection_insert_many(entrada00, entrada01, entrada02, entrada03, entrada04, entrada05)


#Functions-----------------------------------------------------------------------

def add(In):
  r = collection.insert_one(In)
  print(r)
  return r

def find(In):
  r = collection.find_one("Codigo_de_producto":In)
  print(r)

def delete(In):
  r = collection.delete_one(In)
  return r


#MainApp--------------------------------------------------------------------------
print("INVENTARIO MENSUAL DE PRODUCTOS")
do{
  print("""
  ________________________MENU________________________
          1. Registrar nuevo articulo
          2. Buscar un articulo
          3. Editar un articulo
          4. Eliminar un articulo
  """)
  i = input("Elegir una de las 4 opciones 1, 2, 3 o 4:")
  
  if i==1:
    print("Registrar nuevo articulo")
    cdp = input("Codigo del producto: ")
    dscr = input("Descripcion del producto: ")
    entr = input("Entradas mensuales del producto: ")
    slds = input("Salidas mensuales del producto: ")
    stck = input("Stock actual del producto: ")

    entrada = {"Codigo_de_producto":cdp,
               "Descripcion":dscr, 
               "Entradas":entr, 
               "Salidas":slds, 
               "Stock":stck}

    add(entrada)

  if i==2:
    print("Buscar un articulo")
    articulo = input("Ingresar codigo del producto: ")
    
    find(articulo)

  if i==3:
    print("Editar un articulo")
    cdp = input("Actualizar codigo del producto: ")
    dscr = input("Actualizar descripcion del producto: ")
    entr = input("Actualizar entrada mensual del producto: ")
    slds = input("Actualizar salida mensual del producto: ")
    stck = input("Actualizar stock actual del producto: ")
    r = collection.update_one{"Codigo_de_producto":cdp,
                              "Descripcion":dscr, 
                              "Entradas":entr, 
                              "Salidas":slds, 
                              "Stock":stck}
    
  if i==4:
    print("Eliminar un articulo")
    codigo = input("Codigo de producto a eliminar: ")
    articulo = {"Codigo_de_producto":codigo}
    delete(articulo)
}while(i>0)
