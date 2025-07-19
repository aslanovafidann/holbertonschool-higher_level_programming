#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json():
    try:
        with open('products.json') as f:
            return json.load(f)
    except:
        return []

def read_csv():
    try:
        with open('products.csv') as f:
            reader = csv.DictReader(f)
            return [
                {'id': int(row['id']), 'name': row['name'], 'category': row['category'], 'price': float(row['price'])}
                for row in reader
            ]
    except:
        return []

def read_sql():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        rows = cursor.fetchall()
        conn.close()
        return [
            {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            for row in rows
        ]
    except:
        return []

@app.route('/products')
def products():
    source = request.args.get('source')
    prod_id = request.args.get('id', type=int)
    error = None
    data = []

    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    elif source == 'sql':
        data = read_sql()
    else:
        error = "Wrong source"

    if prod_id and not error:
        data = [p for p in data if p['id'] == prod_id]
        if not data:
            error = "Product not found"

    return render_template('product_display.html', products=data, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
