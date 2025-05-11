from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('subscribe.html')

@app.route('/experiments')
def experiments():
    return render_template('experiments.html')

@app.route('/form', methods=['POST'])
def handle_form():
    email = request.form.get('email')
    birthdate = request.form.get('birthdate')

    print(f"Received: {email}, {birthdate}")  # for debugging

    return redirect(url_for('experiments', success=1))

if __name__ == '__main__':
    app.run(debug=True)
