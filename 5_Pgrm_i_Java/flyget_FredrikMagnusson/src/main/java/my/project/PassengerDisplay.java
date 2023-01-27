package my.project;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Map;

/**
 * 
 * The class contains methods for displaying passenger information
 * 
 */
public class PassengerDisplay {
    private SeatPlan seatPlan;

    /**
     * 
     * Constructor of the class
     * 
     * @param seatPlan A seating plan object containing seats and their
     *                 information
     */
    public PassengerDisplay(SeatPlan seatPlan) {
        this.seatPlan = seatPlan;
    }

    public void displayPassengerInformation() {
        List<Seat> seatList = new ArrayList<Seat>(seatPlan.getSeats().values());
        Collections.sort(seatList, new Comparator<Seat>() {
            @Override
            public int compare(Seat seat1, Seat seat2) {
                if (seat1.getSeat() == null || seat2.getSeat() == null) {
                    return 0;
                }
                return seat1.getSeat().compareTo(seat2.getSeat());
            }
        });
        for (Seat seat : seatList) {
            if (seat.getIsBooked()) {
                Person passenger = seat.getPassenger();
                System.out.println("Seat: " + seat.getSeat() + ", Name: " + passenger.getFirstName() + " "
                        + passenger.getLastName()
                        + ", Birthdate: " + passenger.getBirthdate());
            }
        }
    }

    /**
     * 
     * getPassengerList method
     * used to
     * get and
     * display passenger information
     * 
     * @param
     * plane        A
     *              plane object
     *              containing seats
     *              and their information
     */
    public void getPassengerList(Plane plane) {
        boolean anyBooked = false;
        for (Map.Entry<String, Seat> entry : plane.getSeats().entrySet()) {
            if (entry.getValue().getIsBooked()) {
                anyBooked = true;
                break;
            }
        }
        if (anyBooked) {
            plane.displayPassengerList();
        } else {
            System.out.println("No seats are booked.");
        }
    }
}
