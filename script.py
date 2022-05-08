import time
import pyperclip
import pyautogui

time.sleep(1)

print("Press Ctrl-C to quit.")
# script speed
pyautogui.PAUSE = 2
# legends
print(
    "Kolory: 150a, 185a, 3005, 3009, 3011, 5010, 6005, 6020, 7016, 7024, 8004, 8017, 8019, 9005, 9006, 9010, 9998, 9999"
)
print(
    "Powłoki: Alucynk - AL, Exelent - EX, Granite Mat - GM, Granite Standard - GS, Granite UltraMat - GU, Mat - MA, Połysk - PO, Purtex - PU, Purtex Strong - PS, UltraMat - UM"
)
print("Folia: T, N")
print("Antykondensat: T, N")
print("Maszyna: Alex, Gloria, Liwia, Max, Maxima, Mona, Olimpia, Oskar, Petra")
# user input according to legends
# TODO add lower format too whole input
prod = input("Podaj kolor, powłokę, folie, antykondensat i maszynę w jednym ciągu: ")
# user input transfer to list
dane = [prod[0:4], prod[4:6], prod[6], prod[7], prod[8:]]
# roof type discription
liwia = "Blachodachówka dwumodułowa Liwia DUO dzięki prostej i bardzo ciekawej formie idealnie pasuje do nowoczesnego budownictwa. Zaletą blachodachówki jest modułowość, która zapewnia łatwość w transporcie i montażu. Optymalny rozmiar arkuszy sprawdza się zarówno na prostych, jak i bardziej złożonych konstrukcjach dachowych."
mona = "Mona DUO posiada wysokie przetłoczenie z pojedynczym rowkiem, które nadaje połaci harmonijny, bardziej klasyczny i elegancki styl.Dwa delikatniejsze przetłoczenia w dolnej części dodają jej elegancji. Jej modułowość zapewnia optymalne zużycie produktu i sprawia, że może być z łatwością montowana na każdej konstrukcji dachowej, a szczególnie tej bardziej skomplikowanej.Unikatowy profil tej blachodachówki dwumodułowej sprawia, że arkusze ściśle do siebie przylegają, a dach jest bardziej szczelny. Produkowana jest w arkuszach dwumodułowych, dzięki czemu jest bardzo ekonomiczna i sprawdza się na dachach o wszelakich kształtach."
monapro = "Blachodachówka dwumodułowa Mona PRO łączy w sobie tradycję z nowoczesnością i bardzo dobrą jakość.Ten model to idealna propozycja dla inwestorów poszukujących pokrycia dachowego, które będzie zdobić i chronić ich dom przez wiele lat. Wysokie przetłoczenie z pojedynczym rowkiem nadaje połaci harmonijny, bardziej klasyczny i elegancki wygląd.Wieloletnie doświadczenie naszej firmy w projektowaniu blachodachówek zaowocowało uzyskaniem unikatowego profilu tego pokrycia dachowego. Dzięki niemu arkusze ściśle do siebie przylegają, przez co łączenie między nimi jest bardzo szczelne.Zwiększoną trwałość i odporność tej blachodachówki dwumodułowej zapewnia jedna z dwóch unikatowych powłok PRO, w których jest dostępna. Dwumodułowość Mony PROsprawia, że bardzo łatwo można ją montować na konstrukcji dachu o każdym kształcie."
# safetybreak for script to use move mouse to upper-left of the screen
pyautogui.FAILSAFE = True

pyautogui.click(1622, 15)  # choose active window
pyautogui.click(187, 232)  # select tab "Jednostki i kody"
# TODO add chosing param
pyautogui.click(46, 348)  # click if pcs(szt) comment if not

# select "jednostka pomocnicza"
pyautogui.doubleClick(340, 605)
pyautogui.click(344, 328)
pyautogui.click(653, 276)

# TODO add chosing param
# pyautogui.doubleClick(331, 324) #select if m2 not pcs

pyautogui.click(877, 234)  # select "Opisy i tłumaczenia" tab
pyautogui.click(1794, 942)  # click lens
pyautogui.click(635, 516)  # select a discription field
pyperclip.copy(mona)  # copy description
pyautogui.hotkey("ctrl", "v")  # paste description
pyautogui.click(947, 441)  # click save
pyautogui.click(1122, 234)  # select "Atrybuty" tab
pyautogui.click(1761, 941)  # click plus
pyautogui.click(925, 617)  # select active list
pyautogui.press("End", presses=1)  # press end to go to last element

pyautogui.doubleClick(751, 651)  # select "POWŁOKA"
pyautogui.doubleClick(959, 659)  # select empty attribute
# loop for adding correct "POWŁOKA"
if dane[1] == "al":
    pyautogui.press("down", presses=2)
