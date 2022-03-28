'''

message = "Hello Python World!"
print(message) #imprime no ecrã a menssagem

name = "Ada lovelace"
print(name.title()) #primeira letra de cada palavra em maiuscula
print(name.upper()) #toda a string em maiusculas
print(name.lower()) #toda a string em minusculas

first_name = "Ada"
last_name = "Lovelace"
print (first_name + " " + last_name) #contatenação de strings

print ("Hello\nPython World!") #quebra de linha \n 
print ("Hello\tPython World") #tabulação 

last_name = " Lovelace "
print(last_name.lstrip()) #remove espaços em branco à esquerda
print(last_name.rstrip()) #remove espaços em branco à direita
print(last_name.strip()) #remove espaços em branco à direita e à esquerda ao mesmo tempo

idade = 25
print ("a minha idade é " + str(idade)) #a concatenaçao so funciona com string caso pretendemos usar numbers _
temos que fazer um casting 

bycicles = ['trek','cannondale','redline','specialized']
print(bycicles[2]) #retorna o terceiro elemento da lista, a lista começa sempre do zero
bycicles[1] = "canyon" #altera o valor do elemento correspondente da lista
bycicles.insert(2, "honda") #insere na posição 2 o valor movendo todos os seguintes uma posição
bycicles.append("iba") #adiciona na ultima posição o elemento
print(bycicles[1]) #imprime o valor do elemento solicitado
print(bycicles[-1]) #imprime o ultimo elemento da lista
del bycicles[0] #remove o elemento desejado.
bycicles.remove("redline") #remove indicando o valor e nao a posição
bycicles.sort() #ordena de forma crescente e é permanente
print(sorted(bycicles)) #ordena de forma crescente sem alterar a lista
bycicles.sort(reverse=True) #ordena de forma decrescente e é permanente
print(bycicles.reverse()) #nao organiza a lista só inverte a lista
print(bycicles) #imprime toda a lista
print(len(bycicles))
'''
bycicles = ['trek','cannondale','redline','specialized']

for bike in bycicles: 
    print(bike)




