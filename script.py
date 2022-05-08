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
maxpro = 'Panel dachowy MAX PRO to innowacyjne pokrycie dachowe. Łączy w sobie nowoczesny wygląd oraz prostotę montażu. Panel dachowy MAX PRO sprawdzi się zarówno w nowoczesnym i klasycznym budownictwie. Dzięki nowym możliwościom technologicznym oraz najwyższym standardom produkcji, ten rodzaj pokrycia jest doskonałym wyborem - świetnie się prezentuje oraz idealnie współgra z obecnymi trendami w budownictwie. Wyjątkowo płaski kształt nawiązujący do najbardziej pożądanego obecnie trendu na pokrycia dachowe na rąbek stojący wyróżnia się spośród dostępnej oferty. Mikrofala tworzy oryginalny wygląd oraz dodatkowo usztywnia profil dachowy. Ponadto trwałość produktu podnosi jedna z dwóch innowacyjnych powłok PRO.MAX PRO to idealny wybór zarówno dla inwestora oraz dekarza. Oprócz nietuzinkowego wyglądu zapewnia łatwość transportu, łączenia profili przy dłuższych odcinkach, szeroką powierzchnię krycia i szybkość montażu.'
liwiapro = 'Blachodachówka dwumodułowa Liwia PRO dzięki prostej i bardzo ciekawej formie idealnie pasuje do nowoczesnego budownictwa.Przypadnie do gustu osobom lubiącym minimalistyczny styl. Jej płaska powierzchnia została wzbogacona o wąskie, wysokie przetłoczenie z potrójnym falowaniem, które nadaje jej oryginalny kształt i zapewnia lepszą szczelność dachu.Zaletą blachodachówki jest modułowość, która ułatwia transport i montaż. Optymalny rozmiar arkuszy sprawdza się zarówno na prostych, jak i bardziej złożonych konstrukcjach dachowych.Liwia PRO jest wykonana z wysokiej jakości stali zabezpieczonej powłoką PRO. Gwarantuje Twojemu dachowi lepszą trwałość i wspaniały, wpisujący się w najnowsze trendy architektoniczne – wygląd. '
petrapro = 'Blachodachówka dwumodułowa Petra PRO to propozycja dla osób wymagających nowoczesnego, ale i awangardowego pokrycia dachowego.Nadaje budynkowi nietuzinkowy i dynamiczny wygląd. Posiada charakterystyczne, wyraziste, potrójne rowkowanie w górnej części fali i dwa delikatniejsze przetłoczenia w dolnej części, które dodają jej elegancji.Unikatowa forma blachodachówki tworzy jej oryginalny wygląd oraz dodatkowo ją usztywnia, zwiększając tym samym jej odporność na uszkodzenia. O większej trwałości tego pokrycia decyduje przede wszystkim bardzo dobra antykorozyjna powłoka PRO.Petra PRO jest produkowana w arkuszach dwumodułowych, co zapewnia optymalne wykorzystanie produktu i sprawia, że z łatwością może być montowany zarówno na dachach dwuspadowych, jak i bardziej skomplikowanych powierzchniach.'
monapro = 'Blachodachówka dwumodułowa Mona PRO łączy w sobie tradycję z nowoczesnością i bardzo dobrą jakość.Ten model to idealna propozycja dla inwestorów poszukujących pokrycia dachowego, które będzie zdobić i chronić ich dom przez wiele lat. Wysokie przetłoczenie z pojedynczym rowkiem nadaje połaci harmonijny, bardziej klasyczny i elegancki wygląd.Wieloletnie doświadczenie naszej firmy w projektowaniu blachodachówek zaowocowało uzyskaniem unikatowego profilu tego pokrycia dachowego. Dzięki niemu arkusze ściśle do siebie przylegają, przez co łączenie między nimi jest bardzo szczelne.Zwiększoną trwałość i odporność tej blachodachówki dwumodułowej zapewnia jedna z dwóch unikatowych powłok PRO, w których jest dostępna. Dwumodułowość Mony PROsprawia, że bardzo łatwo można ją montować na konstrukcji dachu o każdym kształcie.'
oskarpro = 'Jeśli szukasz najbardziej nowoczesnego i oryginalnego pokrycia dachowego – Oskar PRO spełni Twoje oczekiwania.To wpisująca się w najnowsze trendy architektoniczne forma panelu dachowego.Ze względu na szeroki rozstaw rąbków doskonale podkreśla minimalistyczny wygląd nowoczesnych domów. Jego prosta linia bardzo dobrze współgra również z tradycyjnym budownictwem.Oskar PRO został wykonany z dbałością o najwyższą jakość, którą poświadczamy wieloletnią gwarancją. Produkowany jest z surowca o wyjątkowych parametrach technicznych wykończonego powłoką PRO. Dzięki niej dach jest bardziej odporny na uszkodzenia mechaniczne i oddziaływanie warunków atmosferycznych.Nowoczesne technologie pozwalają na szybki montaż tej formy pokrycia na każdym dachu, przy zachowaniu jej maksymalnej szczelności i troski o każdy detal estetyki wykończenia.'
alexpro = 'Ten panel dachowy został zaprojektowany z myślą o odbiorcach ceniących najnowszy design oraz najwyższą jakość. Tradycyjny dach na rąbek stojący przechodzi obecnie swój renesans i jest najbardziej nowoczesną i pożądaną postacią pokrycia dachowego. Alex PRO to nasza propozycja nowej odsłony tego typu profilu. Nadaje budynkom niepowtarzalny charakter i lekką, szlachetną linię. Doskonale prezentuje się zarówno na modernistycznych, jak i klasycznych domach.Alex PRO to gwarancja wysokiej trwałości. Wykonany jest z wysokogatunkowej blachy, zabezpieczonej jedną z dwóch innowacyjnych, dostępnych tylko w naszej ofercie, powłok ochronnych. Dzięki niej Twój dach będzie bardziej odporny na uszkodzenia oraz dłużej zachowa swój oryginalny kolor. Łatwość montażu i dyskretne łączenia sprawiają, że ta forma pokrycia dachowego jest jeszcze bardziej elegancka i funkcjonalna.'

