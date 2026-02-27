from flask import Flask,render_template
app=Flask(__name__)
@app.route("/",methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/get-data",methods=["GET"])
def get_data():
    @app.route("/get-data", methods = ["GET"])
    db = mysql.connector.connect(
        host="localhost",
        user= "root",
        password= "root",
        database= "flask_app"
    )


    cursor = db.cursor()
    cursor.execute("SELECT * FROM users_auth")

    data = cursor.fetchall()

    return jsonify(data)
if __name__=="__main__":
    app.run(debug=True) 
   
