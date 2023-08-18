from flask import Flask

app = Flask(__name__)

app = Flask(__name__,
            static_url_path='',
            static_folder='./')

app.run(host='0.0.0.0', port=8000)

