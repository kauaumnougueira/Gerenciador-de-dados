from functools import partial
from tkinter import *
from tkinter import ttk
from data import *
from system import *
from interface import *

"""
-- algoritmo dos menus --
1. instancia e desenha o frame principal
2. instancia os elementos gráficos
3. aplica configurações nos elementos gráficos(atribui link a botões, inputs etc) através da função 'configureCommands()'
4. desenha todos os elementos gráficos dentro do frame principal através da função
"""

"""
menu
    1. overview
    2. members
        2.1. listMembers
            2.1.1. memberProfile
        2.2. memberRegistration
    3. reports
        3.1. listReports
        3.2. newReport
    4. backups
        4.1. listBackups
        4.2. newBackup
"""

#INSTANCIA O OBJETO Tk() E ATRIBUI à VARIÁVEL window PARA CRIAR A JANELA ONDE SERÃO DISPOSTOS OS FRAMES
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
# 1
def overview():
    frame = initializeFrame(window)
    
    titulo = Label(frame, text="VISÃO GERAL")

    consultar_lista = Button(frame, text="Botão")
    voltar = Button(frame, text="Voltar", command=menu)

    configureCommands(frame, [consultar_lista, voltar], [menu, menu])
    drawMenu(frame, titulo, [consultar_lista], voltar)

#=================================================
# 2
def members(): 
    frame = initializeFrame(window)
    
    titulo = Label(frame, text="MEMBROS")
    
    consultar_lista = Button(frame, text="Membros")
    cadastrar_membro = Button(frame, text="Cadastrar")
    voltar = Button(frame, text="Voltar")

    configureCommands(frame, [consultar_lista, cadastrar_membro, voltar], [listMembers, memberRegistration, menu])
    drawMenu(frame, titulo, [consultar_lista, cadastrar_membro], voltar)

#=================================================
# 2.1
def listMembers():
    frame = initializeScrollableFrame(window)

    titulo = Label(frame["main_frame"], text = "LISTA DE MEMBROS")

    initializeAndConfigureListButtons(frame, 'members_data', memberProfile)

    voltar = Button(frame["main_frame"], text="Voltar")

    configureCommands(frame["main_frame"], [voltar], [members])
    drawScrollableMenu(frame, titulo, voltar)


#=================================================
# 2.1.1
#EM DESENVOLVIMENTO
def memberProfile(index): 
    frame = initializeFrame(window)

    titulo = Label(frame, text = "PERFIL DO MEMBRO")
#=================================================
# 2.2
#EM DESENVOLVIMENTO
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

menu()

#CONFIGURAÇÕES APLICADAS NA INICIALIZAÇÃO
window.title("Célula Nova Vida")
window.iconphoto(True, PhotoImage(file='img/icone_app.png'))
window.geometry("325x400")
window.resizable(width = 0, height = 0)
window.mainloop() #INICIA A JANELA
