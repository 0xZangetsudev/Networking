import psycopg2
from flask import Flask, render_template
conn = psycopg2.connect(
        host="localhost",
        port="XXXX",
        database="XXXX",
        user="XXXX",
        password="XXXXX"
        )
app = Flask(__name__)
@app.route('/')
def show_data():
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM users;")
        data = cur.fetchall()
        cur.close()
        print(data)
        return render_template('data.html', data=data)
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data from PostgreSQL:", error)
        return "An error occurred while fetching data"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

