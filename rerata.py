from flask import Flask, render_template, request

app = Flask(__name__)

def rerata(n, data):
    jumlah = sum(data)
    rerata = jumlah / n
    return rerata

@app.route('/')
def index():
    return render_template('hitung-rerata.html')

@app.route('/proses', methods=['POST'])
def proses():
    n = int(request.form['n'])
    data = [int(request.form[f'data{i}']) for i in range(1, n + 1)]  
    
    jumlah = sum(data)
    rerata = jumlah / n
    
    hasil = {'data': data, 'rerata': rerata}
    
    return render_template('hitung-rerata.html', hasil=hasil, n=n)

if __name__ == '__main__':
    app.run()
