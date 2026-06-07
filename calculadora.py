def somar (Numero1 , Numero2):
    soma = Numero1 + Numero2
    print(soma)
   
def subtrair (Numero1 , Numero2):
    subtracao = Numero1 - Numero2
    print(subtracao)
   
def multiplicar(Numero1 ,Numero2):
    multiplicacao = Numero1 * Numero2
    print(multiplicacao)
   
def dividir(Numero1, Numero2):
    try:
        divisao = Numero1 / Numero2
        print(divisao)
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")

   
while True :
   
    print('=== CALULADORA ===')


   
    try:
        Numero1 = float(input("Digite um numero : "))
       
    except ValueError:
        print("Digite Apenas Numeros")
        continue  
       
    operacao = str(input("Digite a Operação : (+, -, *, /): "))        
   
   
    try:
        Numero2 = float(input("Digite um numero : "))
       
    except ValueError:
        print("Digite Apenas Numeros")
        continue
    
    if operacao == '+':
            somar(Numero1 ,Numero2)            
           
    elif operacao == '-' :
            subtrair(Numero1 ,Numero2)            
           
    elif operacao == '*':
            multiplicar(Numero1 ,Numero2)              
           
    elif operacao == '/':
            dividir(Numero1 ,Numero2)    
            
    else:
        print("Operação inválida! Use +, -, * ou /")
        continue

    continuar = input("Deseja fazer outra operação? (s/n): ")
    if continuar == "n":
        print("Encerrando Programa...")
        break
