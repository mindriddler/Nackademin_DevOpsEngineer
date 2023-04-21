package my.project;

import java.util.Map;

/**
 * 
 * The Plane class represents an airplane with a seating plan.
 * 
 * It allows for the display of the seating plan, booking and canceling of
 * seats,
 * 
 * displaying a list of passengers, saving and loading bookings,
 * 
 * and checking if a seat is booked.
 */
public class Plane {
    public SeatPlan seatPlan;
    private Booking seatBooking;
    private SeatDisplay seatDisplay;
    private PassengerDisplay passengerDisplay;
    private BookingSaverLoader bookingSaverLoader;
    private Booking booking;

    /**
     * 
     * Creates a new Plane object with a new seatPlan, Booking, seatDisplay,
     * PassengerDisplay, and BookingSaverLoader object.
     */
    public Plane() {
        seatPlan = new SeatPlan();
        seatBooking = new Booking(seatPlan);
        seatDisplay = new SeatDisplay(seatPlan);
        passengerDisplay = new PassengerDisplay(seatPlan);
        bookingSaverLoader = new BookingSaverLoader(seatPlan, Utilities.BOOKINGS_FILE_PATH);
        booking = new Booking(seatPlan);
    }

    /**
     * 
     * Returns the seating plan of the plane
     * 
     * @return the seatPlan object of the plane
     */
    public SeatPlan getseatPlan() {
        return seatPlan;
    }

    /**
     * 
     * Returns the seats of the plane
     * 
     * @return the seats of the plane
     */
    public Map<String, Seat> getSeats() {
        return seatPlan.getSeats();
    }

    public void displaySeats() {
        seatDisplay.display();
    }

    /**
     * 
     * Books a seat for a person
     * 
     * @param seat   the seat to be booked
     * @param person the person booking the seat
     * @return true if the seat was booked, false if the seat was already booked
     */
    public boolean bookSeat(Seat seat, Person person) {
        return booking.bookSeat(seat, person);
    }

    /**
     * 
     * Cancels a booking for a seat
     * 
     * @param seatId the id of the seat whose booking is to be canceled
     * @return true if the booking was canceled, false if the seat was not booked
     */
    public boolean cancelBooking(String seatId) {
        return seatBooking.cancelBooking(seatId);
    }

    public void displayPassengerList() {
        passengerDisplay.displayPassengerInformation();

    }

    public void saveBookings() {
        bookingSaverLoader.save();
    }

    public void loadBookings(String fileName) {
        bookingSaverLoader.load(fileName);
    }

    /**
     * 
     * Checks if a seat is booked
     * 
     * @param seatId the id of the seat to check
     * @return true if the seat is booked, false if the seat is not booked
     * @throws InvalidSeatException if the seat id is invalid
     */
    public boolean isSeatBooked(String seatId) throws InvalidSeatException {
        if (seatPlan.getSeat(seatId) == null) {
            throw new InvalidSeatException();
        }
        return seatPlan.getSeat(seatId).getIsBooked();
    }
}
