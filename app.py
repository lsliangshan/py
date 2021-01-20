from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xed]/'
# app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    # return '''
    #   <div style="display: flex; flex-direction: row; align-items: center; justify-content: center; width: 100%; height: 100%;">
    #     <h1 style="color: #f33;">Greeting from jenkins</h1>
    #   </div>
    # '''
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if (request.method == 'POST'):
        if request.form['username'] != 'ls' or request.form['password'] != '123123':
            error = '账号或密码错误'
        else:
            flash('登录成功')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)


if __name__ == '__main__':
    app.run()
