from app import app, db
from app.models import book, author

@app.shell_context_processor
def make_shell_context():
   return {
       "db": db,
       "Book": book,
       "Author": author,
   }