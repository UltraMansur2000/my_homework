import re


def email_parse(email):
    match = re.split(r'[@]', f'{email}')
    if re.fullmatch(r'\w+\.\w+', match[1]) is not None:
        return {'name': match[0], 'domain': match[1]}
    else:
        raise ValueError(f'wrong email: {email}')


print(email_parse('igorek.abdulov@mail.ru'))