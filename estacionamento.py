def validar_placa(placa):

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

def main():

    while True:
        print("=====================================")
        print("\tESTACIONAMENTO MENU")
        print("=====================================")

        print("1 - Entrada do veiculo")
        print("2 - Saida de veiculo")
        print("3 - Listar Veiculos estacionados")
        print("4 - Consultar vagas")
        print("5 - Encerrar")
        opcao = int(input("Escolha uma opção: "))