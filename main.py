#Homework2

import random
import string
import pan
def generate_password():
    length = random.randint(10, 20)

    password = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    return password
def calculate_average(file_path):
    data = pd.read_csv(file_path)

    average_height = data['height'].mean()
    average_weight = data['weight'].mean()

    return average_height, average_weight
#Приклад
generated_password = generate_password()
print("Сгенерированный пароль:", generated_password)

# Приклад
file_path = "students.csv"
average_height, average_weight = calculate_average(file_path)
print("Средний рост студентов:", average_height)
print("Средний вес студентов:", average_weight)