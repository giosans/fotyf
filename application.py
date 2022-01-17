from flask import Flask, render_template
from flask_assets import Environment, Bundle # that's for the scss

# go to the tutorial for the instructions
application = app = Flask(__name__)

# this is what has to be compiled to css
assets = Environment(app)
# avoid caching
assets.cache = False
assets.manifest = False

assets.url = app.static_url_path
assets.append_path('static/sass')
scss = Bundle('style.scss', filters='pyscss', output='all.css')

# set a few configuration variables
assets.config['PYSCSS_LOAD_PATHS'] = assets.load_path
assets.config['PYSCSS_STATIC_URL'] = assets.url
assets.config['PYSCSS_STATIC_ROOT'] = assets.directory
assets.config['PYSCSS_ASSETS_URL'] = assets.url
assets.config['PYSCSS_ASSETS_ROOT'] = assets.directory

assets.register('scss_all', scss)

@app.route('/') 
@app.route('/index') 
def index(): 
    return render_template("index.html")

@app.route('/about') 
def about(): 
    return render_template("about.html")

@app.route('/gallery') 
def gallery(): 
    return render_template("gallery.html")

@app.route('/contact') 
def contact(): 
    return render_template("contact.html")

#@app.route('/blog') 
#def blog(): 
#    return render_template("blog.html")

@app.route('/listen') 
def listen(): 
    return render_template("listen.html")


# @app.route('/') 
# @app.route('/<user>') 
# def index(user=None): 
#     return render_template("user.html",user=user)

# @app.route('/profile/<name>') 
# def profile(name): 
#     return render_template("profile.html", name=name)

# @app.route('/shopping')
# def shopping(): 
#     food = ["cheese",'tuna',"tomato"]
#     return render_template("shopping.html",food=food)

if __name__ == '__main__': 
    application.run(debug=False)

