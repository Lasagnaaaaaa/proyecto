from app import app
from flask import render_template, request, redirect, url_for
from app.models import Articulo  # Updated to match the model name

@app.route('/articles')
def list_articles():
    articles = Articulo.query.all()  # Use 'Articulo' instead of 'Article'
    return render_template('article_list.html', articles=articles)

@app.route('/article/<int:id>')
def article_detail(id):
    article = Articulo.query.get(id)  # Use 'Articulo' instead of 'Article'
    return render_template('article_detail.html', article=article)



