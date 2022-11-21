import json

datas = {}


def load_data():
    with open('Datas.json', 'r') as dats:
        return json.loads(dats.read())


def save_data():
    f = open('Datas.json', 'w')
    f.write(json.dumps(datas, indent=4))
    f.close()


def add_coin(user, amount):
    if str(user) in datas['Coins']:
        datas['Coins'][str(user)] += amount
    else:
        datas['Coins'][str(user)] = 0
    save_data()


def set_coin(user, amount):
    if str(user) in datas['Coins']:
        datas['Coins'][str(user)] = amount
    else:
        datas['Coins'][str(user)] = 0
    save_data()


def get_coin(user):
    if str(user) in datas['Coins']:
        save_data()
        return datas['Coins'][str(user)]
    else:
        datas['Coins'][str(user)] = 0
        save_data()
        return 0


def get_admin():
    return datas['Admins']


datas = load_data()
