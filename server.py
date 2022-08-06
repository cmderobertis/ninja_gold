from flask import Flask, render_template, session, request, redirect, url_for
import random
import datetime

app = Flask(__name__)
app.secret_key = 'there is a fire in the building'


@app.route('/')
def index():
    if not 'activity_log' in session:
        session['activity_log'] = []
    if not 'gold' in session:
        session['gold'] = 0
    gold = session['gold']
    return render_template('index.html', gold=gold)


@app.route('/process_money', methods=['POST'])
def process():
    if request.form['building'] == 'farm':
        session['amount'] = random.randint(10, 20)
        session['gold'] += session['amount']
    if request.form['building'] == 'cave':
        session['amount'] = random.randint(5, 10)
        session['gold'] += session['amount']
    if request.form['building'] == 'house':
        session['amount'] = random.randint(2, 5)
        session['gold'] += session['amount']
    if request.form['building'] == 'casino':
        session['amount'] = random.randint(-50, 50)
        session['gold'] += session['amount']
    activity_item = {
        'gold': session['gold'],
        'amount': session['amount'],
        'success_danger': 'success' if session['amount'] > 0 else ('danger' if session['amount'] < 0 else 'primary'),
        'earned_lost': 'Earned' if session['amount'] >= 0 else 'Lost',
        'building': request.form['building'],
        'time': datetime.datetime.now()
    }
    session['activity_log'].append(activity_item)
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
