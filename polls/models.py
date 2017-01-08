#coding=utf-8
from django.db import models

# polls应用的模型
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
'''
每个模型都用一个类表示，该类继承自django.db.models.Model。每个模型都有一些类变量，在模型中每个类变量都代表了数据库中的一个字段。

每个字段通过Field类的一个实例表示 —— 例如字符字段CharField和日期字段DateTimeField。这种方法告诉Django，每个字段中保存着什么类型的数据。

每个Field 实例的名字（例如question_text 或 pub_date）就是字段的名字，并且是机器可读的格式。你将在Python代码中使用到它的值，并且你的数据库将把它用作表的列名。

我们使用ForeignKey定义了一个关联。它告诉Django每个Choice都只关联一个Question。Django支持所有常见的数据库关联：多对一、多对多和一对一。
'''