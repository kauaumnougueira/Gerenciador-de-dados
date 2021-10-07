def collectData(input_data): 
    """
    Captura os dados de entrada e retorna-os em uma lista.
    1. Inicializa a variável 'data', lista onde serão atribuídos os elementos.
    2. Através do laço de repetição são acessadas cada um dos elementos(entradas do usuário) contidos na variável 'input_data'.
    3. Os elementos são adicionados na lista 'data'.
    4. Retorna a lista que contém todas as entradas do usuário.
    """
    data = []

    for element in input_data:
        data.append(element.get())

    return data

def dataFormattingFilter(action, vector_data):
    """
    Filtra as strings/elementos para carregar do banco de dados ou gravar no banco de dados.
    1. Inicializa a variável 'filtred_data'.
    2. Verifica a ação solicitada.
    3. Ação 'load_from_data_base': é retirado \n no final de cada um dos elementos da matriz/lista.
    4. Ação 'write_in_data_base': é adicionado \n no final de cada um dos elementos da matriz/lista.
    5. Retorna os dados filtrados.
    """
    filtred_data = []

    if action == 'load_from_data_base':
        for element in vector_data:
            filtred_data.append(element.replace("\n", ''))
    
    if action == 'write_in_data_base':
        for line in vector_data:
            for element in line:
                element += '\n'
                filtred_data.append(element)
        
    return filtred_data

def structuralRearrangement(action, data):
    """
    Organiza a estrutura dos dados para gravar no .txt
    1. Inicializa a variável 'rearrangement_data', matriz onde serão atribuídos os elementos.
    2. Verifica a ação solicitada.
    3. Através do laço de repetição se inicia o processo de organização da estrutura dos dados em uma matriz usando os métodos de listas(insert e append).
    4. Através da função dataFormattingFilter() a estrutura é formatada(são colocados \n) e o retorno dessa função é atribuído à variável 'rearrangement_data'.
    5. Retorna a estrutura organizada e formatada.
    """
    rearrangement_data = []

    if action == 'members_data':
    #PROCESSO DE REARRANJO DA ESTRUTURA
        rearrangement_data = [["##MEMBERS_DATA##"]]
        for member in data:
            member.insert(0, "#MEMBER#")
            member.append("########")
            rearrangement_data.append(member)
    if action == 'reports_data':
        rearrangement_data = [["##REPORTS_DATA##"]]
        for report in data:
            report.insert(0, "#REPORT#")
            report.append("########")
            rearrangement_data.append(report)

    rearrangement_data = dataFormattingFilter('write_in_data_base', rearrangement_data)
    
    return rearrangement_data

def transcriptToDatabase(data):
    """
    Junta todos os elementos do vetor numa string única.
    1. Através da função structuralRearrangement() todos os dados são reorganizados numa matriz para que possam ser formatados e gravados no banco de dados.
    2. É inicializado a variável 'transcribed_data' onde serão armazenados todos os dados em uma string única.
    3. Através dos laços de repetição cada elemento da matriz é somado à variável 'transcribed_data'.
    4. Retorna a string para ser escrita no banco de dados (etapa final do processo de escrita no banco de dados).
    """
    members_data = structuralRearrangement('members_data', data[0])
    reports_data = structuralRearrangement('reports_data', data[1])
    transcribed_data = ''

    for member in members_data:
        for infos in member:
            transcribed_data += f"{infos}"

    for report in reports_data:
        for infos in report:
            transcribed_data += f"{infos}"
        
    return transcribed_data

