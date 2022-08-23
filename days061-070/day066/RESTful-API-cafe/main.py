from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from jsonrpcserver import method
from sklearn.covariance import oas

app = Flask(__name__)


##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)
    
    def to_dict(self) -> dict:
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    def column_names(self) -> list:
        return [column.name for column in self.__table__.columns]


@app.route("/")
def home():
    return render_template("index.html")
    

## HTTP GET - Read Record

@app.route("/random", methods=["GET"])
def random():
    """Fetch a random Cafe record as JSON from the database using SQLAlchemy:"""
    return Cafe.query.order_by(db.func.random()).first().to_dict()

@app.route("/all", methods=["GET"])
def all():
    """Return all cafes in the database as JSON"""
    return jsonify([cafe.to_dict() for cafe in Cafe.query.all()])

@app.route("/search", methods=["GET"])
def search():
    """
    Search for a cafe by name
    
    GET Request Params:
        - name: The name of the cafe to search for
        - location: The location of the cafe to search for 
    """
    name = request.args.get("name")
    location = request.args.get("location")
    if name is None and location is None:
        return {"error": "Value required for either or both parameters 'name' & 'location'"}, 404
    
    query = Cafe.query
    if name is not None:
        query = query.filter(Cafe.name.contains(name))
    if location is not None:
        query = query.filter(Cafe.location.contains(location))
    # result = [cafe.to_dict() for cafe in Cafe.query.filter(Cafe.name.contains(name))]
    result = [cafe.to_dict() for cafe in query]
    if len(result) == 0:
        return {"error": f"No cafes found related to the name '{name}'"}, 404
    
    return jsonify(result), 200

## HTTP POST - Create Record

@app.route("/add", methods=["POST"])
def post_new_cafe():
    try:        
        new_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=str(request.form.get("sockets")).lower() == "true",
            has_toilet=str(request.form.get("toilet")).lower() == "true",
            has_wifi=str(request.form.get("wifi")).lower() == "true",
            can_take_calls=str(request.form.get("calls")).lower() == "true",
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 200
    except Exception as exc:
        return {"error": f"An internal server error occurred when attempting to add the Cafe to the database - {exc}"}, 500
    
## HTTP PUT/PATCH - Update Record

@app.route("/update-price/<int:cafe_id>", methods=["PUT", "PATCH"])
def update_price(cafe_id: int):
    """
    Update the price of coffee at a cafe
    
    Query Params:
        - coffee_price: The new price of coffee at the cafe
    """
    try:
        cafe = Cafe.query.filter_by(id=cafe_id).first()
        if cafe is None:
            return {"error": f"No cafe found with the ID '{cafe_id}'"}, 404
        prev_price = cafe.coffee_price
        cafe.coffee_price = request.args.get("coffee_price")
        db.session.commit()
        return jsonify(response={"success": f"Successfully updated the coffee price from {prev_price} to {cafe.coffee_price} for cafe '{cafe.name}'"}), 200
    except Exception as exc:
        return {"error": f"An internal server error occurred when attempting to update the coffee price for cafe '{cafe.name}' - {exc}"}, 500

## HTTP DELETE - Delete Record

@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed(cafe_id: int):
    """Ensure that the user has 'TopSecretAPIKey' as their api_key query parameter, then delete the cafe from the database"""
    if request.args.get("api_key") != "TopSecretAPIKey":
        return {"error": "Invalid API Key"}, 400
    cafe = Cafe.query.filter_by(id=cafe_id).first()
    if cafe is None:
        return {"error": f"No cafe found with the ID '{cafe_id}'"}, 404
    
    try:
        db.session.delete(cafe)
        db.session.commit()
        return {"success": f"Successfully deleted the cafe with id '{cafe_id}'"}, 200
    except Exception as exc:
        return {"error": f"An internal server error occurred when attempting to delete the cafe with id '{cafe_id}' - {exc}"}, 500
    
    

if __name__ == '__main__':
    app.run(debug=True)
