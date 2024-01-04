def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    last_chars = text[1:]
    return f'{first_char}{last_chars}'
