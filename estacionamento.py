veiculos = []
CAPACIDADE_MAXIMA = 10

def validar_horario_saida(placa ,horario_saida):

    """Devolve True se o horario de saida do carro for maior que o horario de entrada do mesmo carro"""
    
    for placas in veiculos:
        if placa == placas['placa']:
            horario_entrada = placas['entrada']
            
    horas_entrada = int(horario_entrada[:2])
    minutos_entrada = int(horario_entrada[3:])
    
    horas_saida = int(horario_saida[:2])
    minutos_saida = int(horario_saida[3:])
    
    minutos_totais_entrada = (60 * horas_entrada) + minutos_entrada
    minutos_totais_saida = (60 * horas_saida) + minutos_saida
    
    if minutos_totais_saida >= minutos_totais_entrada:
        return True 
    else:
        return False

def validar_placa(placa):

    """Devolve True se a placa esta no formato AAA-1234."""

    placa = placa.upper().strip()
    if len(placa) != 8:
        return False
    if placa[3] != "-":
        return False
    letras = placa[:3]
    numeros = placa[4:]
    if not letras.isalpha():
        return False
    if not numeros.isdigit():
        return False
    return True

def placa_ja_cadastrada(placa):
    
    """Verifica se uma placa já está cadastrada no sistema, retornando false, se nenhuma placa for encontrada"""
    
    for placas in veiculos:
        if placa == placas['placa']:
            return True
    
    return False   

def validar_limites_horario(horario):
    
    """Retorna True se a hora estiver entre 00 e 23, e o minuto estiver entre 00 e 59"""
    
    horas_string =  horario[:2]
    minutos_string = horario[3:]
    
    if not horas_string.isdigit():
        return False
    if not minutos_string.isdigit():
        return False
    
    horas_numero = int(horas_string)
    minutos_numero = int(minutos_string)
    
    if horas_numero < 0 or horas_numero > 23  or minutos_numero < 0 or minutos_numero > 59:
        return False
            
    return True

def validar_horario(horario):
     
    """Devolve True se o horario está no formato HH:MM"""
    
    if len(horario) != 5:
        return False
    if horario[2] != ":":
        return False
    
    horas =  horario[:2]
    minutos = horario[3:]
        
    if not horas.isdigit():
        return False
    if not minutos.isdigit():
        return False
    return True
    
def calcular_valor(placa, horario_saida):
    
    """Faz o calculo da cobrança do carro ao sair do estacionamento"""
    
    minutos_totais = calcular_tempo_permanencia(placa, horario_saida)
    
    if minutos_totais <= 60:
        return 5
    
    minutos_adicionais = minutos_totais - 60
    
    tempo_adicional = 15
    valor_adicional = 2
    while True:
        if minutos_adicionais <= tempo_adicional:
            return 5 + valor_adicional
        
        tempo_adicional += 15
        valor_adicional += 2
   
def calcular_tempo_permanencia(placa, horario_saida):
    
    """Calcula o tempo total de permanencia de um veiculo no estacionamento, retornando o este tempo em minutos"""
    
    veiculo = buscar_veiculo(placa)
    
    horario_entrada = veiculo['entrada']
    
    horas_entrada = int(horario_entrada[:2])
    minutos_entrada = int(horario_entrada[3:])
    
    horas_saida = int(horario_saida[:2])
    minutos_saida = int(horario_saida[3:])
    
    return (60 * horas_saida + minutos_saida) - (60 * horas_entrada + minutos_entrada)
    
def cadastrar_veiculo(placa, horario_entrada, tipo_veiculo):
    
    """Cadastra um veiculo no estacionamento e retorna o numero da vaga em que foi estacionado"""
    
    if tipo_veiculo != "carro" and tipo_veiculo != "moto":
        tipo_veiculo = "carro"
    
    vagas_ocupadas = retornar_vagas_ocupadas()
    
    for i in range(CAPACIDADE_MAXIMA):
        if i + 1 not in vagas_ocupadas:
            vaga = i + 1
            break
    
    veiculo = {"placa": placa, 
               "entrada": horario_entrada, 
               "vaga": vaga,
               "tipo": tipo_veiculo,}
    
    veiculos.append(veiculo)
    return vaga

def remover_veiculo(placa):
    
    """Faz a remoção de um dicionario ou veiculo da lista 'veiculos'"""
    
    veiculo = buscar_veiculo(placa)
    veiculos.remove(veiculo)

