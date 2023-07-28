import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:


A)  Al presionar el botón 'Agregar' se debera cargar el peso* de un articulo, el cual podra ser ingresado en gramos o en onzas 

    La unidad de medida es indicada mediante una lista desplegable.

* Flotantes mayores que cero

Si existe error al validar indicarlo mediante un Alert
Si se cargo  correctamente indicarlo con un Alert

-- SOLO SE CARGARAN LOS VALORES SI Y SOLO SI SON CORRECTOS --

B) Al precionar el boton mostrar se deberan listar los pesos en gramos, en onzas y su posicion en la lista (por terminal)

Del punto C solo debera realizar dos informes,
para determinar que informe hacer, tenga en cuenta lo siguiente:
    
    1- Tome el ultimo numero de su DNI Personal (Ej 4) y realiza ese informe (Ej, Realizar informe 4)

    2- Tome el ultimo numero de su DNI Personal (Ej 4), y restarselo al numero 9 (Ej 9-4 = 5). 
    Realiza el informe correspondiente al numero obtenido.
    
EL RESTO DE LOS INFORMES LOS PUEDE IGNORAR. 

C) Al precionar el boton Informar 
    0- Valor (en onzas) y posicion del articulo mas pesado
    1- Valor (en gramos) y posicion del articulo mas liviano
    2- Peso promedio (en onzas) 
    3- Peso promedio (en gramos)
    4- Informar los pesos que superan el promedio (en gramos)
    5- Informar los pesos que NO superan el promedio (en onzas)
    6- Informar la cantidad de articulos que superan el peso promedio
    7- Informar la cantidad de articulos que NO superan el peso promedio
    8- Indicar los pesos repetidos (gramos)
    9- Indicar los pesos NO repetidos (gramos)


1 gramo son 0.035274 oz
1 oz son 28.3495 gramos
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        # configure window
        self.title("RECUPERATORIO EXAMEN INGRESO")

        self.txt_peso_articulo = customtkinter.CTkEntry(master=self, placeholder_text="PESO")
        self.txt_peso_articulo.grid(row=1, padx=20, pady=20)

        self.combobox_tipo_de_peso = customtkinter.CTkComboBox(master=self, values=["Gramos","Onzas"])
        self.combobox_tipo_de_peso.grid(row=2, column=0, padx=20, pady=(10, 10))

        self.btn_agregar = customtkinter.CTkButton(master=self, text="Agregar", command=self.btn_agregar_on_click)
        self.btn_agregar.grid(row=3, padx=20, pady=20, columnspan=2, sticky="nsew")
       
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=4, padx=20, pady=20, columnspan=2, sticky="nsew")

        self.btn_informar= customtkinter.CTkButton(master=self, text="Informar", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=5, padx=20, pady=20, columnspan=2, sticky="nsew")        

        self.lista_pesos = []


    def btn_agregar_on_click(self):
        # Tomar datos
        peso = self.txt_peso_articulo.get()
        unidad = self.combobox_tipo_de_peso.get()
        
        # Validar datos: Flotantes mayores que cero
        
        peso_es_valido = False
        contador_de_puntos = 0
        
        if peso:
            for letra in peso:
                if not letra.isdecimal() and letra != ".":
                    peso_es_valido = False
                    break
                elif letra == ".":
                    contador_de_puntos += 1
                    if contador_de_puntos > 1:
                        peso_es_valido = False
                        break
                else:
                    peso_es_valido = True

                # if letra.isdecimal():
                #     peso_es_valido = True
                # elif bandera_de_puntos and letra == ".":
                #     bandera_de_puntos = False
                #     peso_es_valido = True
                # else:
                #     peso_es_valido = False
                #     break
        
            peso = float(peso)

            if unidad == "Onzas":
                peso = peso * 28.3495

            self.lista_pesos.append(peso)

            if peso <= 0:
                peso_es_valido = False

        if peso_es_valido:
            txt = "El peso es valido"
        else:
            txt = "El peso no es valido"
        
        alert("Carga", txt)

    def btn_mostrar_on_click(self):
        self.lista_pesos = [1.2, 3.4, 123.2, 54.3]

        pesos_en_gramos = ""

        i = 0
        for peso in self.lista_pesos:
            print(f"Indice {i}")
            i += 1
            pesos_en_gramos += str(peso) + " grs\n"
        for i in range(len(self.lista_pesos)):
            print(f"Indice {i} - Valor {self.lista_pesos[i]}")

        for i, peso in enumerate(self.lista_pesos):
            print(f"Indice {i} - Valor {peso}")

        alert("Pesos en gramos", pesos_en_gramos)

        pesos_en_onzas = []

        for peso in self.lista_pesos:
            peso_onzas = peso / 28.3495
            pesos_en_onzas.append(peso_onzas)

        pesos_en_onzas_txt = ''
        for peso in pesos_en_onzas:
            pesos_en_onzas_txt += str(peso) + " oz\n"

        alert("Pesos en onzas", pesos_en_onzas_txt)


    def btn_informar_on_click(self):
       # Indicar pesos repetidos (gramos)
        self.lista_pesos = [1.2, 1.2, 3.4, 54.3, 123.2, 54.3, 1.2]

        pesos_repetidos = []
        
        for peso in self.lista_pesos:
            print(peso)
            print(self.lista_pesos.count(peso))
            if self.lista_pesos.count(peso) > 1 and pesos_repetidos.count(peso) == 0:
                pesos_repetidos.append(peso)

            if self.lista_pesos.count(peso) > 1: # se repite
                if pesos_repetidos.count(peso) == 0: # esta en la lista
                    pesos_repetidos.append(peso)
            # if peso not in pesos_repetidos and self.lista_pesos.count(peso) > 1:
            #     pesos_repetidos.append(peso)

        print(f"Lista de pesos repetidos: {pesos_repetidos}")

if __name__ == "__main__":
    app = App()

    app.mainloop()
