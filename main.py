nomes = ["Eduardo", "Brian", "Gabriel"]
encontrado = False
 
nomeProcurado = input("Digite o nome para verificar: ")

for i in range(0, 2):
    if nomeProcurado == nomes[i]:
        encontrado = True
        break
    
if encontrado == True:
    print(f"{nomeProcurado} está na lista!")
else:
    print(f"{nomeProcurado} não está na lista!")


        
    
