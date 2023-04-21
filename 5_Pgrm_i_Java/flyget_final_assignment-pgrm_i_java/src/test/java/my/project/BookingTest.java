
package my.project;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@SuppressWarnings({ "PMD", "unused" })
@ExtendWith(MockitoExtension.class)
public class BookingTest {

    @Mock
    private Scanner sc;

    @Mock
    private Plane plane;
    private SeatPlan seatPlan;
    private Booking booking;
    private BookingSaverLoader bookingSaverLoader;
    private Map<String, Seat> seats;

    @BeforeEach
    public void setup() {
        Utilities.deletePassengerInfoFile();
        BookingSaverLoader.deleteBookingsFile();
        plane = new Plane();
        seats = new HashMap<>();
        seatPlan = new SeatPlan();
        booking = new Booking(seatPlan);
        bookingSaverLoader = new BookingSaverLoader(seatPlan, Utilities.BOOKINGS_FILE_PATH);
    }

    @Test
    public void testIsSeatBooked() throws InvalidSeatException {
        SeatPlan mockseatPlan = mock(SeatPlan.class);
        Seat mockSeat = mock(Seat.class);
        when(mockseatPlan.getSeat("1A")).thenReturn(mockSeat);
        when(mockSeat.getIsBooked()).thenReturn(true);
        Plane plane = new Plane();
        plane.seatPlan = mockseatPlan;
        boolean isBooked = plane.isSeatBooked("1A");
        assertTrue(isBooked);
    }

    @Test
    public void testBookSeatInvalidSeat() throws InvalidSeatException {
        when(sc.nextInt()).thenReturn(1);
        when(sc.next()).thenReturn("1Z");
        booking.bookSeat(plane, sc);
        Utilities.deletePassengerInfoFile();
        assertEquals(0, booking.getNumberOfBookedSeats());
        
    }

    @Test
    void testGetFileName() {
        BookingSaverLoader bookingSaverLoader = new BookingSaverLoader(seatPlan, "test.txt");
        bookingSaverLoader.setFileName("test.txt");
        assertEquals("test.txt", bookingSaverLoader.getFileName());
    }

    @Test
    public void testCancelBookingsForMultipleBookings() {
        Plane plane = new Plane();
        List<String> bookedSeats = new ArrayList<>();
        bookedSeats.add("1A");
        bookedSeats.add("1B");
        bookedSeats.add("2A");
        for (String seatId : bookedSeats) {
            plane.bookSeat(plane.getSeats().get(seatId),
                    new Person("Fredrik", "Magnusson", LocalDate.of(1992, 03, 10)));
        }
        for (String seatId : bookedSeats) {
            assertTrue(plane.getSeats().get(seatId).getIsBooked());
        }
        booking.cancelBookingsForMultipleBookings(plane, bookedSeats);
        for (String seatId : bookedSeats) {
            assertFalse(plane.getSeats().get(seatId).getIsBooked());
        }
    }

    @Test
    public void testCancelBooking_notFound() {
        String seatId = "A1";
        boolean result = booking.cancelBooking(seatId);
        assertFalse(result);
    }

}