from web_dev import app
from web_dev import models

if __name__ == '__main__':
    models.create_db()
    app.run(port = 5000, debug = True)