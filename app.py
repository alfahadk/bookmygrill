from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    date = request.form['date']
    location = request.form['location']
    charcoal_qty = float(request.form.get('charcoal_qty', 0))

    grill_price = 500
    charcoal_price = 70 * charcoal_qty
    total = grill_price + charcoal_price

    return f"""
    <h2>Booking Confirmed ✅</h2>
    <p>Thank you, <b>{name}</b>!</p>
    <p>Your Alpham Grill is booked for <b>{date}</b> at <b>{location}</b>.</p>
    <p>Charcoal added: <b>{charcoal_qty} kg</b> (₹70/kg)</p>
    <h3>Total Payment: ₹{total}</h3>
    <a href='/'>Back to Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
