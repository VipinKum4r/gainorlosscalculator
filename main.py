from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        entry_price = float(request.form['entry'])
        exit_price = float(request.form['exit'])
        percent_change = ((exit_price - entry_price) / entry_price) * 100
        if exit_price > entry_price:
            result = f"{percent_change:.2f}% gain"
        else:
            result = f"{percent_change:.2f}% loss"
        return render_template('index.html', result=result)
    else:
        return render_template('index.html')

@app.route('/result')
def result():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)

