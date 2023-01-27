package my.project;

import java.util.Map;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

/**
 * 
 * The seatPlan class represents the seating plan of a plane. It contains a
 * map of seat objects with their corresponding row and column IDs as keys.
 * 
 * The class provides methods to get and set the seats, get a specific seat, get
 * a list of available seats, and get a list of booked seats.
 */
public class SeatPlan {
    private Map<String, Seat> seats;

    /**
     * 
     * Constructor for the seatPlan class.
     * Initializes the seats with a map of seat objects with their corresponding row
     * and column IDs as keys.
     */
    public SeatPlan() {
        seats = new HashMap<String, Seat>();
        for (int i = 1; i <= 30; i++) {
            for (char c = 'A'; c <= 'F'; c++) {
                seats.put(i + "" + c, new Seat(i + "", c));
            }
        }
    }

    /**
     * 
     * Returns the map of seats in the seating plan.
     * 
     * @return Map of seats in the seating plan.
     */
    public Map<String, Seat> getSeats() {
        return seats;
    }

    /**
     * 
     * Sets the map of seats in the seating plan.
     * 
     * @param seats Map of seats to be set in the seating plan.
     */
    public void setSeats(Map<String, Seat> seats) {
        this.seats = seats;
    }

    /**
     * 
     * Returns a specific seat in the seating plan, identified by its row and column
     * ID.
     * 
     * @param seat Row and column ID of the seat to be returned.
     * @return Specific seat in the seating plan.
     */
    public Seat getSeat(Object seat) {
        return seats.get(seat);
    }

    /**
     * 
     * Returns a list of available seats in the seating plan.
     * 
     * @return List of available seats in the seating plan.
     */
    public List<Seat> getAvailableSeats() {
        List<Seat> availableSeats = new ArrayList<>();
        for (Seat seat : seats.values()) {
            if (!seat.getIsBooked()) {
                availableSeats.add(seat);
            }
        }
        return availableSeats;
    }

    /**
     * 
     * Returns a list of booked seats in the seating plan.
     * 
     * @return List of booked seats in the seating plan.
     */
    public List<Seat> getBookedSeats() {
        List<Seat> bookedSeats = new ArrayList<>();
        for (Seat seat : seats.values()) {
            if (seat.getIsBooked()) {
                bookedSeats.add(seat);
            }
        }
        return bookedSeats;
    }

}
