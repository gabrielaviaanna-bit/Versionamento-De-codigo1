ano = int(input("Em que ano você nasceu? "))
idade = 2025 - ano
if idade == 18:
    print("Você está fazendo 18 anos este ano!")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda vai fazer 18 anos.")