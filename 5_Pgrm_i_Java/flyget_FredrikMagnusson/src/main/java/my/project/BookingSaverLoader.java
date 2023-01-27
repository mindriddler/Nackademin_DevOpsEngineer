package my.project;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.Map;

/**
 * 
 * This class is used to save and load bookings from a file.
 */
@SuppressWarnings("PMD")
public class BookingSaverLoader {
    private SeatPlan seatPlan;
    private String fileName;

    /**
     * 
     * Constructor that takes in seatPlan and fileName
     * 
     * @param seatPlan seating plan for the flight
     * @param fileName the name of the file to save and load the bookings
     */
    public BookingSaverLoader(SeatPlan seatPlan, String fileName) {
        this.seatPlan = seatPlan;
        this.fileName = fileName;
    }

    public String getFileName() {
        return fileName;
    }

    public void setFileName(String string) {
        this.fileName = string;
    }

    public void save() {
        try {
            FileOutputStream fileOut = new FileOutputStream(fileName);
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(seatPlan.getSeats());
            out.close();
            fileOut.close();
            System.out.println("Bookings saved in " + fileName);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    @SuppressWarnings("unchecked")
    public void load(String fileName) {
        try {
            FileInputStream fileIn = new FileInputStream(fileName);
            ObjectInputStream in = new ObjectInputStream(fileIn);
            seatPlan.setSeats((Map<String, Seat>) in.readObject());
            in.close();
            fileIn.close();
            System.out.println("Bookings loaded from " + fileName);
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
        }
    }

    public static void deleteBookingsFile() {
        File bookingsFile = new File(Utilities.BOOKINGS_FILE_PATH);
        if (bookingsFile.exists()) {
            bookingsFile.delete();
            System.out.println("Bookings file deleted successfully.");
        } else {
            System.out.println("");
        }
    }

}
