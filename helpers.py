import random
import string


def generate_login():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(3, 10)))
    domains = ['yandex.ru', 'mail.ru', 'gmail.com', 'yahoo.com', 'hotmail.com']
    random_domain = random.choice(domains)
    email = f'test_{random_string}@{random_domain}'
    return email


def generate_password():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(6, 10)))
    return random_string


def generate_incorrect_password():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1, 5)))
    return random_string
