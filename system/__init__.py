from time import sleep
import os

def clear():
    os.system('clear')

def collectData(input_data): #irá pegar os dados de entrada e retorná-los em um vetor
    data = []
    for element in input_data:
        data.append(element.get())
    return data

def decisionSystem(menu_message, opcoes, additional_option = False):
    decisao = False
    error_message = False
    #menu
    while decisao == False:
        clear()
        print("{:^25}\n".format(menu_message))
        #print das opções
        for i in range(0, len(opcoes)):
            print(f"[{i+1}]. {opcoes[i]}")
        #botão para voltar
        if additional_option: print(f"\n[0]. Voltar | [*]. {additional_option}\n")
        else: print("\n[0]. Voltar\n")
        #mensagem de erro na entrada
        if error_message:
            print("[Entrada incorreta]")
        entrada = input("~> ")
        #verificação da entrada
        if additional_option: 
            if entrada == '*': 
                return '*'
        #CASO NÃO HOUVE OPÇÕES ADICIONAIS
        for i in range(0, len(opcoes)+1):
            if entrada == str(i):
                return i
        error_message = True

def dataLoggingSystem(menu_message, inputs):
    data_list = []
    clear()

    print("{:^18}\n".format(menu_message))

    for i in range(0, len(inputs)):
        data_input = input(f"{inputs[i]}: ")
        #data_list += f'{data_input}\n'
        data_list.append(data_input)

    return data_list

def dataFormattingFilter(action, vector_data):
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

def presentationMode(action, input_model): #RETORNO: VETOR
    output_model = []
    if action == 'list_members':
        for i in range(0, len(input_model)):
            output_model.append(f"{input_model[i][0]:<30}| {input_model[i][1]:>10}") #MODELO DE APRESENTAÇÃO DOS NOMES DOS MEMBROS
        return output_model
    if action == 'infos_member': #MODELO DE APRESENTAÇÃO DAS INFORMAÇÕES DO MEMBRO
        #"Nome", "Cargo", "Telefone", "Aniversário", "Data de entrada"
        output_model.append(f"Nome:        {input_model[0]}")
        output_model.append(f"Cargo:       {input_model[1]}")
        output_model.append(f"Telefone:    {input_model[2]}")
        output_model.append(f"Aniversário: {input_model[3]}")
        output_model.append(f"Entrada:     {input_model[4]}")
        return output_model
    if action == 'list_reports':
        for i in range(0, len(input_model)):
            output_model.append(f"Célula | {input_model[i][0]:>10}") #MODELO DE APRESENTAÇÃO DOS NOMES DOS MEMBROS
        return output_model
    if action == 'infos_report': #MODELO DE APRESENTAÇÃO DAS INFORMAÇÕES DO MEMBRO
        #"Nome", "Cargo", "Telefone", "Aniversário", "Data de entrada"
        output_model.append(f"Data:        {input_model[0]}")
        output_model.append(f"Frequência:  {input_model[1]}")
        output_model.append(f"Visitantes:  {input_model[2]}")
        output_model.append(f"Conversões:  {input_model[3]}")
        output_model.append(f"Preletor:    {input_model[4]}")
        output_model.append(f"Local:       {input_model[5]}")
        output_model.append(f"Oferta:      {input_model[6]}")
        output_model.append(f"Observações: {input_model[7]}")
        return output_model

def structuralRearrangement(action, data):
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

def transcriptToDatabase(data): #TRANSFORMA TODOS OS ELEMENTOS DO VETOR EM UMA STRING PARA PASSAR PARA O BANCO DE DADOS
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

def notice(text, time = 2):
    clear()
    print(text)
    sleep(time)

