def expr_cleared(expr):
    """ подгатавливает выражение для вычисления """
    # приводим буквы в выражении к нижнему регистру, удаляем пробелы
    expr_cleared = expr.lower().replace(' ', '')
    # заменяем некорректные символы
    wrong_simbols = {
        'math.': '',
        "'": "",
        '"': '',
        '^': '**',  # возведение в степень
        '?': '',
        '_': '',
        '!': '',
        '@': '',
        ":": '',
        ';': '',
    }
    for key, value in wrong_simbols.items():
        if key in expr_cleared:
            expr_cleared = expr_cleared.replace(key, value)
    return expr_cleared
