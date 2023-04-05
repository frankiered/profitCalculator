from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        list_price = float(request.form['list_price'])
        cost = float(request.form['cost'])
        number_of_tickets = int(request.form['number_of_tickets'])

        result = ((list_price - (list_price * 0.14)) * number_of_tickets) - (cost * 4)
        return render_template('index.html', result=result)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
