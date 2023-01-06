from datetime import datetime

def valDate(input):

    try:
        dateobject = datetime.strptime(input, '%d/%m/%Y')
        return True
    except ValueError:
        return False

input = "05/10/2020"

print(valDate(input))