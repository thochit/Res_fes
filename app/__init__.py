from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
ceramics = [
    {
        'title': 'Ceramic Bowl',
        'description': 'A beautiful ceramic bowl perfect for serving salads.',
        'image': 'ceramic_bowl.jpg'
    },
    {
        'title': 'Ceramic Vase',
        'description': 'An elegant ceramic vase that adds charm to any room.',
        'image': 'ceramic_vase.jpg'
    },
    {
        'title': 'Ceramic Mug',
        'description': 'A cozy ceramic mug for enjoying your favorite hot beverages.',
        'image': 'ceramic_mug.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', ceramics=ceramics)

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/ceramic_restoration')
def ceramic_restoration():
    return render_template('ceramic_restoration.html')

@app.route('/ceramics/<int:ceramic_id>')
def ceramic_details(ceramic_id):
    if ceramic_id < len(ceramics):
        ceramic = ceramics[ceramic_id]
        return render_template('ceramic_details.html', ceramic=ceramic)
    else:
        return 'Ceramic not found'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Handle the form submission
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Code for sending the message or saving it to a database
        return redirect('/')
    return render_template('contact.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    # Handle the form submission and send the message
    return redirect(url_for('contact'))