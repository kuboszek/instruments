class User:
    def __init__(self, nick, avatar, password):
        self.nick = nick
        self.avatar = avatar
        self.rank = 0
        self.password = password
        self.users = []
        self.instruments = []

    def addFriend(self, user):
        self.users.append(user)

    def findFriend(self, nick):
        #wyszukiwanie w baze danych / pliku
        user = User(nick, 'AVATAR', '1234') # MOCK
        #Tak naprawde ta funkcja powinna zwrocic liste uzytkownikow o takim nicku
        return user

    def addInstrument(self, instrument):
        if instrument not in self.instruments:
            self.instruments.append(instrument)

    def printInstruments(self):
        for instrument in self.instruments:
            instrument.print()
