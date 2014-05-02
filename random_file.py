import string
import random


def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    # Returns a random ID
    return ''.join(random.choice(chars) for _ in range(size))

def string_generator(size=8, chars=string.ascii_lowercase):
    # Returns a random string of characters
    return ''.join(random.choice(chars) for _ in range(size))

def date_generator():
    # Returns a random date
    year = str(random.randint(1980, 2014))
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    month = (random.choice(months))
    day = str(random.randint(1, 30))

    if (len(day) == 1):
        day = str("0" + day)

    return str(year + "-" + month + "-" + day)
