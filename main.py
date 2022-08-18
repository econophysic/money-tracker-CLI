import sqlite3
from datetime import date
import re
# from utils import check_credential

db = sqlite3.connect('moneyKeeper.db')
sql = db.cursor()


options = {
    0: 'Exiting the program',
    1: 'FOOD & DRINKS',
    2: 'SHOPPING',
    3: 'HOUSEHOLD',
    4: 'TRANSPORTATION',
    5: 'VEHICLE',
    6: 'INVESTMENT',
    7: 'OTHER',
    8: 'Show Statement',
    9: 'Change user account',
    321: 'Delete All Data '
}



def menu():
    print('Welcome to MoneyKeeper!')

    print('1. Login in')
    print('2. Sign in')
    print('3. Exit')
    print()
    menu_option = int(input('Choose an option: \n'))
    if menu_option == 1:
        login_in()
    elif menu_option == 2:
        sign_in()
    elif menu_option == 3:
        exit()


def main(userId, userName):
    print()
    print('1. Add Food & Drinks Expense')
    print('2. Add Shopping Expense')
    print('3. Add Household Expense')
    print('4. Add Transportation Expense')
    print('5. Add Vehicle Expense')
    print('6. Add Investment Expense')
    print('7. Add Other Expense')
    print('8. Show Statement ')
    print('9. Change user account ')
    print('0. Exit ')
    print('321. Delete All Data ')
    print()
    option = int(input('Choose an option: \n'))
    if option == 0:
        exit()

    elif option in range(1, 8):
        category = input(f'Enter the categories for expense type {options[option]}: ')
        price = int(input(f'Enter the price of the categories: '))
        price *= 1.0

        day = date.today()
        day = get_time(day)

        sql.execute(
            "INSERT INTO wallet(user_id, user_name, category, expense_type, price, dates) VALUES (?, ?, ?, ?, ?, ?)",
            (int(userId), userName, category, options[option], price, day))
        db.commit()
        main(userId, userName)
    elif option == 8:

        stat_answ = input('Show statistics for a period? Y/N ').upper()
        if stat_answ == 'Y':
            print('Enter the start date')
            start_date = correct_data()
            print()
            print('Enter the end date')
            end_date = correct_data()
            q_filter = f" WHERE dates BETWEEN '{start_date}' and '{end_date}'"
        elif stat_answ == 'N':
            q_filter = f" WHERE user_id ='{userId}'"

        q_select = f"SELECT user_id, user_name, expense_type, strftime('%d', dates) AS Day, strftime('%m', dates) AS Month, strftime('%Y', dates) AS Year, sum(price) FROM  wallet "
        q_gb_order = f" GROUP BY 1, 2, 3 ORDER BY 1, 2, 3 "
        query = q_select + q_filter + q_gb_order
       # print(query)
        show_statement(query)
        print()

    elif option == 9:
        menu()
    elif option == 321:
        sql.execute("DELETE FROM wallet")
        sql.execute("DELETE FROM users")
        print("All Data deleted")
        db.commit()
    else:
        print('Incorrect option')


def show_statement(query):
    for value in sql.execute(query):
        print(value)
        print()


def check_credential(userName, password):
    items = sql.execute(f"SELECT id, user_name FROM users WHERE user_name ='{userName}'").fetchall()
    if items == []:
        sql.execute("INSERT INTO users(user_name, password) VALUES (?, ?)", (userName, password))
        db.commit()
        return None
    else:
        return 'this username is already taken'


def login_in():
    print('Registration Form')
    userName = input('Enter your username: ')
    password = input('Enter your password: ')

    msg = check_credential(userName, password)
    if msg:
        print(msg)

    menu()


def sign_in():
    print('Sign in Form')
    userName = input('Enter your username: ')
    password = input('Enter your password: ')
    sql.execute(f"SELECT id, user_name FROM users WHERE user_name ='{userName}' AND password = '{password}'")
    items = sql.fetchall()
    if items == []:
        print('Incorrect username or password!\n')
        menu()
    else:
        userId = items[0][0]
        print()
        print(f"Hello {userName}. Your ID - {userId}")
        main(userId, userName)


# Create a function to get Date
def get_time(day):
    while True:
        try:
            dayOption = input('Selected spend today? Y/N \n').upper()
            if dayOption == 'Y':
                return date.today()
            elif dayOption == 'N':
                day = correct_data()
                return day
        except:
            print('You chose an incorrect option. Please chose again')


# Create a function to check the date format
def correct_data():
    while True:
        try:
            day = input('Input the date yyyy-mm-dd \n')
            pattern = re.compile("^\d{4}-((0[1-9])|(1[012]))-((0[1-9]|[12]\d)|3[01])$")
            if pattern.match(day):
                return day
        except:
            print('You chose an incorrect option. Please chose again')


def menu_check():
    while True:
        try:
            menu()
        except SystemExit:
            print('See you soon')
            break
        except:
            print('Oops. Something wrong')

if __name__ == '__main__':
    menu_check()