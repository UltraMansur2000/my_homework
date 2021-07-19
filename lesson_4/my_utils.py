from requests import get, utils
from decimal import Decimal

def currency_rates(value_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    values = content.replace('<Value>', '</Value>').split('</Value>')[1::2]
    char_code = content.replace('<CharCode>', '</CharCode>').split('</CharCode>')[1::2]

    value_code = value_code.upper()
    date = content[content.index('Date=') + 6:content.index('Date=') + 6 + 10]

    if value_code in char_code:
        return f"{Decimal(values[char_code.index(value_code)].replace(',', '.'))} {date} {value_code}"