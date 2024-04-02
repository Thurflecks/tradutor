import tkinter as Tk
from tkinter import *
from translate import Translator
import translate 
import os
from tkinter import messagebox


root = Tk()
root.geometry('410x500')
root.title('                                                Tradutor ')
root.maxsize(410, 500)
root.minsize(410, 500)
root.iconbitmap('ico.ico')
root.configure(background='black')


def delelar():
    en.delete(0, "end")
    lb2.configure(text=(' '))
    

def Onclick():
    lang1 = en2.get()
    lang3 = en3.get()
    
    if lang1 in ['pt-br', 'en', 'es'] and lang3 in ['pt-br', 'en', 'es']:
        lb2.configure(text=(' '))
    else:
        messagebox.showerror("aviso:", "idioma incorreto")
        
def copiar(): 
    if lb2["text"] == "":
        messagebox.showinfo("aviso:", "nada copiado")
    else:
        root.clipboard_clear()
        root.clipboard_append(lb2["text"])
        root.update()           
        messagebox.showinfo("aviso:", "copiado")   

def get_bem_vindo():
    nome_usuario = os.getlogin()
    bem_vindo.config(text='Bem Vindo ao Tradutor dos Fellas ' + nome_usuario)


def get_bt():
    dados = en.get()
    lang1 = en2.get()
    lang3 = en3.get()
    trad = Translator(from_lang=(lang1), to_lang=(lang3))
    saida = trad.translate(str(dados))
    lb2.configure(text=(saida))
            
    
        
    
    
bem_vindo = Label(root, font='Gabriola 18', bg = '#000', fg = '#e827ea')
bem_vindo.place(x=45, y=10)   

en2 = Entry(font='Arial 14')
en2.place(x=90, y=98)

   
origem = Label(root, font='Arial 13', text='Selecione o idioma de origem: pt-br, en, es.', bg = '#000', fg = 'White')
origem.place(x=50, y=60)



origem2 = Label(root, font='Arial 13', text='Selecione o idioma de saída: pt-br, en, es.', bg = '#000', fg = 'White')
origem2.place(x=50, y=138)


en3 = Entry(font='Arial 14')
en3.place(x=90, y=177)



lang1 = en3.get()
lang3 = en3.get()


lb1 = Label(root, font='Arial 13', text='Digite o que você deseja traduzir:', bg = '#000', fg = 'White')
lb1.place(x=80, y=220)

en = Entry(font='Arial 14')
en.place(x=90, y=260)

bt = Button(font='Arial 13', bg = '#000', fg = '#e827ea', text='Traduzir', command=get_bt)
bt.place(x=160, y=310)

bt1 = Button(font='Arial 13', bg = '#000', fg = '#e827ea', text='verificar', command=Onclick)
bt1.place(x=330, y=175)

lb3 = Label(root, font='Gabriola 19', text='Tradução:', bg = '#000', fg = 'White')
lb3.place(x=155, y=360)

lb2 = Label(root, font='Gabriola 19', text='', bg = '#000', fg = 'White')
lb2.place(x=130, y=405)

bt_copiar = Button(font='Arial 13', bg = '#000', fg = '#e827ea', text='copiar', command=copiar)
bt_copiar.place(x=165, y=460)

btDeletar = Button(font='Arial 13', bg = '#000', fg = '#e827ea', text='limpar', command=delelar, height= 1)
btDeletar.place(x=330, y=257)


get_bt()
get_bem_vindo()



root.mainloop()