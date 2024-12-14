s = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
text = ["блюншж явфвн, бйёпнёж яиэбёйёнляёф! оплизкриоь о еэбэфвж, злабэ кэ яштлбв квжнлккэь овпщ блидкэ яшбэяэпщ кв плищзл зиэоо (зиэооёсёзэуёь) ё кв мнлопл фёоил (нванвооёь). кэ яштлбв крдкл ялеянэцэпщ x, y, width, height ё зиэоо люкэнрдвкклал кэ зэнпёкзв лючвзпэ (ёиё зллнбёкэпш плфвз злкпрнля ъплал лючвзпэ, э-иь овайвкпэуёь)."]
text.append("эзъйфг эюжх. зйьщжвбщлзйф дмйкзы ийюэезавев люёф ийзюдлзы из дмйкм ai, зжв ы щллщрю. цлз жюзъшбщлюехжфю люёф, ыф ёзаюлю ыфъйщлх ечъмч кызч.")
text.append("зрмцфмн ёпдзмрмфтёмы, зиса зтефян. ря х ёдрм еихизтёдпм ут очфхч фтхд отедпац. утпстъисстн уфтжфдрря рси сднцм си чздптха, пмьа цтпаот офдцомн упдс очфхд: ")
text.append("зтефян зиса. ёт ёпткисмм сдьи отррифыихоти уфизпткисми ут утотумнстрч техпчкмёдсмв. д цдоки хумхто уфизтхцдёпгирящ сдрм чхпчж. ечзир фдзя здпасиньирч уптзтцётфстрч хтцфчзсмыихцёч!")
text.append("сьоюьт баюь. обсйат сьоюи этютшцыбай каьа внчщ ын ятюптю. каь сщм ныыи п кщтшаюцшб ьэцяныцт ыьътышщнабюи ынсь хнамыбай.")
text.append("упьлнэюняхюр, пшфюьфх! шрщк уъняю щлюлчзк эрьоррнщл. к кнчкйэз ъафвфлчзщжш ыьрпэюлнфюрчршцьяыщъх ыьъфунъпэюнрщщъчъофэюфгрэцъх цъшылщфф. улщфшлршэк ыъэюлнцлшфыъ йоя ьъээфф.")
text.append("тэпяйш туьк. рэ юуярйд samsung ai юяэрэтчб тън ьо 10сэ ыоабуя щъоаа р ысв. ")
text.append("ощлыёф мпвпы, очуэыуф мцкоучуыщмув! ъщоьхксуэп, хщнок юшкь люопэ ьцпоюидпп ткшйэуп?")
text.append(" ощлыёф опшж. мкг ъщвэщмёф йдух кхэумуыщмкцу")
text.append(" чвфдоэ чшбп, жхуъушаоэ юяьшбё ! х гдвчвяъшбьш булшцв е хуаь чьуявцу- бугдухятс булш гдшчявъшбьш гв гвчюяскшбьс ьбёшдбшёу чят хулшэ вдцубьыуйьь!")


def decrypt(t, shift):
    rez=""
    for c in t:
        if (c in s):
            i=s.find(c)
            i= (i-shift) % len(s)
            rez=rez+s[i]
        else:
             rez=rez+c
    return rez

print("Задание 1  \n" + decrypt(text[0], 30) + "\n")
print("Задание 2  \n" + decrypt(text[1], 26) + "\n")
print("Задание 3  \n" + decrypt(text[2], 4) + "\n")
print("Задание 4  \n" + decrypt(text[3], 4) + "\n")
print("Задание 5  \n" + decrypt(text[4], 14) + "\n")
print("Задание 6  \n" + decrypt(text[5], 12) + "\n")
print("Задание 7  \n" + decrypt(text[6], 15) + "\n")
print("Задание 8  \n" + decrypt(text[7], 11) + "\n")
print("Задание 9  \n" + decrypt(text[8], 11) + "\n")
print("Задание 10  \n" + decrypt(text[9], 20) + "\n")

