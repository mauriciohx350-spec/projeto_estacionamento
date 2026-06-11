veiculos = []
CAPACIDADE_MAXIMA = 10

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
    
    for placas in veiculos:
        if placa == placas['placa']:
            return True
    
    return False   

def validar_limites_horario(horario):
    
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
    
def calcular_valor(minutos): pass

def cadastrar_veiculo(placa, horario_entrada, tipo_veiculo):
    
    if tipo_veiculo != "carro" and tipo_veiculo != "moto":
        tipo_veiculo = "carro"
    
    VAGA_CONTAGEM = len(veiculos) + 1
    veiculo = {"placa": placa, "entrada": horario_entrada, "vaga": VAGA_CONTAGEM,"tipo": tipo_veiculo,}
    veiculos.append(veiculo)
    return VAGA_CONTAGEM

def remover_veiculo(placa, horario_saida):
    
    for veiculo in veiculos:
        if veiculo['placa'] == placa:
            veiculos.remove(veiculo)
        
def listar_veiculos():

    for veiculo in veiculos:
        print(f"Placa: {veiculo['placa']}")
        print(f"Horario de entrada do veiculo: {veiculo['entrada']}")
        print(f"Veiculo estacionado na vaga: {veiculo['vaga']}")
        print(f"Tipo: {veiculo['tipo']}")
        print()    
    
def consultar_vagas(): pass
        
    

def main():

    while True:
        print("=========================================")
        print("\tESTACIONAMENTO MENU")
        print("=========================================")

        print("1 - Entrada do veiculo")
        print("2 - Saida de veiculo")
        print("3 - Listar Veiculos estacionados")
        print("4 - Consultar vagas")
        print("0 - Encerrar")
        
        opcao = input("Escolha uma opcao: ")
       
        if opcao == "1":
            placa = input("Placa(formato ABC-1234): ")
            if not validar_placa(placa):
                print("Placa invalida. Use o formato ABC-1234.")
                continue
            if placa_ja_cadastrada(placa):
                while placa_ja_cadastrada(placa) or not validar_placa(placa):
                    if not validar_placa(placa):
                        print("Placa invalida. Use o formato ABC-1234.")
                    elif placa_ja_cadastrada(placa):
                        print("Essa placa ja esta cadastrada no estacionamento.")
                    placa = input("Placa(formato ABC-1234): ")
    
            horario_entrada = input("Horario de entrada (HH:MM): ")
            while not validar_horario(horario_entrada) or not validar_limites_horario(horario_entrada):
                if not validar_horario(horario_entrada):
                    print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
                elif not validar_limites_horario(horario_entrada):
                    print("Horario invalido. Hora entre 00 e 23, minuto entre 00 e 59.")
                horario_entrada = input("Horario de entrada (HH:MM): ")
            
            tipo_veiculo = input("Tipo do veiculo (carro / moto): ")
            print(f"veiculo {placa} cadastrado na vaga", cadastrar_veiculo(placa, horario_entrada, tipo_veiculo))
            
        elif opcao == "2":
            placa = input("Placa do veiculo que esta saindo: ")
            if not validar_placa(placa):
                while True:
                    placa = input("Placa invalida. Use o formato ABC-1234: ")
                    if validar_placa(placa):
                        break
                    
            horario_saida = input("Horario de saida (HH:MM): ")
            while not validar_horario(horario_saida) or not validar_limites_horario(horario_saida):
                if not validar_horario(horario_saida):
                    print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
                elif not validar_limites_horario(horario_saida):
                    print("Horario invalido. Hora entre 00 e 23, minuto entre 00 e 59.")
                horario_saida = input("Horario de saida (HH:MM): ")
            
            remover_veiculo(placa, horario_saida)
            
        elif opcao == "3":
            listar_veiculos()
            
        elif opcao == "4": pass
            
        elif opcao == "0":
            break
        else:
            print("Opcao invalida. Escolha um numero do menu")

if __name__ == "__main__":
    main()