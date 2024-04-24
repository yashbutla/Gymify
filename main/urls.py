from django.urls import path
from main import views

urlpatterns = [
    path('',views.index,name='home'),
    path('members',views.members,name='members'),
    path('products',views.products,name='products'),
    path('mailing',views.mailing,name='mailing'),
    path('analytics',views.analytics,name='analytics'),
    path('attendance',views.attendance,name='attendance'),
    path('create_member',views.create_member,name='create_member'),
    path('member_info',views.member_info,name='member_info'),
    path('store',views.store,name='store'),
    path('export_all',views.export_all,name='export_all'),
    path('email',views.email,name='email'),
    path('search/', views.search_data, name='search_data'),
    path('sort_data/', views.sort_data, name='sort_data'),
]