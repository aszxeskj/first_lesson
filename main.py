print ("вашего героя окружила огромная армия троллей")
print("смрадными трупали устланы окрестные поля")
print("одинокий герой достает свой меч из ножен, готовясь к последней битве в своей жизни.\n")
health = 100
trolls = 0
damage = 3
while health != 0:
    trolls = trolls +1
    health = health - damage
    print("змахнув рукой ваш герой истребляет злобного тролля но сам получает повреждений на",damage," очков.\n")
    print("ваш герой доблестно сражался и убил",trolls,"троллей.")
    print("но увы он пал на поле боя.")
    input("\n\n нажмите ентер чтобы выйти")