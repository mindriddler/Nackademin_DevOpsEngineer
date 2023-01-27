package my.project;

/**
 * 
 * InvalidSeatException is thrown when an invalid seat is attempted to be
 * booked.
 * This exception is thrown when the seat is already booked or does not exist in
 * the seating plan.
 */
public class InvalidSeatException extends Exception {

    public InvalidSeatException() {
        super("Invalid seat!");
    }
}
