package my.project;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNotNull;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

@SuppressWarnings("PMD")
public class PlaneTest extends Utilities {

    private Plane plane;
    private Person person;
    private Seat seat;
    private String seatId;
    private PassengerDisplay passengerDisplay;

    @BeforeEach
    public void setUp() {
        plane = new Plane();
        person = new Person("Fredrik", "Magnusson", LocalDate.of(1992, 03, 10));
        seatId = "1A";
        seat = plane.getSeats().get(seatId);
    }

    @Test
    public void testGetseatPlan() {
        assertNotNull(plane.getseatPlan());
    }

    @Test
    public void testGetSeats() {
        Map<String, Seat> seats = plane.getSeats();
        assertNotNull(seats);
        assertTrue(seats.size() > 0);
    }

    @Test
    public void testBookSeat() {
        assertFalse(seat.getIsBooked());
        assertTrue(plane.bookSeat(seat, person));
        assertTrue(seat.getIsBooked());
    }

    @Test
    public void testCancelBooking() {
        assertFalse(seat.getIsBooked());
        assertTrue(plane.bookSeat(seat, person));
        assertTrue(seat.getIsBooked());
        assertTrue(plane.cancelBooking(seatId));
        assertFalse(seat.getIsBooked());
    }

    @Test
    public void testIsSeatBooked() throws InvalidSeatException {
        assertFalse(plane.isSeatBooked(seatId));
        assertTrue(plane.bookSeat(seat, person));
        assertTrue(plane.isSeatBooked(seatId));
    }

    @Test
    public void testIsSeatBookedInvalidSeat() {
        assertThrows(InvalidSeatException.class, () -> {
            plane.isSeatBooked("invalid seat id");
        });
    }

    /*
     * @Test
     * public void testSaveAndLoadBookings() throws InvalidSeatException {
     * plane.bookSeat(seat, person);
     * assertTrue(plane.isSeatBooked(seatId));
     * plane.saveBookings();
     * plane.cancelBooking(seatId);
     * assertFalse(plane.isSeatBooked(seatId));
     * plane.loadBookings(BOOKINGS_FILE_PATH);
     * assertTrue(plane.isSeatBooked(seatId));
     * }
     */
    @Test
    public void testDisplayPassengerList_NoSeatsBooked() {
        Plane plane = mock(Plane.class);
        SeatPlan seatPlan = new SeatPlan();
        when(plane.getSeats()).thenReturn(new HashMap<>());
        passengerDisplay = new PassengerDisplay(seatPlan);
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        passengerDisplay.getPassengerList(plane);
        assertEquals("No seats are booked.", outContent.toString().trim());
    }
}