def buscar_veiculo(placa):
    
    """Retorna um veiculo especifico da lista 'veiculos' onde estão todos os veiculo"""
    
    for veiculo in veiculos:
        if placa == veiculo['placa']:
            return veiculo      
        
def listar_veiculos():
    
    """Exibi na tela todos os veiculos estacionados e suas informções"""
    
    if len(veiculos) == 0:
        print("Nenhum veiculo estacionado.")
    else:
        for veiculo in veiculos:
            print(f"Placa: {veiculo['placa']}")
            print(f"Horario de entrada do veiculo: {veiculo['entrada']}")
            print(f"Veiculo estacionado na vaga: {veiculo['vaga']}")
            print(f"Tipo: {veiculo['tipo']}")
            print()    
        
def consultar_vagas():
    
    """Faz um print de todas as vagas disponiveis no estacionamento """
    
    vagas_ocupadas = []
    
    for vagas in veiculos:
            vagas_ocupadas.append(vagas['vaga'])
    
    for i in range(CAPACIDADE_MAXIMA):
        if i+1 not in vagas_ocupadas:
            print(f"Vaga {i+1} disponivel")

def retornar_vagas_ocupadas():
    
    """Retorna uma lista com quais vagas estão ocupadas"""
    
    vagas_ocupadas = []
    
    for vagas in veiculos:
            vagas_ocupadas.append(vagas['vaga'])
            
    return vagas_ocupadas
        
def validar_estacionamento_lotado():
    
    """ Verifica se o estacionamento atingiu a capacidade máxima """
    
    if len(veiculos) == CAPACIDADE_MAXIMA:
        return True
    else:
        return False
    
def main():

    """Controla o menu do sistema de estacionamento"""
    
    while True:
        print("========================================")
        print("  ESTACIONAMENTO - MENU")
        print("========================================")

        print("1 - Entrada do veiculo")
        print("2 - Saida de veiculo")
        print("3 - Listar Veiculos estacionados")
        print("4 - Consultar vagas")
        print("0 - Encerrar")
        
        opcao = input("Escolha uma opcao: ")
       
        if opcao == "1":
            if validar_estacionamento_lotado():
                print("Estacionamento lotado. Nao foi possivel cadastrar.")
                continue
            placa = input("Placa(formato ABC-1234): ")
            if not validar_placa(placa):
                print("Placa invalida. Use o formato ABC-1234.")
                continue
            if placa_ja_cadastrada(placa):
                print("Essa placa ja esta cadastrada no estacionamento")
                continue

            horario_entrada = input("Horario de entrada (HH:MM): ")
            if not validar_horario(horario_entrada):
                print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
                continue
            if not validar_limites_horario(horario_entrada):
                print("Horario invalido. Hora entre 00 e 23, minuto entre 00 e 59.")
                continue
            
            tipo_veiculo = input("Tipo do veiculo (carro / moto): ")
            print(f"veiculo {placa} cadastrado na vaga", cadastrar_veiculo(placa, horario_entrada, tipo_veiculo))
            
        elif opcao == "2":
            placa = input("Placa do veiculo que esta saindo: ")
            if not validar_placa(placa):
                print("Placa invalida. Use o formato ABC-1234.")
                continue
            if not placa_ja_cadastrada(placa):
                print("Placa nao encontrada no estacionamento.")
                continue
            
            horario_saida = input("Horario de saida (HH:MM): ")
            if not validar_horario(horario_saida):
                print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
                continue
            if not validar_limites_horario(horario_saida):
                print("Horario invalido. Hora entre 00 e 23, minuto entre 00 e 59.")
                continue
            if not validar_horario_saida(placa ,horario_saida):
                print("O horario de saida nao pode ser anterior ao de entrada.")
                continue
            
            veiculo = buscar_veiculo(placa)
            permanencia = calcular_tempo_permanencia(placa, horario_saida)
            
            print(f"Placa: {veiculo['placa']}")
            print(f"Entrada: {veiculo['entrada']}")
            print(f"Saída: {horario_saida}")
            print(f"Permanencia: {permanencia} min")
            print(f"Total a pagar: R$ {calcular_valor(placa, horario_saida)},00")
            print(f"vaga {veiculo['vaga']} liberada.")
            
            remover_veiculo(placa)
            
        elif opcao == "3":
            listar_veiculos()
            
        elif opcao == "4":
            consultar_vagas()
            
        elif opcao == "0":
            break
        else:
            print("Opcao invalida. Escolha um numero do menu")
            continue

if __name__ == "__main__":
    main()