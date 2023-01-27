package my.project;

import java.io.File;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.Random;

/**
 * 
 * The Utilities class is a class that contains methods that can be used for
 * different purposes.
 * Methods include:
 * <ul>
 * <li>simulate(Plane plane, seatPlan seatPlan) : generates random
 * bookings and saves them to a file</li>
 * <li>generateNameForSim() : generates a random name</li>
 * <li>generateBirthdateForSim() : generates a random birthdate</li>
 * <li>generatePersonForSim() : generates a random Person object</li>
 * </ul>
 */
@SuppressWarnings("PMD")
public class Utilities {
    private static BookingSaverLoader bookingSaverLoader;
    private static Random random = new Random();

    public static final String PASSENGER_INFO_FILE_PATH = System.getProperty("os.name").toLowerCase().contains("win")
            ? "bookings\\passenger_info.txt"
            : "bookings/passenger_info.txt";
    public static final String BOOKINGS_FILE_PATH = System.getProperty("os.name").toLowerCase().contains("win")
            ? "bookings\\booking.data"
            : "bookings/booking.data";

    /**
     * Generates random bookings and saves them to a file.
     * 
     * @param plane    the plane object
     * @param seatPlan the seating plan object
     * @return the number of booked seats
     * @throws IOException if an I/O error occurs
     */
    public static int simulate(Plane plane, SeatPlan seatPlan) throws IOException {
        System.out.println("\nGenerating random bookings...");
        String fileName = BOOKINGS_FILE_PATH;
        Booking seatBooking = new Booking(seatPlan);
        List<Seat> availableSeats = new ArrayList<>(seatPlan.getSeats().values());
        Collections.shuffle(availableSeats);
        int numberOfSeatsToBook = (int) (availableSeats.size() * 0.8);
        int numberOfBookedSeats = 0;
        for (int i = 0; i < numberOfSeatsToBook; i++) {
            Person person = generatePersonForSim();
            Seat seat = availableSeats.get(random.nextInt(availableSeats.size()));
            if (seatBooking.bookSeat(seat, person)) {
                numberOfBookedSeats++;
            }
        }
        bookingSaverLoader = new BookingSaverLoader(seatPlan, fileName);
        bookingSaverLoader.save();
        plane.loadBookings(fileName);
        return numberOfBookedSeats;
    }

    /**
     * Generates a random name.
     * 
     * @return an array containing the first and last name
     */
    public static String[] generateNameForSim() {
        String[] firstNames = {
                "Emma", "Alexander", "Olivia", "William", "Elin", "Lucas", "Linn", "Oscar", "Sofia", "Adam", "Saga",
                "Erik", "Ebba", "Max", "Tova", "Samuel", "Ella", "David", "Alva", "Viktor", "Astrid", "Johan", "Elina",
                "Filip", "Signe", "Edvard", "Maja", "Isak", "Lina", "Leif", "Wilma", "Hans", "Livia", "Frida", "Anton",
                "Fanny", "Daniel", "Ida" };
        String[] lastNames = { "Andersson", "Johansson", "Karlsson", "Nilsson", "Eriksson", "Larsson", "Olsson",
                "Persson", "Svensson", "Gustavsson", "Pettersson", "Jonsson", "Jansson", "Hansson", "Lindberg",
                "Lindqvist", "Lundberg", "Lundqvist", "Bergström", "Nyberg", "Nilsson", "Fransson", "Berg", "Sandberg",
                "Sjöberg", "Danielsson", "Henriksson", "Lindström", "Axelsson", "Löfberg", "Söderberg", "Lövberg",
                "Samuelsson", "Nilsson", "Holmberg", "Berglund", "Björklund", "Mattsson", "Jonsson", "Lindgren", };

        int firstNameIndex = random.nextInt(firstNames.length);
        int lastNameIndex = random.nextInt(lastNames.length);

        return new String[] { firstNames[firstNameIndex], lastNames[lastNameIndex] };
    }

    /**
     * Generates a random birthdate.
     * 
     * @return a LocalDate object representing the birthdate
     */
    public static LocalDate generateBirthdateForSim() {
        int year = random.nextInt(90) + 1925;
        int month = random.nextInt(12) + 1;
        int day = random.nextInt(28) + 1;

        return LocalDate.of(year, month, day);
    }

    /**
     * Generates a random Person object.
     * 
     * @return a Person object with random name and birthdate
     */
    public static Person generatePersonForSim() {
        String[] name = generateNameForSim();
        LocalDate birthdate = generateBirthdateForSim();
        return new Person(name[0], name[1], birthdate);
    }

    public static void promptEnterKey() {
        System.out.println("Press enter to continue...");
        try {
            System.in.read();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Clearing the screen
    public static void clearScreen() {
        System.out.print("\033[H\033[2J");
        System.out.flush();
    }

    public static void deletePassengerInfoFile() {
        File passengerInfoFile = new File(PASSENGER_INFO_FILE_PATH);
        if (passengerInfoFile.exists()) {
            passengerInfoFile.delete();
        }
    }

    public static void printMenu() {
        System.out.println(MAIN_MENU);
    }

    public static final String MAIN_MENU = """
            *******************************************************************************
            *                 Welcome to the Airplane Seat Booking System                 *
            *******************************************************************************
            *                      1. Display seat plan                                   *
            *                      2. Book a seat                                         *
            *                      3. Cancel a booking                                    *
            *                      4. Display passenger list                              *
            *                      5. Run simulation                                      *
            *                      6. Save bookings to file                               *
            *                      7. Load bookings from file                             *
            *                      8. Delete bookings file                                *
            *                      9. Exit                                                *
            *******************************************************************************

            """;

}
