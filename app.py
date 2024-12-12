from flask import Flask, render_template, request
from converters.length import convert_length
from converters.weight import convert_weight
from converters.temperature import convert_temperature

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/length', methods=['GET', 'POST'])
def length_conversion():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        result = convert_length(value, from_unit, to_unit)

    return render_template('length.html', result=result)


@app.route('/weight', methods=['GET', 'POST'])
def weight_conversion():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        result = convert_weight(value, from_unit, to_unit)

    return render_template('weight.html', result=result)


@app.route('/temperature', methods=['GET', 'POST'])
def temperature_conversion():
    result = None
    if request.method == 'POST':
        value = float(request.form['value'])
        from_unit = request.form['from_unit']
        to_unit = request.form['to_unit']

        result = convert_temperature(value, from_unit, to_unit)

    return render_template('temperature.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
