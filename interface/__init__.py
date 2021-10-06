from functools import partial
from tkinter import *

def initializeFrame(parent):
    """
    Inicializa o frame onde todos os elementos gráficos do programa devem estar contidos.
    """
    frame = Frame(parent, borderwidth = 1, relief = "raised")
    frame.place(x = 5, y = 5, width = 315, height = 390)

    return frame
    
def initializeScrollableFrame(parent):
    """
    Inicializa o frame (rolável) onde os elementos gráficos devem estar contidos.
    """

    main_frame = Frame(parent, borderwidth = 1, relief = "raised")
    container = Frame(main_frame, borderwidth = 1, relief = "sunken")
    canvas = Canvas(container)
    scrollbar = Scrollbar(container, orient = "vertical", command = canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.create_window((0, 0), window = scrollable_frame, anchor="nw")

    canvas.configure(yscrollcommand = scrollbar.set)

    main_frame.place(x = 5, y = 5, width = 315, height = 390)
    container.place(x = 5, y = 60, width = 305, height = 285)
    canvas.place(x = 5, y = 5, width = 310, height = 275)
    scrollbar.pack(side="right", fill="y")

    return {"scrollable_frame": scrollable_frame, "main_frame": main_frame}

def deleteFrameAndGo(frame, destiny):
    frame.destroy()
    destiny()

def configureCommands(frame, elements, destinations):
    position = 0
    for element in elements:
        element["command"] = partial(deleteFrameAndGo, frame, destinations[position])
        position += 1

def drawMenu(frame, title, elements, back_button = False):
    """
    elements = vetor com todos os elementos gráficos
    Desenha um menu com títulos e botões.
    """
    line = 4
    w_label = 38

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_2 = Label(frame, width = w_label, height = 2)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_2.grid(row = 3, column = 1, columnspan = 3)
    
    
    for element in elements:
        spacing_on_top_of_the_button = Label(frame, width = w_label, height = 1)
        spacing_on_top_of_the_button.grid(row = line, column = 1, columnspan = 3)
        
        line += 1 
        
        element["width"] = 10
        element["height"] = 2
        element.grid(row = line, column = 2)
        
        line += 1 
    
    if back_button:
        spacing_3 = Label(frame, width = w_label, height = 2)
        spacing_3.grid(row = line, column = 1, columnspan = 3)
        back_button["width"] = 8
        back_button.grid(row = line+1, column = 2)

def drawForm(frame, title, elements, texts, confirm_button, back_button):
    """
    elements = vetor com todos os elementos gráficos
    texts = vetor com os nomes que seguem cada um dos elementos gráficos dispostos
    Desenha todos os elementos gráficos que foram passados como parâmetro(caixa de entrada, labels etc.). e organiza-os no formato de um formulário.
    """
    line = 4
    w_label = 38
    position = 0

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_2 = Label(frame, width = w_label, height = 1)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_2.grid(row = 3, column = 1, columnspan = 3)
    
    for element in elements:
        spacing_on_top_of_the_button = Label(frame, width = w_label, height = 1)
        spacing_on_top_of_the_button.grid(row = line, column = 1, columnspan = 3)
        
        line += 1 
        
        label_info = Label(frame, text = texts[position])
        label_info.grid(row = line, column = 1, sticky = E)

        
        element.grid(row = line, column = 2, sticky = W)
        
        line += 1
        position += 1

    spacing_3 = Label(frame, width = w_label, height = 3)
    spacing_3.grid(row = line, column = 1, columnspan = 3)

    back_button["width"] = 7
    back_button.grid(row = line+1, column = 1, sticky = E)

    confirm_button.grid(row = line+1, column = 2, columnspan = 2)

def drawMenuListMembers(frame, title, back_button):
    """
    Desenha os elementos gráficos no frame principal do menu 'Lista de membros'
    """
    w_label = 38

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_for_scrollable_frame = Label(frame, height = 18)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_for_scrollable_frame.grid(row = 3, column = 1, sticky = W)

    back_button["width"] = 8
    back_button.grid(row = 4, column = 2)