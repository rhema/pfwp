#  This example uses bottle, a cool python only web server that makes it easy to prototype web applications.
#  To test, run this program and go to http://localhost:8080/Rhema in a browser on your computer.
from bottle import route, run, template


@route('/:name')
def index(name='World'):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)