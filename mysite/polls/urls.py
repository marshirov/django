from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name=''),
    path('<int:question_id>/', views.detail, name='detail'),
    #/question/122/
    path('<int:question_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    #/question/122/leave_comment/
    # ex: /polls/5/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
    ]
 