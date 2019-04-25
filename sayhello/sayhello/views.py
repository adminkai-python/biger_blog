from sayhello import app
from flask import render_template,url_for,redirect,flash
from sayhello.forms import CommentForm
from sayhello.models import Comment
from sayhello import db

# 首页
@app.route("/",methods=["GET","POST"])
def index():

    comment_form = CommentForm()
    comments = Comment.query.order_by(Comment.time.desc()).all()
    print("get请求")
    if comment_form.validate_on_submit():
        name = comment_form.name.data
        comment = comment_form.comment.data
        comment_mysql = Comment(name=name,comment=comment)
        db.session.add(comment_mysql)
        db.session.commit()
        return redirect(url_for("index"))

    return render_template("index.html",comment_form=comment_form,comments=comments)
