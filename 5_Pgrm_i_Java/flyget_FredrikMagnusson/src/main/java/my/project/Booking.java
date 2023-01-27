package my.project;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.List;
import java.util.Scanner;

/*
This class is used to book seats and cancel bookings.
*/

@SuppressWarnings("PMD")
public class Booking {
    private SeatPlan seatPlan;

    /**
     * Creates a new booking object with the specified seating plan.
     * 
     * @param seatPlan
     *                 the seating plan to use for this booking
     */
    public Booking(SeatPlan seatPlan) {
        this.seatPlan = seatPlan;
    }

    /**
     * Books the specified seat for the specified passenger.
     * 
     * @param seat
     *                  the seat to book
     * @param passenger
     *                  the passenger who is booking the seat
     * @return true if the seat was successfully booked, false otherwise
     */
    public boolean bookSeat(Seat seat, Person passenger) {
        if (seat != null && !seat.getIsBooked()) {
            seat.setIsBooked(true);
            seat.setPassenger(passenger);
            return true;
        }
        return false;
    }

    /**
     * Cancels the booking for the seat with the specified seat ID.
     * 
     * @param seatId
     *               the ID of the seat to cancel the booking for
     * @return true if the booking was successfully cancelled, false otherwise
     */
    public boolean cancelBooking(String seatId) {
        Seat seat = seatPlan.getSeat(seatId);
        if (seat != null) {
            return seat.cancelBooking();
        }
        return false;
    }

    /**
     * Allows the user to book one or more seats on the specified plane.
     * 
     * @param plane
     *              the plane to book seats on
     * @param sc
     *              the scanner to use to get input from the user
     */
    @lombok.Generated
    public void bookSeat(Plane plane, Scanner sc) {
        int numberOfSeats = 0;
        List<String> bookedSeats = new ArrayList<>();
        try {
            System.out.print("How many seats do you want to book? ");
            numberOfSeats = sc.nextInt();
            if (numberOfSeats < 1 || numberOfSeats > 180) {
                throw new InputMismatchException();
            }
            String fileName = Utilities.PASSENGER_INFO_FILE_PATH;
            FileWriter writer = new FileWriter(fileName);
            for (int i = 0; i < numberOfSeats; i++) {
                String seatId = Seat.getSeatIdFromUser(plane, sc);
                Seat seat = seatPlan.getSeat(seatId);
                Person person = Person.getPersonDetails(sc);
                plane.bookSeat(seat, person);
                bookedSeats.add(seatId);
                System.out.println("Seat: " + seatId + " booked successfully");
                writer.write(seatId + ", " + person.getFullName() + ", "
                        + person.getBirthdate() + "\n");
            }
            writer.close();
            System.out
                    .println("\nAll seats and passenger information have been successfully saved to " + fileName + "!");
        } catch (InvalidSeatException e) {
            if (numberOfSeats == 1) {
                System.out.println("Error: " + e.getMessage());
                System.out.println("Please try again!");
                System.out.println("Returning to main menu.\n");
            } else {
                System.out.println("Error: " + e.getMessage());
                cancelBookingsForMultipleBookings(plane, bookedSeats);
                System.out.println(
                        "All of your bookings have been canceled. Please try again with a valid seat id for each seat you want to book.");
                System.out.println("Returning to main menu.\n");
            }
        } catch (InputMismatchException e) {
            System.out.println("Error: Invalid input!");
            System.out.println("Please try again!");
            System.out.println("Returning to main menu.\n");
        } catch (IOException e) {
            System.out.println("Error: Unable to save passenger information to file!");
            System.out.println("All bookings have been canceled.");
            cancelBookingsForMultipleBookings(plane, bookedSeats);
            System.out.println("Please try again!");
            System.out.println("Returning to main menu.\n");
        }
    }

    /**
     * Cancels all bookings for the specified seats.
     * 
     * @param plane
     *                    the plane to cancel bookings on
     * @param bookedSeats
     *                    the list of booked seats to cancel
     */
    public void cancelBookingsForMultipleBookings(Plane plane, List<String> bookedSeats) {
        for (String seatId : bookedSeats) {
            plane.cancelBooking(seatId);
        }
    }

    /**
     * Allows the user to cancel one or more bookings on the specified plane.
     * 
     * @param plane
     *              the plane to cancel bookings on
     */
    @lombok.Generated
    public void cancelBooking(Plane plane, Scanner sc) {
        System.out.print("\nEnter seat id (ex 1A): ");
        String seatId = sc.next();
        if (plane.cancelBooking(seatId)) {
            System.out.println("Booking canceled successfully!");
        } else {
            System.out.println("Error: Invalid seat id or seat not booked");
            System.out.println("Please try again!");
            System.out.println("Returning to main menu.\n");
        }
    }

    double getNumberOfBookedSeats() {
        List<Seat> seats = new ArrayList<>(seatPlan.getSeats().values());
        int bookedSeats = 0;
        for (Seat seat : seats) {
            if (seat.getIsBooked()) {
                bookedSeats++;
            }
        }
        return bookedSeats;
    }
}
