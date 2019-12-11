#Uzytkownik wchodzi do systemu - co chce zrobic
# 1) Rejestracja w systemie
#  -> podaje nick, haslo, mail
# 2) Moze sie zalogowac
#  -> podaje nick, haslo
# 3) Moze wybrac sobie instrument z listy instrumentow
#  -> aplikacja wyswietla liste instrumentow
#  -> uzytkownik wybiera instrument
# 4) Po wybraniu instrumentu, uzytkownik moze wykonywac cwiczenia
#  ->
import manager
from music.guitar import Guitar
from music.voice import Voice
from music.flute import Flute


mng = manager.Manager()

#Rejestracja lub logowanie
ans = input('Co chcesz zrobic? (R)ejestracja czy (L)ogowanie?')
if ans == 'R':
    user = mng.register()
elif ans == 'L':
    user = mng.login()
else:
    print('bledna opcja')

while(True):
    ans = input('''Wybierz opcje:
                (I)nstrumenty
                (Z)najomi (niedostepne)
                (G)rupy (niedostepne)         
                ''')
    if ans == 'I':
        print('Twoje instrumenty: ')
        user.printInstruments()
        ans = input('Nowy instrument: (G)uitar, (F)lute, (V)oice')
        if ans == 'G':
            instrument = Guitar()
            user.addInstrument(instrument)
        elif ans == 'F':
            instrument = Flute()
            user.addInstrument(instrument)
        elif ans == 'V':
            instrument = Voice()
            user.addInstrument(instrument)

