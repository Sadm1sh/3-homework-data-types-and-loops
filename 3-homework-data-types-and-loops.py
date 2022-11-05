#Задание №1
boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()
if (len(boys)) == (len(girls)) :
    for name, numder in zip(boys, girls):
        print(name, numder, sep = ' и ')
else:
    print('Кто-то может остаться без пары!!!')
#Задание №2
cook_book = [
  ['cалат',
      [
        ['картофель', 100, 'гр.'],
        ['морковь', 50, 'гр.'],
        ['огурцы', 50, 'гр.'],
        ['горошек', 30, 'гр.'],
        ['майонез', 70, 'мл.'],
      ]
  ],
  ['пицца',
      [
        ['сыр', 50, 'гр.'],
        ['томаты', 50, 'гр.'],
        ['тесто', 100, 'гр.'],
        ['бекон', 30, 'гр.'],
        ['колбаса', 30, 'гр.'],
        ['грибы', 20, 'гр.'],
      ],
  ],
  ['фруктовый десерт',
      [
        ['хурма', 60, 'гр.'],
        ['киви', 60, 'гр.'],
        ['творог', 60, 'гр.'],
        ['сахар', 10, 'гр.'],
        ['мед', 50, 'мл.'],
      ]
  ]
]
# Запрос на кол-во персон
person = int(input('Введите кол-во персон:'))
for dish, ingridient in cook_book:
    print(f'{dish}:'.capitalize())
    for ingr in ingridient:
        weight = int(ingr[1]) * person
        print(ingr[0], ' ',weight, ingr[2], sep='')
    print()