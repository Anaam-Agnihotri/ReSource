from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    waste_item = request.form['waste_item'].lower()
    
    edible_items = ["rice", "bread", "vegetables", "fruits", "dal", "curry"]
    
    if waste_item in edible_items:
        advice = "This still looks consumable! Consider donating it to someone in need or feeding it to stray animals nearby instead of throwing it away."
    else:
        advice = "If it's no longer edible, its a great candidate for composting. Mix it with dry leaves or soil in a compost bin, and in a few weeks it'll break down into nutrient-rich fertilizer."
        
    return render_template('result.html',waste_item=waste_item, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
