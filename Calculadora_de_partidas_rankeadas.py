''' 2 Calculadora de partidas Rankeadas
**O Que deve ser utilizado**

- Variáveis
- Operadores
- Laços de repetição
- Estruturas de decisões
- Funções

## Objetivo:

Crie uma função que recebe como parâmetro a quantidade de vitórias e derrotas de um jogador,
depois disso retorne o resultado para uma variável, o saldo de Rankeadas deve ser feito através do calculo (vitórias - derrotas)

Se vitórias for menor do que 10 = Ferro
Se vitórias for entre 11 e 20 = Bronze
Se vitórias for entre 21 e 50 = Prata
Se vitórias for entre 51 e 80 = Ouro
Se vitórias for entre 81 e 90 = Diamante
Se vitórias for entre 91 e 100= Lendário
Se vitórias for maior ou igual a 101 = Imortal

## Saída

Ao final deve se exibir uma mensagem:
"O Herói tem de saldo de **{saldoVitorias}** está no nível de **{nivel}**" '''

nome = input("Qual é seu nome? ")

calculadora = input("Olá, gostaria de calcular seu ranque? [s/n] ").lower()

def calculo():
    vitorias = int(input("Quantas vitórias você possui? "))
    derrotas = int(input("Quantas derrotas você possui? "))

    saldoVitorias = vitorias - derrotas

    if saldoVitorias <= 10:
        nivel = "Ferro"
    elif 11 <= saldoVitorias <= 20:
        nivel = "Bronze"
    elif 21 <= saldoVitorias <= 50:
        nivel = "Prata"
    elif 51 <= saldoVitorias <= 80:
        nivel = "Ouro"
    elif 81 <= saldoVitorias <= 90:
        nivel = "Diamante"
    elif 91 <= saldoVitorias <= 100:
        nivel = "Lendario"
    else:
        nivel = "Imortal"

    mensagem = print(f"O Herói {nome} tem um saldo de {saldoVitorias} vitórias e está no nível {nivel}")
    return mensagem

while calculadora[0] == "s":
    calculo()
    repetir = input("Deseja realizar uma nova consulta? ").lower()
    if repetir[0] != "s":
        break