from django.urls import path
from . import views
urlpatterns=[
    # path("",views.Maclloc.as_view(),name='maclloc'),
    path("detail/<pk>",views.detail.as_view(),name='detail'),
    path("home/",views.home.as_view(),name="maclloc"),
    path("course/",views.course.as_view(),name="course"),
    path("college_course/",views.college_course.as_view(),name="college_course"),
    path("activities/",views.activities.as_view(),name="activities"),
    path("about_us/",views.about_us.as_view(),name="about_us"),
    path(" blog/",views. blog.as_view(),name=" blog"),
    path("contact/",views.contact.as_view(),name='contact'),
]

