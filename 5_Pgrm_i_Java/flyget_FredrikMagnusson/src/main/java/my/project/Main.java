package my.project;

import java.io.IOException;
import java.util.Scanner;

/**
 * 
 * Main class that handles the user interface and controls the flow of the
 * program.
 * User can select from different options such as viewing seating plan, booking
 * a seat,
 * cancelling a booking, viewing passenger list, saving bookings, loading
 * bookings, deleting bookings file, and exiting the program.
 * Program also includes a simulation feature to load the plane with already
 * randomized booked seats.
 */
@lombok.Generated
@SuppressWarnings("PMD")
public class Main extends Utilities {
    private static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        deletePassengerInfoFile();
        Plane plane = new Plane();
        SeatPlan seatPlan = new SeatPlan();
        Booking booking = new Booking(plane.getseatPlan());
        PassengerDisplay passengerDisplay = new PassengerDisplay(plane.getseatPlan());
        boolean exit = false;
        while (!exit) {
            clearScreen();
            printMenu();
            System.out.print("Enter your choice: ");
            String choice = sc.next();
            switch (choice) {
                case "1":
                    clearScreen();
                    plane.displaySeats();
                    promptEnterKey();
                    break;
                case "2":
                    clearScreen();
                    plane.displaySeats();
                    System.out.println("\n");
                    booking.bookSeat(plane, sc);
                    promptEnterKey();
                    break;
                case "3":
                    booking.cancelBooking(plane, sc);
                    promptEnterKey();
                    break;
                case "4":
                    passengerDisplay.getPassengerList(plane);
                    promptEnterKey();
                    break;
                case "5":
                    System.out.println("\n\u001B[31m!!!This will delete all current bookings!!!\u001B[0m");
                    System.out.print("Do you want to run the simulation (Y/N)?: ");
                    String answer = sc.next();
                    if (answer.equalsIgnoreCase("Y")) {
                        BookingSaverLoader.deleteBookingsFile();
                        simulate(plane, seatPlan);
                        System.out.println("Simulation complete");
                        promptEnterKey();
                        break;
                    } else {
                        System.out.println("Simulation cancelled");
                        promptEnterKey();
                        break;
                    }
                case "6":
                    plane.saveBookings();
                    promptEnterKey();
                    break;
                case "7":
                    plane.loadBookings(BOOKINGS_FILE_PATH);
                    promptEnterKey();
                    break;
                case "8":
                    BookingSaverLoader.deleteBookingsFile();
                    promptEnterKey();
                    break;
                case "9":
                    exit = true;
                    deletePassengerInfoFile();
                    System.out.print("Exiting program... Goodbye!");
                    break;
                default:
                    System.out.println("Invalid choice, please try again");
                    clearScreen();
                    continue;
            }
        }
    }
}
