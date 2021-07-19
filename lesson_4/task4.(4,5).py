from my_utils import currency_rates
import sys

for char_code in sys.argv[1::]:
    print(currency_rates(char_code))