# Sistema de Controle de Estacionamento

## Integrantes

* Maurício Tolosa
* Integrante 2
* Integrante 3

## Como Rodar o Programa

Certifique-se de ter o Python 3 instalado.

No terminal, execute:

```bash
python estacionamento.py
```

ou

```bash
python3 estacionamento.py
```

## Funções Implementadas

### Validação

* validar_placa()
* validar_horario()
* validar_limites_horario()
* validar_horario_saida()
* placa_ja_cadastrada()
* validar_estacionamento_lotado()

### Manipulação de Veículos

* cadastrar_veiculo()
* remover_veiculo()
* buscar_veiculo()
* listar_veiculos()
* consultar_vagas()
* retornar_vagas_ocupadas()

### Cálculos

* calcular_tempo_permanencia()
* calcular_valor()

### Controle do Sistema

* main()

## Decisões de Projeto

* Capacidade máxima definida como 10 vagas.
* Veículos armazenados em uma lista de dicionários.
* Tipos aceitos: carro e moto.
* Caso seja informado um tipo diferente, o sistema registra como carro.
* Os dados são mantidos apenas em memória durante a execução do programa.
* As vagas são atribuídas automaticamente utilizando a primeira vaga livre disponível.
