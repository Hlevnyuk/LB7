import pymongo
from pymongo import MongoClient
import random

# З'єднання з MongoDB
client = MongoClient('localhost', 27017)
db = client['test_database']

# Створення колекцій
collection1 = db['collection1']
collection2 = db['collection2']

# Функція для створення випадкового _id
def generate_random_id():
    return random.randint(1001, 2000)  # випадкове _id після 1000

# Створення записів у першій колекції з посиланнями на документи у другій колекції
for i in range(2000):
    document = {
        '_id': i + 1,  # починаючи з 1
        'counter': i,
        'name': f'name_{i}'  # поле name
    }
    # Випадкове _id документа з другої колекції
    if i >= 999:  # вставляємо випадкові _id після 1000 елемента
        document['ref_id'] = generate_random_id()
    collection1.insert_one(document)

# Створення записів у другій колекції з посиланнями на документи у першій колекції
for i in range(2000):
    document = {
        '_id': i + 1001,  # починаючи з 1001
        'counter': i,
        'name': f'name_{i}'  # поле name
    }
    # Випадкове _id документа з першої колекції
    if i >= 999:  # вставляємо випадкові _id після 1000 елемента
        document['ref_id'] = random.randint(1, 1000)  # випадкове _id з першої колекції
    collection2.insert_one(document)

print("Колекції створені успішно.")
