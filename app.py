import os
from equacao import*
if __name__ == "__main__":
    while True:
        print("0  Sair do programa.")
        print("1  calcular 1º grau.")
        print("2  calcular 2º grau.")

        opcao = input("Opção desejada: ")
        #limpeza de console
        os.system("cls") 

        match opcao:
            case "0":
                break
            case "1":
                try:
                    a = float(input("Informe o valor de a: ").replace(",", "."))
                    b = float(input("Informe o valor de b: ").replace(",", "."))
                    print(f"Valor de x: {primeiro_grau(a, b)}.")
                except Exception as e:
                    print(f"Não foi possível calcular a equação de primeiro grau. {e}.")
                finally:
                    continue
            
            
            
            
            
            
            
            case "2":
                try:
                    a = float(input("Informe o valor de 'a': ").replace(",", "."))
                    b = float(input("Informe o valor de 'b': ").replace(",", "."))
                    c = float(input("Informe o valor de 'c': ").replace(",", "."))
                    
                    #armazena os valores da funçaõ
                    resultados = list(segundo_grau(a, b, c))
                    for resultado in resultados:
                        print(resultado)
                except Exception as e:
                    print(f"Não foi possível calcular a equação de segundo grau. {e}.")
                finally:
                    continue
            case _:
                print("Opção inválida. Tente novamente.")
                continue

               