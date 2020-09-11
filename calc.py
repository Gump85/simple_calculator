from math import *  # импортируем модуль math целиком

from flask import Flask, request, render_template, flash, redirect, url_for

from utils import expr_cleared


app = Flask(__name__)
app.secret_key = "12345"

@app.route('/')
def index():
    """ основная страница калькулятора, получает пользовательский ввод и возвращает ответ"""
    expr = request.args.get('q')
    if expr:
        # очищаем пользовательский ввод
        expr = expr_cleared(expr)
        # обрабатываем очищенное выражение
        try:
            result = eval(expr)
        except (SyntaxError, NameError, ValueError, TypeError):
            flash('Введено неверное выражение')
            return redirect(url_for('index'))
        except ZeroDivisionError:
            flash('В выражении присутствует операция деления на ноль')
            return redirect(url_for('index'))

    context = {
        'title': 'Результат:' if expr else None,
        'result': result if expr else None,
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.debug = True
    app.run()
