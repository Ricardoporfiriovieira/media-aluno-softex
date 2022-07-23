def aprovadoOuReprovado(med, falt):
    if(med >= 7 and falt <= 3):
        return "Aprovado"
    return "Reprovado"

nome = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
faltas = int(input("Digite a quantidade de faltas do aluno: "))

print(f"O aluno {nome} está {aprovadoOuReprovado(media,faltas)}")

