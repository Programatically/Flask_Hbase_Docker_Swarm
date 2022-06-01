from flask import Flask, url_for, redirect, render_template, request, session
import os
import Hbase_API as hbase

app = Flask(__name__)
app.secret_key = 'Programatically'



@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        pass
    else:
        return render_template('index.html')




@app.route('/service-page', methods=["POST", "GET"])
def service_page():
    if request.method == "POST":
        search_text = request.form["search"]
        session['search_text'] = search_text
        radio_filter1 = str(request.form.get("radio_filter1"))
        radio_filter2 = str(request.form.get("radio_filter2"))
        
        if radio_filter1 == 'None' and radio_filter2 == 'None':
            records = hbase.search_products(search_text)
            return render_template('service-page.html', response = records)
        elif radio_filter1 == 'on':
            records = hbase.filter_low_price(search_text)
            return render_template('service-page.html', response = records)
        elif radio_filter2 == 'on':
            records = hbase.filter_latest(search_text)
            return render_template('service-page.html', response = records)
        else:
            records = hbase.search_products(search_text)
            return render_template('service-page.html', response = records)
    else:
        return render_template('service-page.html')




@app.route('/seasonal_products', methods=["POST", "GET"])
def seasonal_products():
    if request.method == "POST":
        products = hbase.seasonal_products(str(list(request.form.keys())[0]))
        return render_template('seasonal_products.html', response = products)
    else:
        return render_template('seasonal_products.html')




@app.route('/product_page', methods=["POST", "GET"])
def product_page(param = "Hello World!"):
    if request.method == "GET":
        name = request.args.get('name')
        price = F"Price: ${request.args.get('price')}"
        custID = request.args.get('custID')

        records = hbase.search_products(custID)
        return render_template('product-page.html', response = records, _record=[price, name])
    else:
        return render_template('product-page.html')




@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        message = request.form["message"]
        is_spam = hbase.detect_spam(message)
        return render_template('contact-us.html', response = is_spam)
    else:
        return render_template('contact-us.html')




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