elif dane[1] == "ex":
    pyautogui.press("down", presses=3)
elif dane[1] == "gm":
    pyautogui.press("down", presses=4)
elif dane[1] == "gs":
    pyautogui.press("down", presses=5)
elif dane[1] == "gu":
    pyautogui.press("down", presses=6)
elif dane[1] == "ma":
    pyautogui.press("down", presses=7)
elif dane[1] == "po":
    pyautogui.press("down", presses=8)
elif dane[1] == "pu":
    pyautogui.press("down", presses=9)
elif dane[1] == "ps":
    pyautogui.press("down", presses=10)
elif dane[1] == "um":
    pyautogui.press("down", presses=11)

pyautogui.click(1129, 423)  # save attribute
pyautogui.click(1333, 631)  # save attribute list

pyautogui.click(1761, 941)  # click plus
pyautogui.click(925, 617)  # select active list
pyautogui.press("End", presses=1)  # press end to go to last element

pyautogui.doubleClick(741, 632)  # select "KOLOR"
pyautogui.doubleClick(959, 659)  # select empty attribute
# loop for adding correct "KOLOR"
if dane[0] == "150a":
    pyautogui.press("down", presses=2)
elif dane[0] == "185a":
    pyautogui.press("down", presses=3)
elif dane[0] == "3005":
    pyautogui.press("down", presses=4)
elif dane[0] == "3009":
    pyautogui.press("down", presses=5)
elif dane[0] == "3011":
    pyautogui.press("down", presses=6)
elif dane[0] == "5010":
    pyautogui.press("down", presses=7)
elif dane[0] == "6005":
    pyautogui.press("down", presses=8)
elif dane[0] == "6020":
    pyautogui.press("down", presses=9)
elif dane[0] == "7016":
    pyautogui.press("down", presses=10)
elif dane[0] == "7024":
    pyautogui.press("down", presses=11)
elif dane[0] == "8004":
    pyautogui.press("down", presses=12)
elif dane[0] == "8017":
    pyautogui.press("down", presses=13)
elif dane[0] == "8019":
    pyautogui.press("down", presses=14)
elif dane[0] == "9005":
    pyautogui.press("down", presses=15)
elif dane[0] == "9006":
    pyautogui.press("down", presses=16)
elif dane[0] == "9010":
    pyautogui.press("down", presses=17)
elif dane[0] == "9998":
    pyautogui.press("down", presses=18)
elif dane[0] == "9999":
    pyautogui.press("down", presses=19)

pyautogui.click(1129, 423)  # save attribute
pyautogui.click(1333, 631)  # save attribute list

pyautogui.click(1761, 941)  # click plus
pyautogui.click(925, 617)  # select active list
pyautogui.press("End", presses=1)  # press end to go to last element

pyautogui.doubleClick(743, 700)  # select "FOLIA"
pyautogui.doubleClick(959, 659)  # select empty attribute
# loop for selecting correct attribute
if dane[2] == "n":
    pyautogui.press("down", presses=2)
elif dane[2] == "t":
    pyautogui.press("down", presses=3)

pyautogui.click(1129, 423)  # save attribute
pyautogui.click(1333, 631)  # save attribute list

pyautogui.click(1761, 941)  # click plus
pyautogui.click(925, 617)  # select active list
pyautogui.press("End", presses=1)  # press end to go to last element

pyautogui.doubleClick(755, 673)  # select "ANTYKONDENSAT"
pyautogui.doubleClick(959, 659)  # select empty attribute
# loop for selecting correct attribute
if dane[3] == "n":
    pyautogui.press("down", presses=2)
elif dane[3] == "t":
    pyautogui.press("down", presses=3)

pyautogui.click(1129, 423)  # save attribute
pyautogui.click(1333, 631)  # save attribute listy

pyautogui.click(1761, 941)  # click plus
pyautogui.click(925, 617)  # select active list
pyautogui.press("End", presses=1)  # press end to go to last element

pyautogui.doubleClick(742, 611)  # select "MASZYNA"
# loop to select correct "MASZYNA"
if dane[4] == "alex":
    pyautogui.press("down", presses=3)
elif dane[4] == "gloria":
    pyautogui.press("down", presses=4)
elif dane[4] == "liwia":
    pyautogui.press("down", presses=5)
elif dane[4] == "max":
    pyautogui.press("down", presses=6)
elif dane[4] == "maxima":
    pyautogui.press("down", presses=7)
elif dane[4] == "mona":
    pyautogui.press("down", presses=8)
elif dane[4] == "olimpia":
    pyautogui.press("down", presses=9)
elif dane[4] == "oskar":
    pyautogui.press("down", presses=10)
elif dane[4] == "petra":
    pyautogui.press("down", presses=11)

pyautogui.press("Enter", presses=1)  # exit list
