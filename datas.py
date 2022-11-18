import json

datas = {}
def load_data():
    with open('Coins.json','r') as coins:
        datas['Coins'] = json.loads(coins.read())
    with open('Admins.json','r') as admins:
        datas['Admins'] = json.loads(admins.read())
    
def save_data():
    f = open('Coins.json','w')
    
    f.write(json.dumps(datas['Coins'],indent=4))
    f.close()
def add_coin(user,amount):
    load_data()
    if str(user) in datas['Coins']:
        datas['Coins'][str(user)] += amount
    else:
        datas['Coins'][str(user)] = 0
    save_data()
def get_coin(user):
    if str(user) in datas['Coins']:
        return datas['Coins'][str(user)]
    else:
        datas['Coins'][str(user)] = 0
        save_data()
        return 0 
    
load_data()