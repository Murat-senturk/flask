from flask import Flask , render_template,request, redirect , url_for
from flask_sqlalchemy import SQLAlchemy

# flaskı başlat
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/kullanıcı/Desktop/pyhton/web/TodoApp/todo.db"

db = SQLAlchemy(app)
from sqlalchemy import Integer, String , select
from sqlalchemy.orm import Mapped, mapped_column



#tablo clası
class Todo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] 
    complete: Mapped[bool]
@app.route("/", methods=["GET"])
def index():
    db= Todo.query.all()
    return render_template("index.html",db =db)
    

@app.route("/add", methods=["POST"])
def addTodo():
    title =request.form.get("title")
    newTodo=Todo(title=title,complete=False)
    db.session.add(newTodo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/update/<string:id>")
def update(id):
    durum=Todo.query.filter_by(id = id).first()
    if   durum.complete ==True:
         durum.complete=False
    else:
        durum.complete=True
        db.session.commit()       
    return redirect(url_for("index"))
    
@app.route("/delete/<string:id>")
def remove(id):
    durum=Todo.query.filter_by(id = id).first()
    db.session.delete(durum)
    db.session.commit()
    return redirect(url_for("index"))
#güncelleme ve silme işlemi       
#   durum=Todo.query.filter_by(id = id).first()
#  db.session.delete(durum)
#  durum=Todo.query.filter_by(id = id).first()
#  durum.complete=False
#ve db.session.commit()   bu işlem
if __name__=="__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
        

        
