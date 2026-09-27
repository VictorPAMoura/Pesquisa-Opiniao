print("--- Pesquisa de Satisfação TudoWeb ---")
excelente = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i + 1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")
    opiniao = int(input("Digite sua opinião: "))
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1
print("\n--- Resultado da Pesquisa ---")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
