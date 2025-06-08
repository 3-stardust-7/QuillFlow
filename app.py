from flask import Flask, render_template, url_for, request, redirect
from models import db, Post
from api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api.init_app(app)

@app.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:id>')
def post_details(id):
    post = Post.query.get_or_404(id)
    return render_template('post_details.html', post=post)

@app.route('/post/add', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        post = Post(title=title, content=content, author=author)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_post.html')

@app.route('/post/edit/<int:id>', methods=['GET', 'POST'])
def edit_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        post.author = request.form['author']
        db.session.commit()
        return redirect(url_for('post_details', id=post.id))
    return render_template('edit_post.html', post=post)

@app.route('/post/delete/<int:id>', methods=['GET', 'POST'])
def delete_post(id):
    post = Post.query.get_or_404(id)
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('delete_post.html', post=post)

if __name__ == '__main__':
    app.run(debug=True)
