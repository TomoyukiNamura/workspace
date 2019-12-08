from bottle import *

@route("/")
def route():
    return'<h1 align="center">hello world</h1>'

if __name__ == '__main__':
    run(host="localhost",port=3031, debug=True, reloader=True)
