import string
import os
import secrets

while True:
    print("|" + "=" * 5 + "[Passw0rd Generat0r]" + "=" * 5 + "|")
    option = input("1 - Gerar senha\n2 - Sair\nOpção: ")
    if option.isnumeric():
        option = int(option)
        if option == 1:
            qtd_caracteres = int(input("Quantidade de caracteres: "))
            print("Escolha a combinação\n")
            print("1 - Somente letras\n2 - Letras e numeros\n3 - Letras, numeros e simbolos\n")
            option_2 = input("Opção: ")
            if option_2.isnumeric():
                option_2 = int(option_2)
                if option_2 == 1:
                    caracteres = string.ascii_letters
                    senha = ''.join(secrets.choice(caracteres) for _ in range(qtd_caracteres))
                    os.system("cls")
                    print(f'Senha gerada: {senha}')
                elif option_2 == 2:
                    caracteres = string.ascii_letters + string.digits
                    senha = ''.join(secrets.choice(caracteres) for _ in range(qtd_caracteres))
                    os.system("cls")
                    print(f'Senha gerada: {senha}')
                elif option_2 == 3:
                    caracteres = string.ascii_letters + string.digits + string.punctuation
                    senha = ''.join(secrets.choice(caracteres) for _ in range(qtd_caracteres))
                    os.system("cls")
                    print(f'Senha gerada: {senha}')
            else:
                print("Ops.. informe apenas o NUMERO da opção!")
        else:
            print("Encerrando..")
            break
