nome = ""
xp = 2

if xp <= 1000:
    nivel = "ferro"
elif xp >= 1001 and xp <= 2000:
    nivel = "bronze"
elif xp >= 2001 and xp <= 5000:
    nivel = "prata"
elif xp >= 5001 and xp <= 7000:
    nivel = "ouro"
elif xp >= 7001 and xp <= 8000:
    nivel = "platina"
elif xp >= 8001 and xp <= 9000:
    nivel = "Ascendente"
elif xp >= 9001 and xp <= 10000:
    nivel = "imortal"
else:
    nivel = "Radiante"

print(f'o Herói {nome} está no nível de {nivel}')