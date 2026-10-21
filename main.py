def calcular_media(notas):
    return sum(notas) / len(notas)

def classificar(media):
    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
    
notas = []

for i in range(3):
    valor = float(input(f"Digite a nota {i + 1}: "))
    notas.append(valor)
    
media = calcular_media(notas)
print(f"Notas: {notas}")
print(f"Média: {media:.2f}")
print(f"Situação: {classificar(media)}")