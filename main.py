from cgitb import text
from functools import partial
from tkinter import *
from tkinter import ttk
from data import *
from system import *
from interface import *

window = Tk()

#=================================================

def menu():
    frame = initializeFrame(window)

    titulo = Label(frame, text="MENU")
    
    visao_geral = Button(frame, text="Visão geral")
    membros = Button(frame, text="Membros")   
    relatorios = Button(frame, text="Relatórios")
    backup = Button(frame, text="Backup")

    configureCommands(frame, [visao_geral, membros], [overview, members])
    drawMenu(frame, titulo, [visao_geral, membros, relatorios, backup])

#=================================================

def overview():
    frame = initializeFrame(window)
    
    titulo = Label(frame, text="VISÃO GERAL")

    consultar_lista = Button(frame, text="Botão")
    voltar = Button(frame, text="Voltar", command=menu)

    configureCommands(frame, [consultar_lista, voltar], [menu, menu])
    drawMenu(frame, titulo, [consultar_lista], voltar)

#=================================================

def members(): 
    frame = initializeFrame(window)
    
    titulo = Label(frame, text="MEMBROS")
    
    consultar_lista = Button(frame, text="Membros")
    cadastrar_membro = Button(frame, text="Cadastrar")
    voltar = Button(frame, text="Voltar")

    configureCommands(frame, [consultar_lista, cadastrar_membro, voltar], [menu, memberRegistration, menu])
    drawMenu(frame, titulo, [consultar_lista, cadastrar_membro], voltar)

#=================================================

def listMembers():
    frame = initializeFrame(window)

    titulo = Label(frame, text = "LISTA DE MEMBROS")

    #função para criar várias labels com os nomes dos membros

#=================================================

def memberRegistration():
    frame = initializeFrame(window)

    titulo = Label(frame, text = "CADASTRO DE NOVO MEMBRO")

    nome = Entry(frame, width = 20)
    cargo = ttk.Combobox(frame, values = ["Líder", "Vice-líder", "Tesoureiro", "Membro"], width = 10)
    cargo.current(3)

    telefone = Entry(frame, width = 15)
    aniversario = Entry(frame, width = 10)
    entrada = Entry(frame, width = 10)

    voltar = Button(frame, text = "Voltar")
    voltar["command"] = partial(deleteFrameAndGo, frame, members)

    confirmar = Button(frame, text = "Confirmar", padx = 40)
    confirmar["command"] = partial(processMemberRegistration, frame, 'member_registration', [nome, cargo, telefone, aniversario, entrada], members)

    drawForm(frame, titulo, [nome, telefone, cargo, aniversario, entrada], ["Nome: ", "Telefone: ", "Cargo: ", "Aniversário: ", "Entrada: "], confirmar, voltar)

#=================================================

#INICIO
menu()

#configurações
window.title("Célula Nova Vida")
window.iconphoto(True, PhotoImage(file='/home/pedro/Área de Trabalho/Projetos/Gerenciador de dados/Protótipo 2/icone_app.png'))
window.geometry("325x400")
window.resizable(width = 0, height = 0)
window.mainloop()
