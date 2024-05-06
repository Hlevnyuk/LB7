from pymongo import MongoClient

# Підключення до MongoDB
client = MongoClient('localhost', 27017)
db = client['lb5']  # Назва вашої бази даних

# Створення зразка даних
collection1 = db['collection1']
collection2 = db['collection2']

# Вставка даних у колекцію №1
collection1.insert_many([
    {"_id": 1, "name": "Alice", "friend": 101},
    {"_id": 2, "name": "Bob", "friend": 102},
    {"_id": 3, "name": "Charlie", "friend": 103},
    {"_id": 4, "name": "David", "friend": 104},
    {"_id": 5, "name": "Emma", "friend": 105},
])

# Вставка даних у колекцію №2
collection2.insert_many([
    {"_id": 101, "details": "Details of friend 101"},
    {"_id": 102, "details": "Details of friend 102"},
    {"_id": 103, "details": "Details of friend 103"},
    {"_id": 104, "details": "Details of friend 104"},
    {"_id": 105, "details": "Details of friend 105"},
])

# Параметри N, M та MAXK
N = 6
M = 8
MAXK = 10


# Функція для побудови ланцюжка документів
def build_chain(start_doc):
    chain = [start_doc]
    current_doc = start_doc
    chain_length = 0

    while current_doc.get('friend') and chain_length < MAXK:
        next_doc = collection2.find_one({'_id': current_doc['friend']})
        if next_doc:
            chain.append(next_doc)
            current_doc = next_doc
            chain_length += 1
        else:
            break

    return chain


# Запит для виведення перших N записів колекції №1
cursor1 = collection1.find().limit(N)

# Запит для виведення перших M записів колекції №2
cursor2 = collection2.find().limit(M)

# Виведення результатів
print(f"N = {N}, M = {M}")

for doc1 in cursor1:
    chain = build_chain(doc1)
    print("\nChain starting with document from collection1:")
    for doc in chain:
        print(doc)
