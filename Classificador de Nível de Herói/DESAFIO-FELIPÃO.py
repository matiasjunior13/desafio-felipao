personagem = input('Nome do personagem:')
xp = int(input('Digite a quantidade de XP do seu personagem:'))

if xp < 1000 : 
    print('O Herói de nome', personagem, ' está no nível de Ferro')
elif xp >= 1001 and xp <= 2000: 
    print('O Herói de nome', personagem, ' está no nível de Bronze')
elif xp >= 2001 and xp <= 5000: 
    print('O Herói de nome', personagem, ' está no nível de Prata')
elif xp >= 6001 and xp <= 7000: 
    print('O Herói de nome', personagem, ' está no nível de Ouro')
elif xp >= 7001 and xp <= 8000: 
    print('O Herói de nome', personagem, ' está no nível de Platina')
elif xp >= 8001 and xp <= 9000: 
    print('O Herói de nome', personagem, ' está no nível de Ascendente')
elif xp >= 9001 and xp <= 10000: 
    print('O Herói de nome', personagem, ' está no nível de Imortal')
else: xp >= 100
