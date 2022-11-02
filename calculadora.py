operacao = ""
finalizar = ""

while finalizar != "S":

    while operacao != "SOMA" or "SUBTRAÇÃO" or "MULTIPLICAÇÃO" or "DIVISÃO":
        print("Bem vindo a Calculadora básica")
        valor1 = float(input("Digite o valor 1: "))
        valor2 = float(input("Digite o valor 2: "))    
            
        operacao = str(input("Qual operação deseja usar? \n [SOMA - SUBTRAÇÃO - MULTIPLICAÇÃO - DIVISÃO] "))
        operacao = operacao.upper()

        if operacao == "SOMA":
            result = valor1 + valor1
            print("Resultado da conta foi: {}".format(result))
            break        

        elif operacao == "SUBTRAÇÃO":
            result = valor1 - valor2
            print("Resultado da conta foi: {}".format(result))
            break       

        elif operacao == "MULTIPLICAÇÃO":
            result = valor1 * valor2
            print("Resultado da conta foi: {}".format(result))
            break        

        elif operacao == "DIVISÃO":
            result = valor1 / valor2
            print("Resultado da conta foi: {}".format(result))
            break

    finalizar = input("deseja finalizar a tarefa? [S / N] ")
    finalizar = finalizar.upper()
print("tarefa finalizada! \n OBRIGADO!!")
print("isso foi AGORA NO VS CODE")