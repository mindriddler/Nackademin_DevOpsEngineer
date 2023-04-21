package my.project;

import java.util.Map;

/**
 * 
 * The seatDisplay class is used to display the seating plan of a plane.
 * 
 * It takes in a seatPlan object and uses it to retrieve the seats and
 * display their status (booked or available)
 * 
 * in a formatted manner. The seats are displayed with booked seats marked as
 * "X" and available seats as "O".
 */
public class SeatDisplay {
    private static final int NUM_ROWS = 30;
    private static final int NUM_COLS = 6;
    private static final String AVAILABLE_SEAT = "\033[32mO\033[0m";
    private static final String BOOKED_SEAT = "\033[31mX\033[0m";

    private SeatPlan seatPlan;

    /**
     * 
     * Constructor for seatDisplay class, which takes in a seatPlan object
     * 
     * @param seatPlan the seatPlan object containing information about the
     *                 seats
     */

    public SeatDisplay(SeatPlan seatPlan) {
        this.seatPlan = seatPlan;
    }

    /**
     * 
     * Constructor for seatDisplay class, which takes in a seatPlan object
     * 
     * @param seatPlan the seatPlan object containing information about the
     *                 seats
     */

    public void display() {
        System.out.println("\n \033[31mX\033[0m = Booked\n \033[32mO\033[0m = Available\n");
        Map<String, Seat> seats = seatPlan.getSeats();
        // Print column letters at the top
        System.out.print("  ");
        for (int i = 0; i < NUM_COLS; i++) {
            System.out.print("  " + (char) ('A' + i) + " ");
        }
        System.out.println();
        // Print separator line
        System.out.print("  ");
        for (int i = 0; i < NUM_COLS; i++) {
            System.out.print("____");
        }
        System.out.println();
        for (int i = 0; i < NUM_ROWS; i++) {
            // Print row number
            System.out.print(String.format("%2d", i + 1) + "| ");
            for (int j = 0; j < NUM_COLS; j++) {
                Seat seat = seats.get((i + 1) + "" + (char) ('A' + j));
                System.out.print(seat.getIsBooked() ? BOOKED_SEAT : AVAILABLE_SEAT);
                System.out.print(" | ");
            }
            System.out.println();
        }
    }
}
