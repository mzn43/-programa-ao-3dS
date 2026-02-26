idade = 16
classificacao = "R"

if classificacao == "G":
    print("Permitido para todas as idades.")
elif classificacao == "PG" and idade >= 10:
    print("Permitido para crianças com mais de 10 anos.")
elif classificacao == "PG-13" and idade >= 13:
    print("Permitido para adolescentes com mais de 13 anos.")
elif classificacao == "R" and idade >= 17:
    print("Permitido para maiores de 17 anos.")
else:
    print("Não permitido.")