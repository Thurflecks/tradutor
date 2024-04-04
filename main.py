import customtkinter
from customtkinter import *
from translate import Translator
import translate 
import os


root = customtkinter.CTk()
root.geometry('410x550')
root.title('                                                Tradutor ')
root.maxsize(410, 550)
root.minsize(410, 550)
root.iconbitmap('tradutor.ico')
root.configure(background='black')

portugues = 'pt-br'
espanhol = "es"
ingles = "en"

idiomas = [portugues, espanhol, ingles]

def delelar():
    en.delete(0, "end")
    lb2.configure(text=(' '))
    aviso.configure(text="")

        
def copiar(): 
    if lb2.cget('text') == "":
        aviso.configure(text=("Aviso: Nada copiado"))
    else:
        root.clipboard_clear()
        root.clipboard_append(aviso.cget('text'))
        root.update()           
        aviso.configure(text=("Aviso: Copiado")) 

def get_bem_vindo():
    nome_usuario = os.getlogin()
    bem_vindo.configure(text='Bem Vindo ao Tradutor dos Fellas, ' + nome_usuario)


def get_bt():
    dados = en.get()
    if dados in ["", " "]:
        lb2.configure(text=("Escreva algo para traduzir!"))
    else:
        dados = en.get()
        lang1 = en2.get()
        lang3 = en3.get()
        trad = Translator(from_lang=(lang1), to_lang=(lang3))
        saida = trad.translate(str(dados))
        lb2.configure(text=(saida))
    
            
var = customtkinter.StringVar(root)
var.set(idiomas[0])    

var1 = customtkinter.StringVar(root)
var1.set(idiomas[0]) 
        
    

bem_vindo = customtkinter.CTkLabel(root)
bem_vindo.place(relx=0.5, y=20, anchor="center")   

en2 = customtkinter.CTkOptionMenu(root, variable=var, values=idiomas)
en2.place(relx=0.5, y=98, anchor="center")

   
origem = customtkinter.CTkLabel(root, text='Selecione o idioma de origem:')
origem.place(relx=0.5, y=60, anchor="center")



origem2 = customtkinter.CTkLabel(root, text='Selecione o idioma de saída:')
origem2.place(relx=0.5, y=138, anchor="center")


en3 = customtkinter.CTkOptionMenu(root, variable=var1, values=idiomas)
en3.place(relx=0.5, y=177, anchor="center")



lang1 = en3.get()
lang3 = en3.get()


lb1 = customtkinter.CTkLabel(root, text='Digite o que você deseja traduzir:')
lb1.place(relx=0.5, y=220, anchor="center")

en = customtkinter.CTkEntry(root)
en.place(relx=0.5, y=260, anchor="center")

bt = customtkinter.CTkButton(root, text='Traduzir', command=get_bt)
bt.place(relx=0.5, y=310, anchor="center")

lb3 = customtkinter.CTkLabel(root, text='Tradução:')
lb3.place(relx=0.5, y=350, anchor='center')

lb2 = customtkinter.CTkLabel(root, text='')
lb2.place(relx=0.5, y=390, anchor="center")

bt_copiar = customtkinter.CTkButton(root, text='copiar', command=copiar)
bt_copiar.place(relx=0.5, y=460, anchor="center")

btDeletar = customtkinter.CTkButton(root, text='limpar', command=delelar, width= 1)
btDeletar.place(x=310, y=246)

aviso = customtkinter.CTkLabel(root, text='')
aviso.place(relx=0.5, y=500, anchor="center")



get_bem_vindo()



root.mainloop()