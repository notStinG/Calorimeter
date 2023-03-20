from flask import Flask, request, render_template, redirect

app = Flask(__name__)

meals = []

@app.route('/', methods=['GET', 'POST'])
def index():
    counter = 0
    if request.method == 'POST':
        name = request.form.get('name')
        calories = request.form.get('calories')
        if not calories:
            calories = 0
        if calories == "6969":
            url = f'https://www.youtube.com/watch?v=b6SYrzgvi00'
            return redirect(url)
        else:
            calories = int(calories)
        meal = {
            'name': name,
            'calories': calories
        }
        meals.append(meal)
    total_calories = sum([meal['calories'] for meal in meals])
    if total_calories <= 2200:
        return render_template('index.html', total_calories=total_calories, meals=meals)
    elif total_calories > 2200:
        return render_template('excess.html', total_calories=total_calories, meals=meals) 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)
