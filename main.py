import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://toni:1234@cluster0.wi9ojnj.mongodb.net/?retryWrites=true&w=majority")


db = cluster["FirstMongoDBApp"]
collection = db["Diccionario"]

#Añadiendo vocabulario--------------------------------------------
post1 = {"word":"Abuelazón", "meaning":"Dícese de la conducta de entusiasmo excesivo que los abuelos sienten por los nietos; actitud típica de personas ancianas."}
post2 = {"word":"Ahuevado", "meaning":"sinónimo de huevón, lento, imbécil"}
post3 = {"word":"Arrabalero/a", "meaning":"Buscapleitos"}
post4 = {"word":"Arranque", "meaning":"de arrancarse [irse de fiesta/a parrandear]"}
post5 = {"word":"Ayala", "meaning":"interjección de sorpresa o enojo. "}
post6 = {"word":"Cabreado(a)", "meaning":"Que esta molesto(a)."}
post7 = {"word":"Cafá", "meaning":"Una Palmada fuerte átras en la cabeza."}
post8 = {"word":"Carretilla", "meaning":"Que va muy rapído e.j. A carretilla, como una carretilla..."}
post9 = {"word":"Camarón", "meaning":"actividad extracurricular que permite a un individuo ganar dinero extra."}
post10 = {"word":"Chantin", "meaning":"casa, hogar."}
post11 = {"word":"Cholywood", "meaning":"farándula panameña."}
post12 = {"word":"Datien", "meaning":"  "}
post13 = {"word":"De a vaina", "meaning":"ganar algo por pura buena suerte en el ultimo momento."}
post14 = {"word":"En bomba", "meaning":"objeto atractivo (no se usa con personas), bueno, excelente"}
post15 = {"word":"Frenteao", "meaning":"Decir directamente a uno, en la cara"}
post16 = {"word":"Fulo(a)", "meaning":"Rubio/a."}
post17 = {"word":"Fundillo", "meaning":"especificamente el orificio anal."}
post18 = {"word":"Fuas", "meaning":"Nalgas, Trasero."}
post19 = {"word":"Fuste", "meaning":"Sinonimo de fuas."}
post20 = {"word":"Gallinero", "meaning":" la entreda general o area popular de algun evento cultural (concierto) o evento deportivo."}
post21 = {"word":"Grubeo/ar", "meaning":"Estar con una persona por un tiempo o por una noche para pasarla bien y para nada serio o formal."}
post22 = {"word":"Guagua", "meaning":"se dice de un automóvil muy viejo o en mal estado."}
post23 = {"word":"Yeyé", "meaning":"Persona adinerada que presume de su condición y/o comúnmente usa anglicismos en su habla."}
post24 = {"word":"Zambito(a)", "meaning":"expresión de las provincias de Herrera y Los Santos, significa niño o niña."}

collection_insert_many(post1, post2, post3, post4, post5,
                      post6, post7, post8, post9, post10,
                      post11, post12, post13, post14, post15,
                      post16, post17, post18, post19, post20,
                      post21, post22, post23, post24)

#Funciones--------------------------------------------------------

def add_word(In):
  result= collection.insert_one(In)
  print(result)
  return result

def change_word(In, In1)
  result = collection.update_one{"word":In}, { $set: {"word":In1} }
  return result

def delete_a_word(In):
  result = collection.delete_one(In)
  return result

def look_for_meaning(In):
  result = collection.find_one("word":In)
  print(result)


#Programa principal-----------------------------------------------

print("_________________Diccionario slang panameño_________________")
do {
print("""
    Elegir una de las siguientes opciones:
        1.- Añadir nueva palabra
        2.- Cambiar palabra existente
        3.- Eliminar palabra del diccionario
        4.- Mostrar todas las palabras con su significado
        5.- Buscar el significado de una palabra
""")
num = input()
if num == 1:
  print("Añadir nueva palabra")

  palabra = input("palabra: ")
  significado = input("significado: ")
  pal = {"word":palabra, "meaning":significado}
  add_word(pal)
elif num == 2:
  print("Cambiar palabra existente")
  palabra2 = input("palabra a cambiar: ")
  nuevaPalabra = input("nueva palabra: ")
  change_word(palabra2,nuevaPalabra)
elif num == 3:
  print("Eliminar palabra del diccionario")
  palabra3 = input("palabra: ")
  pal3 = {"word":palabra3}
  delete_a_word(pal3)
elif num == 4:
  print("Mostrar todas las palabras con su significado")
  result4 = collection.find()
  print(result4)
elif num == 5:
  print("Buscar el significado de la siguiente palabra")
  palabra5 = input("palabra:")
  show5 = {"word":palabra5, "meaning"}
  print(show)
elif:
  print("El programa se reiniciara")

}while(num>0);