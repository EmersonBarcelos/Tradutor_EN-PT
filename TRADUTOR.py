from logging import root
from translate import Translator
from tkinter import *
from tkinter.filedialog import asksaveasfilename

janela = Tk()
janela.title('TRADUTOR EN/PT')
file_path = ''
tradulen = StringVar()
tradupass = StringVar()

#Funções para as opções
def set_file_path(path):
    global file_path
    file_path = path

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Text Files', '*.txt')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = tradupass.get()
        file.write(code)
        set_file_path(path)

def run_en():
    s = Translator(from_lang="english", to_lang="pt-br")
    tradu = tradulen.get()
    convert = s.translate(tradu)
    tradupass.set(convert)

def run_pt():
    s = Translator(from_lang="pt-br", to_lang="english")
    tradu = tradulen.get()
    convert = s.translate(tradu)
    tradupass.set(convert)


#Criando barras com opções
menu_bar = Menu(janela)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Salvar', command=save_as)
file_menu.add_command(label='Sair', command=exit)
menu_bar.add_cascade(label='Arquivo', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='EN/PT', command=run_en)
run_bar.add_command(label='PT/EN', command=run_pt)
menu_bar.add_cascade(label='Traduzir', menu=run_bar)

#Criando os campos para captura e apresentação dos textos
janela.config(menu=menu_bar)
Label(janela, text="DIGITAR TEXTO ↓").pack()
Entry(janela, textvariable=tradulen, width=50).pack(pady=10)
Label(janela, text="TRADUÇÃO ↓").pack()
Entry(janela, textvariable=tradupass, width=50).pack(pady=10)
janela.mainloop()
