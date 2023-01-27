package my.project;

import java.io.Serializable;
import java.util.Scanner;

/**
 * 
 * The Seat class represents a seat on a plane. It contains information about
 * whether the seat is booked and who the passenger is.
 * 
 * It also includes methods for booking and cancelling a seat.
 */
class Seat implements Serializable {
    private boolean isBooked;
    private Person passenger;
    private String seat;

    /**
     * 
     * Creates a new seat object with the given seat identifier.
     * 
     * @param rowNum  the row number of the seat
     * @param seatNum the seat number within the row
     */
    public Seat(String rowNum, char seatNum) {
        this.isBooked = false;
        this.seat = rowNum + seatNum;
    }

    public boolean getIsBooked() {
        return isBooked;
    }

    public void setIsBooked(boolean isBooked) {
        this.isBooked = isBooked;
    }

    public Person getPassenger() {
        return passenger;
    }

    public void setPassenger(Person passenger) {
        this.passenger = passenger;
    }

    public String getSeat() {
        return this.seat;
    }

    /**
     * 
     * Books the seat for the provided passenger
     * 
     * @param passenger an object of type Person representing the passenger who is
     *                  booking the seat
     * @return true if the booking is successful and false otherwise
     */
    public boolean bookSeat(Person passenger) {
        this.passenger = passenger;
        return this.isBooked = true;
    }

    /**
     * 
     * Cancels the booking of the current seat
     * 
     * @return true if the cancellation is successful and false otherwise
     */
    public boolean cancelBooking() {
        if (isBooked) {
            isBooked = false;
            passenger = null;
            return true;
        }
        return false;
    }

    /**
     * 
     * Gets the seat id from the user and checks if it's booked
     * 
     * @param plane an object of type Plane representing the plane
     * @param sc    a Scanner object for reading user input
     * @return seatId a string representing the seat id
     * @throws InvalidSeatException if the seat id entered is invalid
     */
    public static String getSeatIdFromUser(Plane plane, Scanner sc) throws InvalidSeatException {
        String seatId = "";
        boolean isBooked = true;
        while (isBooked) {
            System.out.print("\nEnter seat id (ex: 1A): ");
            seatId = sc.next();
            isBooked = plane.isSeatBooked(seatId);
            if (isBooked) {
                System.out.println("Seat is already booked, please try again");
            } else {
                System.out.println("\nSeat is available. Proceeding to booking..");
            }
        }
        return seatId;
    }

}