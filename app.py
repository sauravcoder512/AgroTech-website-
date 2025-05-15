from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.secret_key = 'your_secret_key_here'
users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop-care', methods=['GET', 'POST'])
def crop_care():
    summary = None
    if request.method == 'POST':
        file = request.files['crop_image']
        climate = request.form.get('climate', '')
        if file:
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            summary = {
                'crop': 'Wheat',
                'condition': 'Healthy',
                'climate': climate,
                'summary': 'Your crop looks healthy. No major issues detected.',
                'suggestion': 'Continue regular watering, monitor for pests, and ensure optimal temperature for wheat growth.',
            }
    return render_template('crop_care.html', summary=summary)

@app.route('/buy-sell')
def buy_sell():
    return render_template('buy_sell.html')

@app.route('/schemes')
def schemes():
    return render_template('schemes.html')

@app.route('/learn')
def learn():
    return render_template('learn.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/crop-library')
def crop_library():
    return render_template('crop_library.html')

@app.route('/weather')
def weather():
    return render_template('weather.html')

@app.route('/pest-alerts')
def pest_alerts():
    return render_template('pest_alerts.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    if username in users:
        flash('Username already exists. Please choose another.', 'danger')
        return redirect(url_for('index'))
    users[username] = {'email': email, 'password': password}
    flash('Registration successful! You can now sign in.', 'success')
    return redirect(url_for('index'))

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if username in users and users[username]['password'] == password:
        session['user'] = username
    else:
        flash('Invalid username or password.', 'danger')
    return redirect(url_for('index'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    product_id = request.form.get('product_id')
    # Placeholder: In a real app, add product to user's cart here
    flash(f'Added product {product_id} to cart (demo only).', 'success')
    return redirect(url_for('buy_sell'))

if __name__ == '__main__':
    app.run(debug=True) 