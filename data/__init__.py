from interface import deleteFrameAndGo
from system import collectData, dataFormattingFilter, transcriptToDatabase
from tkinter import messagebox

#====================================
#FUNÇÕES DE MANIPULAÇÃO DE ARQUIVO
def checkData(arquivo = 'data.txt'):

    if searchFile(arquivo):
        print("Banco de dados encontrado.")
    else:
        print("Banco de dados não encontrado.")
        createFile(arquivo)

def searchFile(arquivo = 'data.txt'):
    try:
        archive = open(arquivo, 'rt') #leitura arquivo texto
        archive.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(arquivo = 'data.txt'):
    try:
        archive = open(arquivo, 'wt+') #escrever arquivo e se não existir criar
    except:
        print("Não foi possível criar o banco de dados.")
    else:
        print("Banco de dados criada.")

def readFile(arquivo = 'data.txt'):
    try:
        archive = open(arquivo, 'rt')
    except:
        print("Não foi possível ler os dados.")
    else:
        return archive.readlines()
    finally:
        archive.close()

#====================================

def requestData(action):
    """
    Captura dados do .txt e transforma cada linha em um elemento de um vetor.
    """
    raw_data = readFile()
    data = dataFormattingFilter('load_from_data_base', raw_data)
    members_data = []
    reports_data = []
    counter = 0

    if action == 'all_data':
        return data
    if action == 'number_of_members':
        for i in range(0, len(data)):
            if data[i] == '#MEMBER#':
                counter += 1
        return counter #RETORNA A QUANTIDADE DE MEMBROS
    if action == 'members_data':
        for i in range(0, len(data)):
            if data[i] == '#MEMBER#':
                members_data.append([data[i+1], data[i+2], data[i+3], data[i+4], data[i+5]]) #"Nome", "Cargo", "Telefone", "Aniversário", "Data de entrada"
        return members_data #RETORNA UMA MATRIZ COM VETORES PARA CADA MEMBRO
    if action == 'number_of_reports':
        for i in range(0, len(data)):
            if data[i] == '#REPORT#':
                counter += 1
        return counter #RETORNA A QUANTIDADE DE RELATÓRIOS
    if action == 'reports_data':
        for i in range(0, len(data)):
            if data[i] == '#REPORT#':
                reports_data.append([data[i+1], data[i+2], data[i+3], data[i+4], data[i+5], data[i+6], data[i+7], data[i+8]])
        return reports_data #RETORNA UMA MATRIZ COM VETORES PARA CADA RELATÓRIO

#variaveis de dados
report_data = requestData('reports_data')
number_of_members = requestData('number_of_members')
member_data = requestData('members_data')
all_data = [member_data, report_data]
#variaveis de dados

def dataRegistration(action, new_data, arquivo = 'data.txt'):
    """
    Faz a gravação de dados no banco de dados.
    """
    member_data = requestData('members_data')
    report_data = requestData('reports_data')
    data = [member_data, report_data]
    try:
        archive = open(arquivo, 'wt') #a de append, adicionar dados no arquivo de texto
    except:
        print("Erro ao acessar banco de dados.")
    else:
        if action == 'member_registration':
            member_data.append(new_data)
            archive.write(transcriptToDatabase(data))
            
        if action == 'update_info_member':
            data = [new_data, report_data]
            archive.write(transcriptToDatabase(data))
            
        if action == 'report_registration':
            report_data.insert(0, new_data)
            archive.write(transcriptToDatabase(data))

        if action == 'update_info_report':
            data = [member_data, new_data]
            archive.write(transcriptToDatabase(data))

def checkStatus(action):
    """
    Checa se existe pelo menos um membro ou relatório no banco de dados. Retorno do tipo bool.
    """
    if action == 'member_exists':
        if requestData('number_of_members') > 0: return True
        else: return False
    if action == 'report_exists':
        if requestData('number_of_reports') > 0: return True
        else: return False

def processMemberRegistration(frame, action, data, destiny):
    """
    Registra os dados do membro após tê-los filtrado.
    """
    new_data = collectData(data)
    dataRegistration(action, new_data)
    messagebox.showinfo(title = "Aviso", message = "Novo membro adicionado.")
    deleteFrameAndGo(frame, destiny)