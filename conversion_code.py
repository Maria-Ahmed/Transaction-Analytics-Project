import csv


def read_file(filename):
    rows = []
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        #headers = reader.fieldnames

        for row in reader:
            rows.append(row)
        return rows

transactions = read_file('transactions.csv')
users = read_file('users.csv')

def user_is_inactive(user_id):
    for user in users:
        if user_id == user["user_id"]:
            if user["is_active"] == "False":
                return True
            else:
                return False

transaction_category = {}
for transaction in transactions:
    if transaction['is_blocked'] == "True":
        continue
    if user_is_inactive(transaction['user_id']):
        continue

    category = transaction_category.get(transaction['transaction_category_id'], {'sum_amount': 0, 'num_users': 0, 'users': set()})
    print(category)
    transaction_category[transaction['transaction_category_id']] = {
        'sum_amount': int(category['sum_amount']) + int(transaction['transaction_amount']), 
        'users': category['users'] | {transaction['user_id']}
    }

for category, value in transaction_category.items():
    transaction_category[category]['num_users'] = len(transaction_category[category]['users'])
    del transaction_category[category]['users']

print(transaction_category)


