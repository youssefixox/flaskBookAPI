from flask import Flask , request , make_response,render_template
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from functools import wraps

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
   id=db.Column(db. Integer,primary_key=True)
   name=db.Column(db.String(80), unique=True, nullable=False)
   description=db.Column(db.String(120))
   def __repr__(self):
        return f"{self.name}-{self.description}"


#decorators for http basic authentication
def auth_required(f):
      @wraps(f)
      def decorated(*args,**kwargs):
          auth= request.authorization
          if auth and auth.username=="admin" and auth.password=="admin":
             return f(*args,**kwargs)

          return make_response("could not verify your login !",401,{'WWW-Authenticate':'Basic realm="Login required"'})

      return decorated


#home page
@app.route("/")
@auth_required
def home():
   return render_template("index.html")


#get books
@app.route("/books")
def get_books():
   #return {"books":"books data"}
   books = Book.query.all()

   output=[]
   for book in books:
      book_data={'name':book.name,'description':book.description}
      output.append(book_data)
   return {"books": output}


#get book
@app.route("/books/<id>")
def get_book(id):
   book=Book.query.get_or_404(id)
   return jsonify({"name":book.name,"description":book.description})


#add books
@app.route("/books",methods=['POST'])
@auth_required
def add_book():

   content_type = request.headers.get('Content-Type')

   if (content_type == 'application/json'):

      book = Book(name=request.json["name"],description=request.json["description"])
      db.session.add(book)
      db.session.commit()
      return {"message":"success"}

   else:
      return 'Content-Type not supported!'

#delete books
@app.route("/books/<id>",methods=['DELETE'])
@auth_required
def delete_book(id):
   book = Book.query.get(id)
   if book is None:
       return {"error":"not found"}
   db.session.delete(book)
   db.session.commit()
   return {"message":"deleted"}

if __name__ == "__main__":
   context = ('ssl.cert', 'ssl.key')
   app.run(host='0.0.0.0',ssl_context=context)


