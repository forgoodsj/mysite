#coding=utf-8
from django.contrib import admin
from .models import Question,Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
#有model choice组成，默认是3个 TabularInline 紧密型输入框

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Date information',{'fields':['pub_date'],'classes':['collapse']}),
                 ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']#增加过滤器
    search_fields = ['question_text']
#fieldsets中每个元组的第一个元素是字段集的标题。以下是我们的对象表单现在的样子：
#你可以任意地为每个字段集指定HTML样式类。'classes': ['collapse']默认收起
#使用list_display是一个要显示的字段名称的元组，在对象的变更列表页面上作为列显示

admin.site.register(Question, QuestionAdmin)

