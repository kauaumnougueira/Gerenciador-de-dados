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
    1. Através da função readFile() todos os dados são copiados do banco de dados para a variável 'raw_data'.
    2. Através da função dataFormattingFilter() os dados copiados são formatados e atribuídos à variável 'data'.
    3. Verifica a ação solicitada e retorna os dados específicos.
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
        return members_data #RETORNA UMA MATRIZ COM UM VETOR PARA CADA MEMBRO
    if action == 'number_of_reports':
        for i in range(0, len(data)):
            if data[i] == '#REPORT#':
                counter += 1
        return counter #RETORNA A QUANTIDADE DE RELATÓRIOS
    if action == 'reports_data':
        for i in range(0, len(data)):
            if data[i] == '#REPORT#':
                reports_data.append([data[i+1], data[i+2], data[i+3], data[i+4], data[i+5], data[i+6], data[i+7], data[i+8]])
        return reports_data #RETORNA UMA MATRIZ COM UM VETOR PARA CADA RELATÓRIO


#variaveis de dados
report_data = requestData('reports_data')
number_of_members = requestData('number_of_members')
member_data = requestData('members_data')
all_data = [member_data, report_data]
#variaveis de dados


def dataRegistration(action, new_data, arquivo = 'data.txt'):
    """
    Faz a gravação de dados no banco de dados.
    1. Solicita os dados antigos do banco de dados.
    2. Através do tratamento de erros e exceções checa se é possível abrir o arquivo para escrita.
    3. Verifica a ação solicitada e transcreve os novos dados para o banco de dados.
    """
    member_data = requestData('members_data')
    report_data = requestData('reports_data')
    data = [member_data, report_data]
    try:
        archive = open(arquivo, 'wt') #a de append, adicionar dados no arquivo de texto
        #arquivo é o arquivo editável depois de aberto
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


def processMemberData(frame, action, destiny, data = False, index = False):
    """
    Coleta os dados dos inputs, formata-os e transcreve para o banco de dados.
    + Ação 'member_registration'
        1. Coleta os dados de entrada do usuário com a função collectData() e atribui à variável 'new_data' o retorno dessa função(uma lista/array/vetor).
        2. Grava os dados no banco de dados através da função dataRegistration().
        3. Dispara uma caixa de mensagem após o registro das informações.
        4. Deleta o Frame atual e prossegue para o destino.
    + Ação 'delete_info_member'
        1. Dispara uma caixa de mensagem para confirmar a decisão do usuário.
        2. Caso retornar True os dados dos membros são requisitados através da função requestData().
        3. Os dados do membro escolhido são deletados por meio do índice através de del().
        4. Grava os dados no banco de dados através da função dataRegistration().
        5. Deleta o Frame atual e prossegue para o destino.
    + Ação 'update_info_member'
        1. Dispara uma caixa de mensagem para confirmar a decisão do usuário.
        2. Coleta os dados de entrada do usuário com a função collectData() e atribui à variável 'new_data' o retorno dessa função(uma lista/array/vetor).
        3. Os novos dados são substituidos na matriz 'members_data' por meio do índice.
        4. Grava os dados no banco de dados através da função dataRegistration().
        5. Deleta o Frame atual e prossegue para o destino.
    """
    if action == 'member_registration':
        new_data = collectData(data)
        dataRegistration(action, new_data)
        messagebox.showinfo(title = "Aviso", message = "Novo membro adicionado.")
        deleteFrameAndGo(frame, destiny)
    
    if action == 'delete_info_member':
        decision = messagebox.askyesno(title = "Confirmar", message = "Tem certeza de que deseja excluir os dados?")
        if decision:
            data = requestData("members_data")
            del(data[index])
            dataRegistration('update_info_member', data)
            deleteFrameAndGo(frame, destiny)
    
    if action == 'update_info_member':
        decision = messagebox.askyesno(title = "Confirmar", message = "Tem certeza de que deseja salvar as modificações?")
        if decision:
            new_data = collectData(data)
            members_data = requestData("members_data")
            members_data[index] = new_data
            dataRegistration(action, members_data)
            deleteFrameAndGo(frame, destiny)