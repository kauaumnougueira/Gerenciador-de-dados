from interface import deleteFrameAndGo
from system import collectData, dataFormattingFilter, notice, transcriptToDatabase, dataLoggingSystem
from time import sleep
from tkinter import messagebox

def checkData(arquivo = 'data.txt'):

    if searchFile(arquivo):
        print("Banco de dados encontrado.")
    else:
        print("Banco de dados não encontrado.")
        createFile(arquivo)

def searchFile(arquivo = 'data.txt'):
    try:
        a = open(arquivo, 'rt') #leitura arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def createFile(arquivo = 'data.txt'):
    try:
        a = open(arquivo, 'wt+') #escrever arquivo e se não existir criar
    except:
        print("Não foi possível criar o banco de dados.")
    else:
        print("Banco de dados criada.")

def readFile(arquivo = 'data.txt'):
    try:
        a = open(arquivo, 'rt')
    except:
        print("Não foi possível ler os dados.")
    else:
        return a.readlines()
    finally:
        a.close()

def requestData(action):
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
    member_data = requestData('members_data')
    report_data = requestData('reports_data')
    data = [member_data, report_data]
    try:
        a = open(arquivo, 'wt') #a de append, adicionar dados no arquivo de texto
    except:
        print("Erro ao acessar banco de dados.")
    else:
        if action == 'member_registration':
            member_data.append(new_data)
            a.write(transcriptToDatabase(data))
            #notice("[Novo membro adicionado...]")

        if action == 'update_info_member':
            data = [new_data, report_data]
            a.write(transcriptToDatabase(data))
            notice("[Os dados foram atualizados...]")

        if action == 'report_registration':
            report_data.insert(0, new_data)
            a.write(transcriptToDatabase(data))
            notice("[Novo relatório adicionado...]")
        if action == 'update_info_report':
            data = [member_data, new_data]
            a.write(transcriptToDatabase(data))
            notice("[Os dados foram atualizados...]")

def checkStatus(action):
    if action == 'member_exists':
        if requestData('number_of_members') > 0: return True
        else:
            notice("[Não há membros para listar...]")
            return False
    if action == 'report_exists':
        if requestData('number_of_reports') > 0: return True
        else:
            notice("[Não há relatórios para listar...]")
            return False

def editData(action, position_in_matrix, position_in_list = False):
    members_data = requestData('members_data')
    reports_data = requestData('reports_data')

    if action == 'member_data':
        if position_in_list == 0:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Nome"])
        elif position_in_list == 1:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Cargo"])
        elif position_in_list == 2:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Telefone"])
        elif position_in_list == 3:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Aniversário"])
        elif position_in_list == 4:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Entrada"])
    
        members_data[position_in_matrix][position_in_list] = new_data[0]
        return members_data

    if action == 'delete_member_data':
        del(members_data[position_in_matrix])
        return members_data
    
    if action == 'report_data':
        if position_in_list == 0:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Data"])
        elif position_in_list == 1:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Frequência"])
        elif position_in_list == 2:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Visitantes"])
        elif position_in_list == 3:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Conversões"])
        elif position_in_list == 4:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Preletor"])
        elif position_in_list == 5:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Local"])
        elif position_in_list == 6:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Oferta"])
        elif position_in_list == 7:
            new_data = dataLoggingSystem("EDIÇÃO DE DADO", ["Observações"])

        reports_data[position_in_matrix][position_in_list] = new_data[0]
        return reports_data
    
    if action == 'delete_report_data':
        del(reports_data[position_in_matrix])
        return reports_data

def processMemberRegistration(frame, action, data, destiny):
    new_data = collectData(data)
    dataRegistration(action, new_data)
    messagebox.showinfo(title = "Aviso", message = "Novo membro adicionado.")
    deleteFrameAndGo(frame, destiny)