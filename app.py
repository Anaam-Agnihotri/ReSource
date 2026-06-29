from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    waste_item = request.form['waste_item'].lower()
    
    edible_items = ["rice", "bread", "vegetables", "fruits", "dal", "curry", "roti", "chapati", "milk", "paneer", "sabzi", "leftover food"]
    compost_only = ["banana peels", "vegetable peels", "eggshells", "tea leaves", "coffee grounds", "fruit peels"]
    
    if waste_item in edible_items:
        advice = "This still looks consumable! Consider donating it to someone in need or feeding it to stray animals nearby instead of throwing it away."
    elif waste_item in compost_only:
        advice = "This is a great candidate for composting. Mix it with dry leaves or soil in a compost bin, and in a few weeks it'll break down into nutrient-rich fertilizer."
    else:
        advice = "We don't have specific advice for this item yet, but as a general rule: if it's organic and no longer edible, composting is usually a safe bet."
        
    return render_template('result.html',waste_item=waste_item, advice=advice)

if __name__ == '__main__':
    app.run(debug=True)
