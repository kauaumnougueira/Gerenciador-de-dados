from functools import partial
from tkinter import *
import data as data

def initializeFrame(parent):
    """
    Inicializa o frame onde todos os elementos gráficos do programa devem estar contidos.
    1. Instancia o Frame.
    2. Desenha o Frame.
    3. Retorna o objeto Frame para que sejam associados os elementos gráficos.
    """
    frame = Frame(parent, borderwidth = 1, relief = "raised")
    frame.place(x = 5, y = 5, width = 315, height = 390)

    return frame
    
def initializeScrollableFrame(parent):
    """
    Inicializa o Frame principal e o Frame rolável(é um elemento gráfico que será inserido no frame principal, portanto será desenhado depois).
    1. Inicializa o Frame principal(onde serão dispostos todos os elementos gráficos).
    2. Inicializa o Frame container(onde estará contido o canvas e o scrollbar).
    3. Inicializa o Canvas(onde estará contigo o Scrollable Frame).
    4. Configura o Scrollable Frame e o Canvas.
    5. Desenha o Frame principal.
    6. Retorna os objetos inicializados (main_frame, container, canvas, scrollable_frame) num dicionário.
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

    return {"scrollable_frame": scrollable_frame, "main_frame": main_frame, "container": container, "canvas": canvas, "scrollbar": scrollbar}

def initializeAndConfigureListButtons(frame, action, destiny):
    """
    Inicializa e configura os links dos botões de uma lista.
    1. Requisita os dados através de requestData(). (ou dados dos membros ou dos relatórios dependendo da ação)
    2. Percorre cada elemento da lista/vetor/array retornada/o de requestData().
    3. Instancia um botão e inicializa configurações(Frame pai, texto, dimensões).
    4. Desenha-o no Frame pai através do método .grid().
    5. Atribui ao parâmetro "command"(parâmetro que guarda o evento que é disparado após detectar o click no botão) o algoritmo para deletar o Frame atual e prosseguir para o próximo Frame linkado com aquele botão.
    6. Itera sobre as variáveis index(guarda o índice de cada elemento da lista/vetor/array) e line(linha na qual o botão vai ser desenhado).
    """
    index = 0
    line = 1

    if action == 'members_data':
        members_data = data.requestData('members_data')
        for member in members_data:
            option = Button(frame["scrollable_frame"], text=f"{member[0]}", anchor = W, relief="ridge", width = 31, height = 2)
            option.grid(row = line, column = 1)
            option["command"] = partial(deleteFrameAndGo, frame["main_frame"], destiny, index)
            
            index += 1
            line += 1

def deleteFrameAndGo(frame, destiny, parameter = ''):
    """
    Deleta o Frame atual(objeto contigo na variável 'frame') para evitar o acúmulo de Frames na janela.
    """
    frame.destroy()
    destiny() if parameter == '' else destiny(parameter)

def configureCommands(frame, elements, destinations):
    """
    Configura links associando um elemento da variável 'elements' com um elemento da variável 'destinations' através do índice.
    1. Através de um laço percorre cada um dos elementos contidos em 'elements'.
    2. Atribui ao parâmetro "command" daquele elemento o destino(associa cada elemento de 'destinations' com cada elemento de 'elements' através do índice).
    3. Itera na variável 'index' e finaliza o laço.
    """
    index = 0
    for element in elements:
        element["command"] = partial(deleteFrameAndGo, frame, destinations[index])
        index += 1

def drawMenu(frame, title, elements, back_button = False):
    """
    Desenha um menu com títulos e botões.
    1. Inicializa as variáveis 'line'(linha do grid onde será colocado o elemento) e 'w_label'(largura do Label).
    2. Inicializa Labels para espaçamento.
    3. Desenha os Labels de espaçamentos e entre eles é desenhado o título.
    4. Através do laço serão desenhados cada um dos botões do menu.
    5. O parâmetro opcional 'back_button' é verificado. Dependendo do estado(True/False) ele será desenhado ou não.
    elements = vetor com todos os elementos gráficos
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

def drawForm(frame, title, inputs, texts, confirm_button, back_button):
    """
    Desenha todos os elementos gráficos que foram passados como parâmetro(caixa de entrada, labels etc.). e organiza-os no formato de um formulário.
    1. Inicializa as variáveis line(linha do grid onde será colocado o elemento),  'w_label'(largura do Label), index(índice dos textos) e os Labels de espaçamento.
    2. Desenha os Labels de espaçamento e o título.
    3. Através do laço são desenhados os textos(contidos em 'texts') e os inputs(contidos em 'inputs').
    4. São desenhados os botões de voltar e de confirmação do formulário.
    inputs = vetor com todos os inputs gráficos
    texts = vetor com os nomes que seguem cada um dos elementos gráficos dispostos
    """
    line = 4
    w_label = 38
    index = 0

    spacing_1 = Label(frame, width = w_label, height = 1)
    spacing_2 = Label(frame, width = w_label, height = 1)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    spacing_2.grid(row = 3, column = 1, columnspan = 3)
    
    for input in inputs:
        spacing_on_top_of_the_button = Label(frame, width = w_label, height = 1)
        spacing_on_top_of_the_button.grid(row = line, column = 1, columnspan = 3)
        
        line += 1 
        
        label_info = Label(frame, text = texts[index])
        label_info.grid(row = line, column = 1, sticky = E)

        
        input.grid(row = line, column = 2, sticky = W)
        
        line += 1
        index += 1

    spacing_3 = Label(frame, width = w_label, height = 3)
    spacing_3.grid(row = line, column = 1, columnspan = 3)

    back_button["width"] = 7
    back_button.grid(row = line+1, column = 1, sticky = E)

    confirm_button.grid(row = line+1, column = 2, columnspan = 2)

def drawScrollableMenu(frame, title, back_button):
    """
    Desenha os elementos gráficos no frame principal do menu 'Lista de membros'
    1. Inicializa a variável 'w_label'(largura do Label) e o Label de espaçamento.
    2. O Label de espaçamento e o título são desenhados nessa ordem.
    3. Os elementos gráficos passados em 'frame'(dicionário) são desenhados.
    4. O botão de voltar é desenhado.
    """
    w_label = 38

    spacing_1 = Label(frame["main_frame"], width = w_label, height = 1)

    spacing_1.grid(row = 1, column = 1, columnspan = 3)
    title.grid(row = 2, column = 1, columnspan = 3)
    
    frame["container"].place(x = 5, y = 60, width = 305, height = 285)
    frame["canvas"].place(x = 5, y = 5, width = 310, height = 275)
    frame["scrollbar"].pack(side="right", fill="y")

    back_button["width"] = 8
    back_button.place(x = 110, y = 350)