mona = 'Blachodachówka Mona łączy w sobie tradycję z nowoczesnością i bardzo dobrą jakością. Jej unikatowy profil zapewnia arkuszom ścisłe przyleganie i szczelne łączenia. Jest dostępna na wymiar i przeznaczona dla dużych i prostych powierzchni dachowych. '
alex = 'Panel dachowy Alex został zaprojektowany z myślą o odbiorcach ceniących design i najwyższą jakość.Jest nową odsłoną tradycyjnego dachu na rąbek stojący, która nadaje budynkom niepowtarzalny charakter i lekką, szlachetną linię. Doskonale prezentuje się zarówno na modernistycznych, jak i klasycznych domach.'
petra = 'Petra to propozycja dla osób oczekujących nowoczesnego, ale i awangardowego pokrycia dachowego.Cechuje ją oryginalny i wyrazisty profil. Jest dostępna w wersji na wymiar, dzięki czemu nie wymaga wielu łączeń, co podnosi estetykę dachu.'
olimpia = 'Olimpia jest uniwersalna dzięki swej formie. Jej szerokie przetłoczenie równoważy się z niską falą i nadaje pokryciu charakterystyczny, a przy tym regularny wygląd.Ten profil blachodachówki dedykowany jest nowoczesnemu i tradycyjnemu budownictwu. Produkujemy ją ze stali najwyższej jakości, w arkuszach ciętych na wymiar, które ułatwiają montaż na dachach o różnym kształcie.'
gloria = 'Blachodachówka Gloria to klasyka w najlepszym wydaniu. Tworzy eleganckie i trwałe pokrycie dachowe. Sprawdza się zarówno w tradycyjnym budownictwie, jak i przy renowacji obiektów zabytkowych. Odporność na wszelkie uszkodzenia zapewnia wysoka jakość materiału, z którego jest wykonana, jej szczelność natomiast gwarantuje m.in. rowek kapilarny'
max = 'Panel dachowy Max to najnowocześniejsza forma pokrycia dachowego.Dzięki nowym możliwościom technologicznym oraz produkcji, ten rodzaj pokrycia jest doskonałym wyborem - świetnie się prezentuje oraz idealnie współgra z obecnymi trendami w budownictwie. Oprócz nietuzinkowego wyglądu zapewnia łatwość transportu, łączenia profili przy dłuższych odcinkach, szeroką powierzchnię krycia.'
oskar = 'Oskar ze względu na szeroki rozstaw rąbków doskonale podkreśla minimalistyczny wygląd nowoczesnych domów.Jego prosta linia bardzo dobrze współgra również z tradycyjnym budownictwem. Produkowany jest z blachy o wysokich parametrach technicznych. Nowoczesne technologie pozwalają na jego szybki montaż przy zachowaniu maksymalnej szczelności.'

