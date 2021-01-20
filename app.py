from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '''
      <div style="display: flex; flex-direction: row; align-items: center; justify-content: center; width: 100%; height: 100%;">
        <h1 style="color: #f33;">Greeting from jenkins</h1>
      </div>
    '''


if __name__ == '__main__':
    app.run()
