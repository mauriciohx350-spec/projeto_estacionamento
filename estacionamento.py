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

def validar_horario(horario):
     
     if len(horario) != 5:
         return False
     if horario[2] != ":":
        return False
     horas = horario[:2]
     minutos = horario[3:]
    
     if not horas.isdigit():
         return False
     if not minutos.isdigit():
         return False
     if horas < 0 or horas > 23:
         return False
     if minutos < 0 or minutos > 59:
         return False
     return True


def calcular_valor(minutos): pass



def cadastrar_veiculo(veiculos): pass

def remover_veiculo(veiculos): pass

def listar_veiculos(veiculos): pass

def consultar_vagas(veiculos): pass

def main():

    while True:
        print("="*40)
        print("\tESTACIONAMENTO MENU")
        print("="*40)

        print("1 - Entrada do veiculo")
        print("2 - Saida de veiculo")
        print("3 - Listar Veiculos estacionados")
        print("4 - Consultar vagas")
        print("0 - Encerrar")
        
        opcao = int(input("Escolha uma opcao: "))
        
        while opcao !=1!=2!=3!=4!=0:
            if opcao !=1!=2!=3!=4!=0:
                opcao = int(input("Opcao invalida. Escolha um numero do menu: "))
            else:
                break
            
        if opcao == 1:
            placa = input("Placa(formato ABC-1234): ")
            if validar_placa(placa) == False:
                while True:
                    placa = input("Placa invalida. Use o formato ABC-1234: ")
                    if validar_placa(placa) == True:
                        break
                    
            horario_entrada = input("Horario de entrada (HH:MM): ")
            if validar_horario(horario_entrada) == False:
                while True:
                    horario_entrada = input("Horario invalido. Use o formato HH:MM (exemplo 08:30): ")
                    if validar_horario(horario_entrada) == True:
                        break
            
            tipo = input("Tipo do veiculo (carro / moto): ")
            
            
        
main()