package my.project;

import java.io.Serializable;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.Scanner;

/**
 * 
 * This class represents a person. It contains fields for the person's first
 * name, last name, and birthdate.
 * 
 * It provides methods for setting and getting these fields and also a method
 * for getting the full name of the person.
 * 
 * It also contains a static method for getting the person details from the
 * user.
 */
public class Person implements Serializable {
    private String firstName;
    private String lastName;
    private LocalDate birthdate;
    private static final long serialVersionUID = 1L;

    public Person(String firstName, String lastName, LocalDate birthdate) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.birthdate = birthdate;
    }

    public String getFirstName() {
        return firstName;
    }

    @lombok.Generated
    private void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    @lombok.Generated
    private void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public LocalDate getBirthdate() {
        return birthdate;
    }

    @lombok.Generated
    private void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
    }

    public String getFullName() {
        return firstName + " " + lastName;
    }

    /**
     * 
     * Get the person details from the user.
     * 
     * @param sc a scanner object to read user input
     * @return a Person object containing the details entered by the user
     */
    public static Person getPersonDetails(Scanner sc) {
        System.out.print("\nEnter first name: ");
        String firstName = sc.next();
        System.out.print("Enter last name: ");
        String lastName = sc.next();
        LocalDate correctBirthDate = null;
        while (correctBirthDate == null) {
            System.out.print("Enter birthdate (yyyy-MM-dd): ");
            String birthdate = sc.next();
            try {
                DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd");
                correctBirthDate = LocalDate.parse(birthdate, formatter);
            } catch (DateTimeParseException e) {
                System.out.println("Error: Invalid birthdate format, please try again");
            }
        }
        return new Person(firstName, lastName, correctBirthDate);
    }
}
