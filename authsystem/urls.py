
from django.contrib import admin
from django.urls import path,include
from authapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base_view),
    path('login/',views.login_view),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup_view)
]
