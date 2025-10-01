ano_nascimento = int(input("digiter o ano em que voce nasceu:"))
ano_atual = 2025
idade = ano_atual - ano_nascimento
if idade == 18:
    print("voce faz 18 anos neste ano!")
elif idade > 18: 
  print("voce fez 18 anos")
else:
  print("voce ainda nao fez 18 anos")  