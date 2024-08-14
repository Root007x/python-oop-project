from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike


cholo_jai = RideSharing("Cholo Jai")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 1324, "Mohakhali", 1200)
cholo_jai.add_rider(rahim)

abul_huddin = Driver("Abul Uddin", "abul@gmail.com",134234,"Ghulshan")
cholo_jai.add_driver(abul_huddin)
rahim.request_ride(cholo_jai,"Uttara", "car")
abul_huddin.reach_destination(rahim.current_ride)

rahim.show_current_ride()