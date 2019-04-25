from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import DataRequired,Length

class CommentForm(FlaskForm):
    name = StringField("名字",validators=[DataRequired(message="无效数据"),Length(1,10,message="名字不能超过10位")],render_kw={"placeholder":"请输入您的名字或昵称"})
    comment = TextAreaField("留言内容",validators=[DataRequired(message="无效数据"),Length(1,2000,message="留言内容不能超过2000字")])
    submit = SubmitField(render_kw={"value":"提交"})



