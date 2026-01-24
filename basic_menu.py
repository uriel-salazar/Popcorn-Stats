
from set_api import authorize_code

from flask_config import app


def menu():
    while True:
        option=print(""" 1. Initialize OAuth
                     2. Something Else""")
        if option==1:
            authorize_code()
            app.run(port=8000)
            