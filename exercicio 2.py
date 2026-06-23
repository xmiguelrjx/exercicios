#  nota do aluno

nota1 = input("digite a primeira nota: ").replace(",",".")
nota2 = input("digite a segunda nota: ").replace(",",".")
nota3 = input("digite a terceira nota: ").replace(",",".")
nota4 = input("digite a quarta nota: ").replace(",",".")

# calculo da media
media = (float(nota1) + float(nota2) + float(nota3) + float(nota4)) / 4

# resultado
print(f" a media do aluno é {media}")

if media >=5:
    print("o aluno foi aprovado")
else:
    print("o aluno foi reprovado")