petraduo = 'Blachodachówka Petra DUO posiada charakterystyczne, potrójne rowkowanie w górnej części fali, dzięki któremu dach zyskuje nietuzinkowy i dynamiczny wygląd. Dwa delikatniejsze przetłoczenia w dolnej części dodają jej elegancji. Jej modułowość zapewnia optymalne zużycie produktu i sprawia, że może być z łatwością montowana na każdej konstrukcji dachowej, a szczególnie tej bardziej skomplikowanej'
liwiaduo = 'Blachodachówka dwumodułowa Liwia DUO dzięki prostej i bardzo ciekawej formie idealnie pasuje do nowoczesnego budownictwa.Zaletą blachodachówki jest modułowość, która zapewnia łatwość w transporcie i montażu. Optymalny rozmiar arkuszy sprawdza się zarówno na prostych, jak i bardziej złożonych konstrukcjach dachowych.'
monaduo = 'Mona DUO posiada wysokie przetłoczenie z pojedynczym rowkiem, które nadaje połaci harmonijny, bardziej klasyczny i elegancki styl.Dwa delikatniejsze przetłoczenia w dolnej części dodają jej elegancji. Jej modułowość zapewnia optymalne zużycie produktu i sprawia, że może być z łatwością montowana na każdej konstrukcji dachowej, a szczególnie tej bardziej skomplikowanej.Unikatowy profil tej blachodachówki dwumodułowej sprawia, że arkusze ściśle do siebie przylegają, a dach jest bardziej szczelny. Produkowana jest w arkuszach dwumodułowych, dzięki czemu jest bardzo ekonomiczna i sprawdza się na dachach o wszelakich kształtach.'

t7 = 'T7 to najbardziej klasyczny wzór blachy trapezowej. Jest chętnie wykorzystywany jako elementy wykończeniowe dachu, ale również na elewacjach lub jako obicie bram garażowych. Dostępny w bogatej kolorystyce, także drewnopodobnej.'
t14 = 'Profil T14 ma szerokie zastosowanie i jest bardzo wydajny. Wykonany jest z blachy o wysokiej trwałości i posiada rowek kapilarny, który zapewnia szczelność na łączeniach arkuszy. To bardzo wytrzymała i jednocześnie lekka forma pokrycia dachowego i elewacyjnego.'
t18 = 'Blacha trapezowa T18 posiada wzmacniane gęste przetłoczenia, które zapewniają wysoką sztywność tego profilu. Jednocześnie zaletą T18 jest jego łatwy montaż.'
t20 = 'Blacha trapezowa T20 swoim kształtem przypomina profil dachu na rąbek stojący. T20 ma wysokie walory estetyczne i parametry odpornościowe, jednocześnie stanowi znakomitą, bardziej ekonomiczną alternatywę dla paneli dachowych'
t20plus = 'Dodatkowe przetłoczenia na dolnej fali profilu blachy T20+ wpływają na usztywnienie profilu i nadają mu bardziej elegancki wygląd.'
t35 = 'Profil T35 jest przeznaczony do stosowania na rozległych powierzchniach dachowych o niewielkim nachyleniu. To pokrycie idealne dla obiektów przemysłowych. Wykonany jest ze stali o podwyższonej odporności na uszkodzenia mechaniczne, przy czym jest bardzo lekki. W efekcie nie tylko nie obciąża dachu, ale zapewnia mu jeszcze dodatkową szczelność.'
t35plus = 'T35 Plus posiada dodatkowe przetłoczenia, które wzmacniają sztywność profilu i zapewniają mu większą estetykę.'
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
