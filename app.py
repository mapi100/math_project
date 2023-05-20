from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import InputRequired

app = Flask(__name__)
app.secret_key = 'avueno'


class NumberForm(FlaskForm):
    number = IntegerField('Enter a number:', validators=[InputRequired()])
    submit = SubmitField('Find Closest Prime')


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_closest_prime(n):
    if is_prime(n):
        return n

    lower = n - 1
    upper = n + 1

    while True:
        if is_prime(lower):
            return lower
        elif is_prime(upper):
            return upper
        lower -= 1
        upper += 1


@app.route('/', methods=['GET', 'POST'])
def closest_prime():
    form = NumberForm()

    if form.validate_on_submit():
        number = form.number.data
        closest_prime_number = find_closest_prime(number)
        flash(f"The closest prime number to {number} is {closest_prime_number}.")

    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
