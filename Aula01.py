import os
os.system("cls||clear")
valor=float(input("Digite um Valor inteiro: "))
print(f"O Antercessor é: {valor-1}")
print(f"O Sucessor é: {valor+1}")
print(f"A raiz qnuadrada È: {valor**(1/2):.1f}")
if (valor%2==0):
    resultado="Par"
else:
    resultado="Impar"
print(f"o Valor é: {resultado} ")    
if (valor>=0 and valor<11):
    resposta="Valor é Válido"
else:
    resposta="Valor não é Valido"
print(resposta)