
package my.project;

import java.time.LocalDate;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.when;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

@SuppressWarnings("PMD")
@ExtendWith(MockitoExtension.class)
class SeatTest {
    private Seat seat = new Seat("1", 'A');
    private Person passenger = new Person("Fredrik", "Magnusson", LocalDate.of(1992, 03, 10));

    @Test
    void testGetPassenger() {
        assertNull(seat.getPassenger());
        seat.setPassenger(passenger);
        assertEquals(passenger, seat.getPassenger());
    }

    @Test
    void testBookSeat() {
        assertFalse(seat.getIsBooked());
        assertTrue(seat.bookSeat(passenger));
        assertTrue(seat.getIsBooked());
    }

    @Test
    void testGetSeat() {
        assertEquals("1A", seat.getSeat());
    }

    @Test
    void testCancelBookingTrue() {
        seat.setIsBooked(true);
        assertTrue(seat.getIsBooked());
        assertTrue(seat.cancelBooking());
        assertFalse(seat.getIsBooked());
    }

    @Test
    void testCancelBookingFalse() {
        seat.cancelBooking();
        seat.setIsBooked(false);
        assertFalse(seat.getIsBooked());
        assertFalse(seat.cancelBooking());
        assertFalse(seat.getIsBooked());
    }

    @Mock
    private Scanner mockScanner;

    @Mock
    private Plane mockPlane;

    @Test
    public void testGetSeatIdFromUser() throws InvalidSeatException {
        Scanner mockScanner = mock(Scanner.class);
        when(mockScanner.next()).thenReturn("1A", "1B");
        Plane mockPlane = mock(Plane.class);
        when(mockPlane.isSeatBooked("1A")).thenReturn(true);
        when(mockPlane.isSeatBooked("1B")).thenReturn(false);
        String seatId = Seat.getSeatIdFromUser(mockPlane, mockScanner);
        assertEquals("1B", seatId);
    }

}
