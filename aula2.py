#Lista

lista = ["Neto","Priscila","Alícia","Geo"]

print(lista[2]+" e fulano sairam com "+ lista[1])
print(lista[3])

#imprimir uma sequência de strings

print(lista[0:4]) #aqui ele vai imprimir do item 0 ate o item 4

#para selecionar de trás para frente basta inserir valores negativos

print(lista[-4])  #ele começa a contar do último

#provando o tópico anterior através das condicionais if e else

if  (lista[-4]) == (lista[0]) :
    print("você entendeu como funciona a lista")
else:
    print("o item -4 náo e igual o item 0")

lista.append("Miguel") #Adiciona item a lista
idades = [12,34,23,45,42,12,42,32,66]

print(lista) 
print(idades)