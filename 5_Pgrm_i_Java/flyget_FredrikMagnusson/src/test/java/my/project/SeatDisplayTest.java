package my.project;

import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.BeforeEach;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

@SuppressWarnings({ "PMD", "unused" })
public class SeatDisplayTest {
    private SeatPlan seatPlan;
    private SeatDisplay seatDisplay;

    @BeforeEach
    public void setup() {
        seatPlan = new SeatPlan();
        seatDisplay = new SeatDisplay(seatPlan);
    }

    @Test
    public void testDisplay() {
        for (Seat seat : seatPlan.getSeats().values()) {
            seat.setIsBooked(false);
        }
        seatDisplay.display();
        String output = getOutput();
        for (Seat seat : seatPlan.getSeats().values()) {
            assertEquals(output.contains("\033[32mO\033[0m"), true);
        }

        for (Seat seat : seatPlan.getSeats().values()) {
            seat.setIsBooked(true);
        }
        seatDisplay.display();
        output = getOutput();
        for (Seat seat : seatPlan.getSeats().values()) {
            assertEquals(output.contains("\033[31mX\033[0m"), true);
        }
    }

    private String getOutput() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        seatDisplay.display();
        return outContent.toString();
    }

}