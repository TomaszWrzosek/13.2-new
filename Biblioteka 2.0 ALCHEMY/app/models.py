from app import db

class book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   author = db.Column(db.Text, index=True, unique=True)
   title = db.Column(db.Text, index=True, unique=True)

   def __str__(self):
       return f"<book {self.book}>"

class author(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.Text)
   author_id = db.Column(db.Integer, db.ForeignKey('book.author'))

   def __str__(self):
       return f"<Post {self.id} {self.author} ...>"