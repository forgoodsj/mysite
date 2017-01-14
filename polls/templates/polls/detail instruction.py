__author__ = 'jun'
#coding=utf-8
'''
在detail网页模板中，我们为Question对应的每个Choice都添加了一个单选按钮用于选择。
每个单选按钮的value属性是对应的各个Choice的ID。每个单选按钮的name是"choice"。
这意味着，当有人选择一个单选按钮并提交表单提交时，它将发送一个POST数据choice=#，
其中# 为选择的Choice的ID。这是HTML 表单的基本概念。

我们设置表单的action为{% url 'polls:vote' question.id %}，
并设置 method="post"。使用method="post"（与其相对的是method="get"）是非常重要的，
因为这个提交表单的行为会改变服务器端的数据。
无论何时，当你需要创建一个改变服务器端数据的表单时，请使用 method="post"。
这不是Django的特定技巧；这是优秀的网站开发实践。

forloop.counter指示for标签已经循环多少次。

由于我们创建一个POST表单（它具有修改数据的作用），所以我们需要小心跨站点请求伪造。
 谢天谢地，你不必太过担心，因为Django已经拥有一个用来防御它的非常容易使用的系统。
 简而言之，所有针对内部URL的POST表单都应该使用{% csrf_token %}模板标签。
现在，让我们来创建一个Django视图来处理提交的数据。 记住，在教程 3中，
我们为投票应用创建了一个URLconf ，包含这一行：
'''