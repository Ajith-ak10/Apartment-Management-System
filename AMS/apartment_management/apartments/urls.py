from django.urls import path
from .views import register, user_login, user_logout, home, submit_complaint, make_payment
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('complaint/', submit_complaint, name='submit_complaint'),
    path('payment/', make_payment, name='make_payment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)