"""
Desafio 5 - Listas

Neste desafio, vamos receber dois números que deverar ser informado pelo o usuário.
E armazenar os resultados em uma lista.

Em seguida vamos imprimir a soma, a subtração, a multiplicação e divisão e a
exponenciação (primerio número eleado ao segundo número).



"""
#Entrada
num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))


#Lista
resultados = [f"Soma: {num1 + num2}", f"Subtração: {num1 - num2}",
              f"multiplicação:{num1 * num2}", f"Divisão: {num1/num2}",
              f"Potencia:{num1**num2}"]

#Saida
print(f"Resultados: {resultados}")