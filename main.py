from pyscript import display, document


def convert_temp(e):
            document.getElementById('output').innerHTML = ' '
            f = float(document.getElementById("fahrenheit").value)
            c = (f - 32) * 5 / 9

            if c >= 37.8:
                display(f'Fever', target='output')
            else:
                display(f'Normal Temperature', target='output')