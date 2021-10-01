def collectData(input_data): 
    """
    Captura os dados de entrada e retorna-os em uma lista.
    """
    data = []
    for element in input_data:
        data.append(element.get())
    return data

def dataFormattingFilter(action, vector_data):
    """
    Filtra as strings/elementos para carregar do banco de dados ou gravar no banco de dados.
    """
    filtred_data = []
    if action == 'load_from_data_base':
        for element in vector_data:
            filtred_data.append(element.replace("\n", ''))
        return filtred_data
    
    if action == 'write_in_data_base':
        for line in vector_data:
            for element in line:
                element += '\n'
                filtred_data.append(element)
        return filtred_data

def structuralRearrangement(action, data):
    """
    Organiza a estrutura dos dados para gravar no .txt
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

    #PROCESSO FINAL
    rearrangement_data = dataFormattingFilter('write_in_data_base', rearrangement_data)
    return rearrangement_data

def transcriptToDatabase(data):
    """
    Junta todos os elementos do vetor numa string única.
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

