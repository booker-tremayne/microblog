from app import app

@app.route('/')
@app.route('/route')
def index():
    return "Hello, World! >:("