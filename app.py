from flask import Flask

application = Flask(__name__)
#application.config.from_object('config.BaseConfig')

@application.route('/')
def index():
    return 'Hello, world!'

if __name__=='__main__':
    application.run()
