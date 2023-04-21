package my.project;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;

import java.util.List;

import org.junit.jupiter.api.Test;

public class SeatPlanTest {

    @Test
    public void testGetAvailableSeats() {
        SeatPlan seatPlan = new SeatPlan();
        // Set some seats to booked
        seatPlan.getSeat("1A").setIsBooked(true);
        seatPlan.getSeat("1B").setIsBooked(false);
        seatPlan.getSeat("1C").setIsBooked(true);
        seatPlan.getSeat("2A").setIsBooked(false);
        seatPlan.getSeat("2B").setIsBooked(true);
        seatPlan.getSeat("2C").setIsBooked(false);
        List<Seat> availableSeats = seatPlan.getAvailableSeats();
        /*
         * Check that the correct number of seats are available which in this case is
         * 177 as there are 3 booked seats
         * and 180 seats in total
         */
        assertEquals(177, availableSeats.size());
        for (Seat seat : availableSeats) {
            assertFalse(seat.getIsBooked());
        }
    }
}
