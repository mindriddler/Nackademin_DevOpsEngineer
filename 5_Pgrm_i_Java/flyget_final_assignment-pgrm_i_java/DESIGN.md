# Class diagram
```mermaid
classDiagram
%% classes
class Plane{
    -List<Booking> bookings
    +Plane()
    +bookSeat(String seatId, Person person) : boolean
    +cancelBooking(String seatId) : boolean
    +isSeatBooked(String seatId) : boolean
    +getBookings() : List<Booking>
    +loadBookings() : void
    +getPassengerInfo() : List<Person>
}

class Person {
    -firstName: String
    -lastName: String
    -birthdate: LocalDate
    +getFirstName(): String
    +getLastName(): String
    +getBirthdate(): LocalDate
    +getFullName(): String
}

class Booking {
    -seatPlan: SeatPlan
    +bookSeat(seat: Seat, passenger: Person): boolean
    +cancelBooking(seat: Seat): boolean
    +getPassengerInfo(seatId: String): Person
}

class Seat {
    -isBooked: boolean
    -passenger: Person
    -seat: String
    +Seat(rowNum: String, seatNum: char)
    +getIsBooked(): boolean
    +setIsBooked(isBooked: boolean)
    +getPassenger(): Person
    +setPassenger(passenger: Person)
    +getSeat(): String
    +bookSeat(passenger: Person): boolean
    +cancelBooking(): boolean
    +getSeatIdFromUser(plane: Plane, sc: Scanner): String
}

class SeatDisplay {
    -seatPlan: SeatPlan
    +display()
}

class SeatPlan {
    -seats: Map<String, Seat>
    +SeatPlan()
    +getSeats(): Map<String, Seat>
    +setSeats(seats: Map<String, Seat>)
    +getSeat(seat: Object): Seat
    +getAvailableSeats(): List<Seat>
    +getBookedSeats(): List<Seat>
}

class Utilities {
    +simulate(Plane, SeatPlan): int
    +generateNameForSim(): String[]
    +generateBirthdateForSim(): LocalDate
    +generatePersonForSim(): Person
}

%% relationships

Booking *-- SeatPlan
Booking --> Person
Seat --> Person
Seat --> Plane
SeatDisplay --> SeatPlan
SeatPlan *-- Seat
Utilities --> Plane
Utilities --> SeatPlan
Utilities --> Person
```
```bash
"*--" Booking has a composition relationship with SeatPlan, as it contains a SeatPlan object.
"-->" Booking has an association relationship with Person, as it uses Person objects to book seats.
"-->" Seat has an association relationship with Person, as it contains a Person object representing the passenger who booked it.
"-->" Seat has an association relationship with Plane, as it uses a Plane object to check if a seat is booked or not.
"-->" SeatDisplay has an association relationship with SeatPlan, as it uses a SeatPlan object to display the seat plan of a plane.
"*--" SeatPlan has a composition relationship with Seat, as it contains a map of Seat objects.
"-->" Utilities has an association relationship with Plane and SeatPlan, as it uses these objects to simulate bookings.
"-->" Utilities has an association relationship with Person, as it uses Person objects to generate random bookings.
```
# NOUNS
```bash
* Plane
* Person
* Booking
* InvalidSeatException
* Seat
* SeatDisplay 
* SeatPlan
* Utilities
```
# VERBS
```bash
* Load bookings
* Check if seat is booked
* Get FirstName
* Get LastName
* Get birthdate
* Get fullName
* Book a seat
* Cancel a booking
* Get passenger inforomation
* Set a seat as booked
* Get passenger of a seat
* Set passenger of a seat
* Get seat id from user
* Display seat plan
* Simulate
* Generate name for siumlation
* Generate birthdate for simulation
* Generate person for simulation
* Get a list of all passengers
```

    
