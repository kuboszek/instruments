from user import User
class Manager:
    def __init__(self):
        pass

    def register(self):
        nick = input('Podaj nick: ')
        avatar = input('Sciezka dostepu do pliku z avatarem: ')
        user = User(nick, avatar)
        # Zapis uzytkownika do bazy danych
        # TODO: addUserToDB(user)
        return user

    def login(self):
        nick = input('Podaj nick: ')
        passwd = input('Podaj hasło: ')
        user = User(nick, 'xyz', passwd )   #MOCK: TODO # user = getUserFromDB()
        return user

