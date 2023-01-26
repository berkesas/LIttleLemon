Index view
/restaurant/

Menuitems
/restaurant/api/menuitems/
/restaurant/api/menuitems/<int:pk>

Get a token by submitting username/password pair
/restaurant/api/api-token-auth/

Bookings
/restaurant/api/bookings/tables/

With token authentication you can test POST

{
    "name": "Jennifer Smith",
	"no_of_guests": 8,
	"booking_date": "2023-01-26T18:10:39.514843Z"
}

Delete a booking - DELETE
/api/bookings/tables/<int:pk>

Update a booking - PUT
api/bookings/tables/<int:pk>/