from faker import Faker
import requests
import pandas as pd
import random
import string


def get_requirements():
    with open('requirements.txt') as f:
        file = f.read()
    return file


def get_password(length: int = 10) -> str:
    """
    generate password
    """

    password = ''
    chars = string.ascii_letters + string.digits + string.punctuation
    for _ in range(length):
        password += random.choice(chars)

    return password


def get_generate_users(length: int = 100):
    fake = Faker()
    generate_users = ''
    for _ in range(length):
        if _ != length - 1:
            a = f'{fake.first_name()} : {fake.email()}, '
        else:
            a = f'{fake.first_name()} : {fake.email()}'
        generate_users += a
    return generate_users


def get_space():
    r = requests.get('http://api.open-notify.org/astros.json')
    return r.json()["number"]


def get_mean():
    df = pd.read_csv('hw.csv')
    arg_height = df[' "Height(Inches)"'].mean()
    arg_weight = df[' "Weight(Pounds)"'].mean()
    return f'Average Height is {arg_height}, Average Weight is {arg_weight}'
