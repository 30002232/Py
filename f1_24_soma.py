'''
24) Leia do STDIN os valores A, B e C.
Mostre uma mensagem que informe se a soma de A com B é menor,
maior ou igual a C.
''' 

a = int(input('insira o valor de A:\n'))
b = int(input('insira o valor de B:\n'))
c = int(input('insira o valor de C:\n'))

soma = a + b
if(soma > c):
    print("A soma de A com B é maior que C")
elif(soma < c):
    print("A soma de A com B é menor que C")
else:
    print("A soma de A com B é igual que C")
