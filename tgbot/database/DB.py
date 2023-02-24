import sqlite3
import time
from dataclasses import dataclass


@dataclass
class User:
    telegram_id: int
    registration_time: int
    subscribe_date: int
    username: str
    name: str
    referrals: int
    money: int
    email: str
    phone: str


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS Пользователи(
        Telegram_id INT PRIMARY KEY, 
        Registration_time INT,              
        Subscribe_date INT,
        Username TEXT,
        Name TEXT,
        Referrals INT,
        Money INT,
        Phone TEXT,
        Email TEXT);""")
        self.conn.commit()

    '''ПОЛЬЗОВАТЕЛИ'''

    def add_user(
            self,
            telegram_id,
            username,
            name,
            registration_time=f'{time.time()}',
            subscribe_date=f'{24 * 5}',
            referrals=0,
            money=0,
            phone='Не указано',
            email='Не указано'):
        user = [telegram_id, registration_time, subscribe_date, username, name, referrals, money, phone, email]
        self.cur.execute("INSERT INTO Пользователи VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?);", user)
        self.conn.commit()

    def update(self, index, val, user):
        self.cur.execute(f"UPDATE Пользователи SET {index} = '{val}' WHERE Telegram_id = {user};")
        self.conn.commit()

    def user_exist(self, user_id):
        self.cur.execute(f"SELECT COUNT(*) FROM Пользователи WHERE Telegram_id = {user_id}")
        count = self.cur.fetchone()[0]
        if count != 0:
            return True
        else:
            return False

    def get_user(self, user_id):
        self.cur.execute("SELECT * FROM Пользователи")
        users = self.cur.fetchall()
        if len(users) != 0:
            for i in range(len(users)):
                if users[i][0] == user_id:
                    return User(telegram_id=users[i][0], registration_time=users[i][1], subscribe_date=users[i][2],
                                username=users[i][3], name=users[i][4], referrals=users[i][5], money=users[i][6],
                                phone=users[i][7], email=users[i][8])

    def up_sub(self):
        self.cur.execute("SELECT * FROM Пользователи")
        users = self.cur.fetchall()
        if len(users) != 0:
            return users
