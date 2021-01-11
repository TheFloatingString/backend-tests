from flask import Flask 
from db.models import Article

from sqlalchemy	import create_engine
from sqlalchemy.orm import sessionmaker

import os 

app = Flask(__name__)

engine = create_engine(os.environ["DATABASE_URL"], echo = True)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()
session.rollback()

@app.route("/")
def home():
	return "home"

@app.route("/api/get_all_articles")
def get_all_articles():
	return_dict = dict()
	counter = 0
	for article in session.query(Article):
		return_dict[counter] = {"uuid":article.uuid, "title":article.title}
		counter += 1
	return return_dict

@app.route("/api/get_article/<article_uuid>")
def get_article(article_uuid):
	return_dict = dict()
	for article in session.query(Article):
		if str(article.uuid) == article_uuid:
			return_dict = {"title": article.title, "content": article.content}
			break
	return return_dict

if __name__ == "__main__":

	for article in session.query(Article):
		print("===")
		print(article.uuid, article.title)

	app.run(host="0.0.0.0", port=5000)