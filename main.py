#homework3
import pandas as pd
import requests


def generate_students(count=1000):
    student_data = {
        'first_name': ['John', 'Jane', 'Alice', 'Bob'],
        'last_name': ['Doe', 'Smith', 'Johnson', 'Brown'],
        'email': ['john.doe@gmail.com', 'jane.smith@gmail.com', 'alice.johnson@gkamil.com',
                  'bob.brown@gmail.com'],
        'password': ['aesrdtf1', 'esxrdcftvg2', 'easrdtfg3', 'sxrcfygv4'],
        'birthday': ['1990-01-01', '1995-03-15', '1988-07-20', '1992-11-30']
    }
    df = pd.DataFrame(student_data)

    df.to_csv('students.csv', index=False)

    return df.head(count).to_html(index=False)


def get_bitcoin_value(currency='USD', count=1):
    url = f'https://bitpay.com/api/rates/bitcoin_rate?currency={currency}&convert={count}'
    response = requests.get(url)
    bitcoin_value = response.json()['data']['rate']

    currency_symbol = response.json()['data']['symbol']

    bitcoin_value *= count

    return f'{currency_symbol} {bitcoin_value}'