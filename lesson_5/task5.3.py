tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Евгений', 'Александр', 'Михаил'
]
classes = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

a = ((tutors[i], classes[i]) if i < len(classes) else (tutors[i], None) for i in range(len(tutors)))
for i in range(len(tutors)+1):
    print(next(a))