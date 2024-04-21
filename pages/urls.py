from django.urls import path
# from django.urls import include
# from accounts import urls
from .views import HomePageView
# from .views import calculator_view, please_login_view, booking_success_view


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    # path("book/", book_view , name="book"),
    # path("mybookings/", my_bookings_view, name="my_bookings"),
    # path("booking-success/", booking_success_view, name="booking_success"),
    # path("please-login/", please_login_view, name="please_login"),    
    # path("profile/", ProfileView.as_view(), name="profile"),
    # path("calculator/", calculator_view, name="calculator"),
]