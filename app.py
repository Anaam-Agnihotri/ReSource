from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    waste_item = request.form['waste_item']
    return f"You entered: {waste_item}"

if __name__ == '__main__':
    app.run(debug=True)
