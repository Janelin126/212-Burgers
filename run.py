from flask import Flask, render_template, g
import sqlite3

app = Flask(__name__)

MENUDB = 'menu.db'

def fetchMenu(con):
    burgers = []
    free = '0'
    cur = con.execute('SELECT burger,price FROM burgers WHERE price>=?', (free,))
    for row in cur:
        burgers.append(list(row))

    drinks = []
    cur = con.execute('SELECT drink,price FROM drinks')
    for row in cur:
        drinks.append(list(row))

    sides = []
    cur = con.execute('SELECT side,price FROM sides')
    for row in cur:
        sides.append(list(row))

    return {'burgers':burgers, 'drinks':drinks, 'sides':sides}

burgers = [
 ['Classic Burger', '$4.99'],
 ['Cheese Burger', '$5.99'],
 ['Chicken Burger', '$5.99'],
 ['Double Burger', '$6.99']
]
drinks = [
  ['Cola', '$0.99'],
  ['Ginger Ale', '$0.99'],
  ['Beer', '$1.99'],
  ['Coffee', '$1.99']
]
sides = [
   ['Fries', '$1.99'],
   ['Onion Rings', '$1.99'],
   ['Mushrooms', '$1.99'],
   ['Salad', '$1.99']
]
@app.route('/')
def index():
    con = sqlite3.connect(MENUDB)
    menu = fetchMenu(con)
    con.close()

    db = sqlite3.connect(MENUDB)
    print(db)

    cur = db.execute('SELECT burger,price FROM burgers')
    for row in cur:
        print(row)

    return render_template(
                           'index.html',
                           disclaimer='may contain nuts',
                           burgers=menu['burgers'],
                           drinks=menu['drinks'],
                           sides=menu['sides'])


@app.route('/order')
def order():
    con = sqlite3.connect(MENUDB)
    menu = fetchMenu(con)
    con.close()

    con = sqlite3.connect(MENUDB)

    burgers = []
    free = '0'
    cur = con.execute('SELECT burger,price FROM burgers WHERE price>=?', (free,))
    for row in cur:
        burgers.append(list(row))


    drinks = []
    cur = con.execute('SELECT drink, price FROM drinks')
    for row in cur:
        drinks.append(list(row))


    sides = []
    cur = con.execute('SELECT side, price FROM sides')
    for row in cur:
        sides.append(list(row))

    con.close()

    return render_template('order.html', burgers=menu['burgers'], drinks=menu['drinks'], sides=menu['sides'])

@app.route('/confirm')
def confirm():
    return render_template('confirm.html')
