# https://medium.com/fintechexplained/flask-host-your-python-machine-learning-model-on-web-b598151886d

# from flask_flatpages import FlatPages
from flask_frozen import Freezer

app = Flask('house_pricer')
app.config.from_pyfile('settings.py')
# pages = FlatPages(app)
freezer = Freezer(app)



# if __name__ == "__main__":
#     app.run("localhost", "9999", debug=True)



