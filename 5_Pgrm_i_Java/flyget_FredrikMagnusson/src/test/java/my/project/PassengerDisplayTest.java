package my.project;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;
import java.time.LocalDate;
import java.util.HashMap;
import java.util.Map;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.mockito.Mockito.mock;
import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

public class PassengerDisplayTest {
    private SeatPlan seatPlan = new SeatPlan();
    private Seat seat = new Seat("1", 'A');
    private PassengerDisplay passengerDisplay = new PassengerDisplay(seatPlan);

    @Test
    public void testDisplayPassengerList() {
        Person passenger = new Person("Fredrik", "Magnusson", LocalDate.of(1992, 03, 10));
        seat.setPassenger(passenger);
        seat.setIsBooked(true);
        seatPlan.getSeats().put("1A", seat);
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        passengerDisplay.displayPassengerInformation();
        assertEquals("Seat: 1A, Name: Fredrik Magnusson, Birthdate: 1992-03-10" + System.lineSeparator(),
                outContent.toString());

    }

    @Test
    void testGetPassengerList() {
        Plane plane = mock(Plane.class);
        Map<String, Seat> seats = new HashMap<>();
        Seat seat1 = mock(Seat.class);
        when(seat1.getIsBooked()).thenReturn(true);
        seats.put("1A", seat1);
        Seat seat2 = mock(Seat.class);
        when(seat2.getIsBooked()).thenReturn(false);
        seats.put("1B", seat2);
        when(plane.getSeats()).thenReturn(seats);
        PassengerDisplay passengerDisplay = new PassengerDisplay(null);
        passengerDisplay.getPassengerList(plane);
        verify(plane).displayPassengerList();
    }

}
