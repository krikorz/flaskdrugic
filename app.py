from flask import Flask, render_template
import random as r
# pip install flask
app = Flask(__name__)
dijaki=["kiki", "bomba", "pipi", "tuti"]
imena = [
    "Ana", "Borut", "Cene", "Dora", "Eva",
    "Franc", "Gaja", "Hana", "Igor", "Jana",
    "Klemen", "Lana", "Miha", "Nina", "Oskar",
    "Petra", "Rok", "Sara", "Tina", "Urban",
    "Vid", "Zala", "Žiga", "Neža", "Lea",
    "David", "Katja", "Luka", "Tim", "Maja"
]
priimki = [
    "Novak", "Kranjc", "Zupančič", "Mlakar", "Potočnik",
    "Kovač", "Hribar", "Medved", "Rozman", "Petek",
    "Jereb", "Turk", "Kos", "Kotnik", "Vidmar",
    "Gregorc", "Majer", "Zajc", "Kralj", "Božič",
    "Križaj", "Lesjak", "Logar", "Tomšič", "Prevc",
    "Dolenc", "Fabjan", "Jenko", "Šubic", "Oblak"
]

starosti = [
    23, 34, 45, 29, 31,
    52, 27, 38, 41, 36,
    22, 44, 33, 30, 25,
    60, 26, 48, 39, 28,
    24, 43, 35, 46, 21,
    40, 50, 32, 19, 58
]

kraji_rojstva = [
    "Ljubljana", "Maribor", "Celje", "Kranj", "Koper",
    "Novo mesto", "Velenje", "Ptuj", "Trbovlje", "Murska Sobota",
    "Jesenice", "Nova Gorica", "Kamnik", "Škofja Loka", "Izola",
    "Postojna", "Sežana", "Ravne na Koroškem", "Brežice", "Litija",
    "Domžale", "Logatec", "Kočevje", "Žalec", "Črnomelj",
    "Metlika", "Idrija", "Lenart", "Radovljica", "Laško"
]

naslovi = [
    "Slovenska cesta 12", "Tržaška cesta 45", "Dunajska cesta 78", "Celovška cesta 34", "Cankarjeva ulica 56",
    "Prešernova cesta 8", "Partizanska ulica 21", "Gregorčičeva ulica 67", "Levstikova ulica 39", "Bežigrajska cesta 14",
    "Kidričeva ulica 88", "Župančičeva ulica 31", "Tomačevo 25", "Rožna dolina 42", "Savska cesta 9",
    "Litijska cesta 61", "Šmartinska cesta 17", "Koroška cesta 70", "Poljanska cesta 22", "Viška cesta 38",
    "Vodnikova cesta 19", "Tivolska cesta 6", "Parmova ulica 53", "Zaloška cesta 80", "Barjanska cesta 3",
    "Kajuhova ulica 29", "Koprska ulica 74", "Miklošičeva cesta 16", "Ilirska ulica 11", "Stari trg 60"
]




@app.route("/")
def hello_world():
    dijak=r.choice(dijaki)
    ocena=r.randint(1,5)
    return render_template("index.html", naslov="Najboljša stran❤️", dijak=dijak,ocena=ocena)

@app.route("/randomOseba")
def rndOseba():
    ime=r.choice(imena)
    priimek=r.choice(priimki)
    starost=r.choice(starosti)
    krajr=r.choice(kraji_rojstva)
    naslov=r.choice(naslovi)
    return render_template("randomOseba.html", a=ime, b=priimek,c=starost,d=krajr,e=naslov)
app.run(debug=True, port=7777)