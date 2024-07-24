from chalice import Chalice

app = Chalice(app_name='hello')


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/blog')
def blog():
    return {'Blog': 'This is my blog'}

@app.route('/blogs')
def blog():
    return {'Blog': 'This is my blog demo'}


