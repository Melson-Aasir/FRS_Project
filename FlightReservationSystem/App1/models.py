from django.db import models


class ArrivalCities(models.Model):
    A_City = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.A_City}'


class DestinationCities(models.Model):
    D_City = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.D_City}'


class Flights(models.Model):
    FlightName = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.FlightName}'


class Airlines(models.Model):
    Name_Of_Airline = models.CharField(max_length=50, unique=True)
    Logo = models.ImageField()
    Date_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Name_Of_Airline}"


class Airport(models.Model):
    Airport_Name = models.CharField(max_length=100, unique=True)
    Location = models.CharField(max_length=100)
    Date_Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.Airport_Name},{self.Location}"


# class Seat(models.Model):
#     Seat_Type = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f"{self.Seat_Type}"


class FlightDetails(models.Model):
    Flight_number = models.CharField(max_length=100)
    Flight_name = models.ForeignKey(Airlines, on_delete=models.CASCADE)
    Arrival_city = models.ForeignKey(ArrivalCities, on_delete=models.CASCADE)
    Destination_city = models.ForeignKey(DestinationCities, on_delete=models.CASCADE)
    Arrival_Date_Time = models.DateTimeField(auto_now=False, auto_now_add=False)
    Departure_Date_Time = models.DateTimeField(auto_now=False, auto_now_add=False)
    Economy_Seat = models.IntegerField(default=0)  # Provide the default value here
    Economy_Cost = models.FloatField()
    Business_Seat = models.IntegerField(default=0)  # Provide the default value here
    Business_Cost = models.FloatField()

    def __str__(self):
        return f"{self.Flight_number},{self.Flight_name},{self.Arrival_city},{self.Destination_city},{self.Arrival_Date_Time},{self.Departure_Date_Time},{self.Business_Seat},{self.Business_Cost},{self.Economy_Cost},{self.Economy_Seat}"


class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_phno = models.BigIntegerField()
    customer_password = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    Date_Of_Birth = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.customer_name}"


class ReservationDetails(models.Model):
    Flight_details = models.ForeignKey(FlightDetails, on_delete=models.CASCADE)
    First_name = models.CharField(max_length=100)
    Middle_name = models.CharField(max_length=50, null=True)
    Last_name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email_id = models.EmailField()
    Gender = models.CharField(max_length=100)
    Phno = models.BigIntegerField()
    Booking_status = models.BooleanField()
    Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.Flight_details},{self.First_name},{self.Middle_name},{self.Last_name},{self.Age},{self.Gender}," \
               f"{self.Phno},{self.Email_id},{self.Booking_status},{self.Customer_id}"

