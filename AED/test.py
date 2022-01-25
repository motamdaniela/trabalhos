from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")
window.title("Test")

nome_selecao = "Nome(0)"
#txt_comentario = "text text text"
username = "user123"
spin = 6

button = Button(window,height=3, width=10, text=">", command = lambda: avaliar(spin,nome_selecao))
button.place(x=20, y=20)

def avaliar(spin,nome_selecao):
    catalogo = open("catalogo.txt","r", encoding="UTF-8")
    lista = catalogo.readlines()
    if username == "":
        msg = messagebox("Sessão não iniciada", "Por favor faça login!")
    else:
        for line in lista:
            campos = line.split(";")
            if campos[0] == nome_selecao:
                numerador = float(campos[4][0])
                divisor = float(campos[4][1])
                numerador = numerador*divisor + float(spin)  #soma anterior + nova pontuacao
                divisor += 1
                number = round(numerador/divisor)   #pontuacao é igual à media
                campos[4] = str(number) + str(round(divisor))
                new_line = campos[0] + ";" + campos[1] + ";" + campos[2] + ";" + campos[3] + ";" + campos[4] + ";" + campos[5] + ";" + campos[6] + ";" + campos[7] + ";" + campos[8] + ";" + campos[9]
                lista[lista.index(line)] = str(new_line)
                catalogo = open("catalogo.txt", "w")
                catalogo.write("")
                catalogo = open("catalogo.txt", "a", encoding="UTF-8")
                for i in range(len(lista)):
                    catalogo.write(lista[i])
                break
    catalogo.close()

window.mainloop()