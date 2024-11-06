from garbage_collection import*

bird_1=songbird('Koko', 'tweet, tweet!\n')
print(bird_1.name, 'ID:', id(bird_1))
bird_1.sing()

del bird_1

bird_2=songbird('Louie', 'Chirp, chirp!\n')
print(bird_2.name, 'ID:', id(bird_2))
bird_2.sing()
bird_3=songbird('Misty', 'Squawk, squawk!\n')
print(bird_3.name, 'ID:', id(bird_3))
bird_3.sing()

del bird_2
del bird_3
'''здесь: self - имя класса. Оно в __init__. Там же прописываем
в скобках имя и как поет. Потом обычная ффункция.
И функция del - просто пишет нам что-то'''