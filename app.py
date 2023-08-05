from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index2.html')
  

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sproducts')
def sproducts():
    return render_template('sproduct.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True) 