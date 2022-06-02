import happybase


connection = happybase.Connection('hbase-docker', port=9090, autoconnect=True)


# FETCHING LIST OF ALL TABLES IN DB
def fetch_table():
    return connection.tables()




# SEACHING FOR A PRODUCT
def search_products(search_text="SHIRT"):
    table = connection.table('productss')
    products = []

    for key, data in table.scan():
        if len(products) == 6: break
        if search_text in str(data):
            id = key.decode('utf-8')
            _product = [id]
            for val1, val2 in data.items():
                val1 = val2.decode('utf-8')
                _product.append(val1)
            products.append(_product)
    return products




# SORTING PRODUCTS BY LOW PRICE
def filter_low_price(search_text="CLOCK"):
    products = search_products(search_text)
    elm = 4
    products.sort(key=lambda x: x[elm])
    return products




# SORTING PRODUCTS BY LATEST
def filter_latest(search_text="METAL"):
    products = search_products(search_text)
    elm = 2
    products.sort(key=lambda x: x[elm])
    return products




# FETCHING RELATED PRODUCTS
def related_products(CustomerID='16425'):
    table = connection.table('productss')
    products = []

    for key, data in table.scan():
        if len(products) == 5: break
        if CustomerID in str(data):
            id = key.decode('utf-8')
            _product = [id]
            for val1, val2 in data.items():
                val1 = val2.decode('utf-8')
                _product.append(val1)
            products.append(_product)
    return products




# FETCHING RECORDS ACCORDING TO SEASON
def seasonal_products(season="Summer"):
    global months
    if season == "Summer":
        months = [5, 6, 7]
    elif season == "Winter":
        months = [12, 1, 2]
    elif season == "Autumn":
        months = [9, 10, 11]
    elif season == "Spring":
        months = [3, 4, 5]

    table = connection.table('products')
    products = []

    for key, data in table.scan():
        id = key.decode('utf-8')
        _product = [id]
        for val1, val2 in data.items():
            val1 = val2.decode('utf-8')
            _product.append(val1)
        products.append(_product)
    products.pop()

    for _record in products:
        _month = str(_record[1]).split('/')
        if int(_month[1]) not in months:
            products.remove(_record)
    return products[0:6]




# DETECTION SPAM MESSAGES
def detect_spam(message="WINNER"):
    table = connection.table('spam')

    for key, data in table.scan():
        if message in str(data):
            return "SPAM"
    return "NOT SPAM"