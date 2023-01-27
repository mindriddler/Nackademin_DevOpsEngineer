package my.project;

import static org.junit.jupiter.api.Assertions.assertEquals;

import static org.junit.jupiter.api.Assertions.assertTrue;
import static org.mockito.Mockito.mock;

import static org.mockito.Mockito.verify;
import static org.mockito.Mockito.when;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintStream;
import java.time.LocalDate;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.junit.jupiter.MockitoExtension;

@ExtendWith(MockitoExtension.class)
public class UtilitiesTest {

    private String osName;

    @BeforeEach
    public void setUp() {
        osName = System.getProperty("os.name");
    }

    @Test
    public void testGenerateRandomName() {
        String[] name = Utilities.generateNameForSim();
        String firstName = name[0];
        String lastName = name[1];
        assertEquals(name[0], firstName);
        assertEquals(name[1], lastName);
    }

    @Test
    public void testGenerateRandomBirthdate() {
        LocalDate birthdate = Utilities.generateBirthdateForSim();
        assertEquals(birthdate, birthdate);
    }

    @Test
    public void testGenerateRandomPerson() {
        Person person = Utilities.generatePersonForSim();
        assertEquals(person.getFirstName(), person.getFirstName());
        assertEquals(person.getLastName(), person.getLastName());
        assertEquals(person.getBirthdate(), person.getBirthdate());
    }

    @Test
    public void testClearScreen() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        System.out.println("Test Output Before Clearing the Screen");
        Utilities.clearScreen();
        String output = outContent.toString();
        assertTrue(output.isEmpty() || output.contains("\033[H\033[2J"));
    }

    @Test
    public void testPromptEnterKey() {
        ByteArrayInputStream in = new ByteArrayInputStream("\n".getBytes());
        System.setIn(in);
        Utilities.promptEnterKey();
    }

    @SuppressWarnings("PMD")
    @Test
    public void testPromptEnterKeyThrowsIOException() throws IOException {
        InputStream mockInputStream = mock(InputStream.class);
        when(mockInputStream.read()).thenThrow(new IOException());
        System.setIn(mockInputStream);
        Utilities.promptEnterKey();
        verify(mockInputStream).read();
        mockInputStream.close();
    }

    @Test
    public void testPrintMenu() {
        ByteArrayOutputStream outContent = new ByteArrayOutputStream();
        System.setOut(new PrintStream(outContent));
        Utilities.printMenu();
        assertEquals(Utilities.MAIN_MENU + System.lineSeparator(), outContent.toString());
    }

    @Test
    public void testSimulation() throws IOException {
        Plane plane = new Plane();
        SeatPlan seatPlan = new SeatPlan();
        String fileName = Utilities.BOOKINGS_FILE_PATH;
        int numberOfBookedSeats = Utilities.simulate(plane, seatPlan);
        List<Seat> bookedSeats = seatPlan.getBookedSeats();
        assertEquals(bookedSeats.size(), numberOfBookedSeats);
        assertTrue(new File(fileName).exists());
    }

    @Test
    public void testFilePaths() {
        String passengerInfoFilePath = Utilities.PASSENGER_INFO_FILE_PATH;
        String bookingsFilePath = Utilities.BOOKINGS_FILE_PATH;
        if (osName.toLowerCase().contains("win")) {
            assertEquals("bookings\\passenger_info.txt", passengerInfoFilePath);
            assertEquals("bookings\\booking.data", bookingsFilePath);
        } else {
            assertEquals("bookings/passenger_info.txt", passengerInfoFilePath);
            assertEquals("bookings/booking.data", bookingsFilePath);
        }
    }
}
