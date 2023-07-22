from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from App1.models import Customer, FlightDetails, Flights, ArrivalCities, DestinationCities, ReservationDetails


#  Register
def register_fun(request):
    if request.method == 'POST':
        c1 = Customer()
        c1.customer_name = request.POST['txt_username']
        c1.customer_email = request.POST['txt_email']
        c1.customer_phno = request.POST['txt_phn']
        c1.customer_password = request.POST['txt_pwd']
        c1.Date_Of_Birth = request.POST['']
        c1.Gender = request.POST['']

        if authenticate(username=request.POST["txt_username"], password=request.POST['txt_pwd']) is not None:
            return render(request, 'register.html', {'msg': 'username already exists'})
        elif Customer.objects.filter(customer_name=request.POST["txt_username"]).exists():
            return render(request, 'register.html', {'msg': 'username already exists'})
        elif Customer.objects.filter(customer_email=request.POST["txt_email"]).exists():
            return render(request, 'register.html', {'msg': 'email already exists'})
        else:
            c1.save()
            return redirect('log')
    else:
        return render(request, 'register.html', {'msg': ''})


# Login
def login_fun(request):
    if request.method == 'POST':
        name = request.POST['username']
        pwd = request.POST['Password']
        user = authenticate(username=name, password=pwd)

        if user is not None:
            if user.is_superuser:
                login(request, user)
                request.session['Name'] = name
                return redirect('admin_home')
        elif Customer.objects.filter(
                Q(customer_name=request.POST["username"])
                & Q(customer_password=request.POST["Password"])).exists():
            request.session['Name'] = name
            return redirect('home')
        else:
            return render(request, 'login.html', {'msg': 'enter proper credentials'})
    else:
        return render(request, 'login.html', {'msg': ''})

        # try:
        #     user1 = Customer.objects.get(customer_name=u_name)
        #     if check_password(u_pwd, user1.customer_password):
        #         request.session['Name'] = u_name
        #         # Passwords match, perform login logic here
        #         return render(request, 'home.html')
        #     else:
        #         # Passwords do not match, handle invalid login
        #         return render(request, 'login.html', {'msg': 'Enter proper username and password'})
        # except ObjectDoesNotExist:
        #     # User does not exist, handle invalid login
        #
        #     if user is not None:
        #         if user.is_superuser:
        #             login(request, user)
        #             request.session['Name'] = u_name
        #             return redirect('admin_home')
        #     else:
        #         return render(request, 'login.html', {'msg': 'Enter proper username and password'})
        #
        # if user is not None:
        #     if user.is_superuser:
        #         login(request, user)
        #         request.session['Name'] = u_name
        #         return redirect('admin_home')
        #     else:
        #         login(request, user)
        #         request.session['Name'] = u_name
        #         return redirect('home')
        # else:
        #     return render(request, 'login.html', {'msg': 'Enter proper username and password'})

    # if user is not None:
    #         if user.is_superuser:
    #             login(request, user)
    #             request.session['Name'] = u_name
    #             return redirect('admin_home')
    #         else:
    #             login(request, user)
    #             request.session['Name'] = u_name
    #             return redirect('home')
    #     elif customer is not None:
    #         request.session['Name'] = u_name
    #         return redirect('home')
    #     else:
    #         return render(request, 'login.html', {'msg': 'Enter proper username and password'})
    # else:
    # return render(request, 'login.html', {'msg': ''})
    # return redirect('home')


# Admin page fun
@login_required
@never_cache
def adminHome_fun(request):
    return render(request, 'admin_home.html', {'data': request.session['Name']})


@login_required
@never_cache
def addFlights_fun(request):
    if request.method == 'POST':
        f1 = FlightDetails()
        f1.Flight_number = request.POST['txtFlightNum']
        f1.Flight_name = Flights.objects.get(FlightName=request.POST['ddlFlightName'])
        f1.Arrival_city = ArrivalCities.objects.get(A_City=request.POST['ddlArrivalCity'])
        f1.Destination_city = DestinationCities.objects.get(D_City=request.POST['ddlDestCity'])
        f1.Date = request.POST['txtDate']
        f1.Cost = request.POST['txtCost']

        datetime_string = request.POST['txtTime']
        datetime_value = datetime_string.split('T')  # taking only time from the textbox

        f1.Arrival_time = datetime_value[-1]
        f1.save()
        return redirect('addFlights')
    else:
        destination_city = DestinationCities.objects.all()
        arrival_city = ArrivalCities.objects.all()
        flight = Flights.objects.all()
        return render(request, 'admin_page/addFlights.html', {'msg': '',
                                                              'Destination_city': destination_city,
                                                              'Arrival_city': arrival_city,
                                                              'Flight': flight
                                                              })


@login_required
@never_cache
def displayFlight_fun(request):
    f1 = FlightDetails.objects.all()
    return render(request, 'admin_page/displayFlights.html', {'data': f1})


@login_required
@never_cache
def reservation_fun(request):
    r1 = ReservationDetails.objects.all()
    return render(request, 'admin_page/display_reserve.html', {'data': r1})


@login_required
@never_cache
def status_fun(request, id):
    r1 = ReservationDetails.objects.get(id=id)
    if request.method == 'POST':
        r1.booking_status = request.POST['txtStatus']
        r1.save()
        return redirect('reservation')
    else:
        return render(request, 'admin_page/status.html', {'data': r1})


def logoutadmin_fun(request):
    logout(request)
    return redirect('log')


# customer page url functions

@never_cache
def home_fun(request):
    return render(request, 'home.html', {'data': request.session['Name']})


def findFlights_fun(request):
    dest_city = DestinationCities.objects.all()
    arrival_city = ArrivalCities.objects.all()
    if request.method == 'POST':
        arrival_city = request.POST['ddlArrivalCity']
        destination_city = request.POST['ddlDestinationCity']
        date = request.POST['txtDate']
        data = FlightDetails.objects.filter(Arrival_city=ArrivalCities.objects.get(A_City=arrival_city)
                                            , Destination_city=DestinationCities.objects.get(
                D_City=destination_city), Date=date)
        # print(data)
        if data.count() != 0:
            return render(request, 'customer/FindFlights.html', {
                'data': data, 'value': True,
                'dest_city': dest_city,
                'arrival_city': arrival_city,
            })
        else:
            return render(request, 'customer/FindFlights.html', {
                'data': '', 'value': False,
                'dest_city': dest_city,
                'arrival_city': arrival_city,
            })
    else:
        return render(request, 'customer/FindFlights.html', {
            'dest_city': dest_city,
            'arrival_city': arrival_city,
            'data': '', 'value': ''
        })


@never_cache
def bookFlight_fun(request, id):
    flights = FlightDetails.objects.get(id=id)
    if request.method == 'POST':
        r1 = ReservationDetails()
        r1.First_name = request.POST['txtFName']
        r1.Last_name = request.POST['txtLName']
        r1.Age = request.POST['txtAge']
        r1.Phno = request.POST['txtPhNo']
        r1.Flight_details = flights
        r1.Booking_status = False
        r1.Customer_id = Customer.objects.get(customer_name=request.session['Name'])
        r1.save()
        return redirect('displayReservation')
    else:
        return render(request, 'customer/reservation.html', {'data': flights})


@never_cache
def displayReservation_fun(request):
    r1 = ReservationDetails.objects.filter(Customer_id=Customer.objects.get(customer_name=request.session['Name']))
    return render(request, 'customer/displayReservation.html', {'data': r1})


@never_cache
def userLogout_fun(request):
    del request.session['Name']
    return redirect('log')
