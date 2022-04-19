from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid>/',views.update,name='update'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.Taskdetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.Taskupdateview.as_view(),name='cbvupdate'),
    path('cbvde lete/<int:pk>/', views.Taskdeleteview.as_view(), name='cbvdelete'),

]