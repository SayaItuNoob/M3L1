from flask import Flask
import random
elements = "+-/*!&$#?=@<>"
password = ""

for i in range(7):
    password += random.choice(elements)
Pass = "Here is your pass"
app = Flask(__name__)

tech_list = ['Kebanyakan orang yang menderita kecanduan teknologi mengalami stres yang kuat ketika mereka berada di luar area jangkauan jaringan atau tidak dapat menggunakan perangkat mereka',
             'Menurut sebuah studi yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka bergantung pada ponsel pintar mereka.',
             'Studi tentang ketergantungan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan',
             'Menurut sebuah studi tahun 2019, lebih dari 60% orang merespons pesan pekerjaan di ponsel mereka dalam waktu 15 menit setelah pulang kerja',
             'Salah satu cara untuk memerangi ketergantungan teknologi adalah dengan mencari kegiatan yang membawa kesenangan dan meningkatkan suasana hati',
             'Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten',
             'Elon Musk juga menganjurkan regulasi jejaring sosial dan perlindungan data pribadi pengguna. Dia mengklaim bahwa jejaring sosial mengumpulkan sejumlah besar informasi tentang kita, yang kemudian dapat digunakan untuk memanipulasi pikiran dan perilaku kita',
             'Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini'
             ]

@app.route("/")
def hello_world():
    return '''<h1>Hello, World!</h1>
    <p>We can play games:</p>
    <ul>
        <li><a href="/tech_fact">View interesting facts</a>
        <li><a href="/password_gen">Generate a password</a>
    </ul>
    '''


@app.route("/tech_fact")
def fact():
    return f'<h1>{random.choice(tech_list)}</h1>'

@app.route("/password_gen")
def password_gen():
    
    return f'''
    <h1>Here is your password :</h1>
    <h2>{password}</h2>'''
    
app.run(debug=True)