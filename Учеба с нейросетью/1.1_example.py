def calculate_bmi(weight, height): #рассчитывает индекс массы тела (ИМТ)
    if weight >=0 and height>0:
        bmi=weight/((height/100)**2)
        return bmi
    else: return None

def get_bmi_category(bmi): #проверка диапазона ИМТ
    if bmi < 18.5:
        return 'Недостаточный вес'
    elif 18.5 <= bmi < 25: 
        return 'Норма'
    else: 
        return 'Избыточный вес'

name='Mikhail'
age=22
height=178.5
weight=72
print(f'Привет, {name}!\nТебе {age} лет, и твой рост \u2014 {int(height)} см, а вес \u2014 {weight} кг.')
#проверка диапазона возраста
if age<18: print('Ты еще молод!')
else: print('Ты уже взрослый!')
bmi=calculate_bmi(weight, height)
if bmi is not None:
    print(f'Ваш ИМТ: {bmi:.1f}')
    category=get_bmi_category(bmi)
    print(category)
else: print('Ошибка, неверные данные')