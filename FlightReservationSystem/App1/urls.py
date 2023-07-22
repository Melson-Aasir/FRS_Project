from django.urls import path

from App1 import views

urlpatterns = [
    path('', views.login_fun, name='log'),
    path('reg', views.register_fun, name='reg'),

    path('admin_home', views.adminHome_fun, name='admin_home'),
    path('addFlights', views.addFlights_fun, name='addFlights'),
    path('displayFlight', views.displayFlight_fun, name='displayFlight'),
    path('reservation', views.reservation_fun, name='reservation'),
    path('status/<int:id>', views.status_fun, name='status'),
    path('logout', views.logoutadmin_fun, name='logout'),

    path('home', views.home_fun, name='home'),
    path('FindFlights', views.findFlights_fun, name='FindFlights'),
    path('bookFlight/<int:id>', views.bookFlight_fun, name='bookFlight'),
    path('displayReservation', views.displayReservation_fun, name='displayReservation'),
    path('userLogout', views.userLogout_fun, name='userLogout')

]