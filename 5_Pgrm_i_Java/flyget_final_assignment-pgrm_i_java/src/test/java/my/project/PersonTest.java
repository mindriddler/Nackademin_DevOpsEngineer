package my.project;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.LocalDate;
import java.util.Scanner;

import org.junit.jupiter.api.Test;
import org.mockito.Mock;

public class PersonTest {
    @Mock
    private Scanner scanner;

    @Test
    public void testGetPersonDetails() {
        Scanner sc = new Scanner("Fredrik\nMagnusson\n1992-03-10\n");
        Person person = Person.getPersonDetails(sc);
        assertEquals("Fredrik", person.getFirstName());
        assertEquals("Magnusson", person.getLastName());
        assertEquals(LocalDate.of(1992, 03, 10), person.getBirthdate());
    }

    @Test
    public void getFullName() {
        Person person = new Person("Fredrik", "Magnusson", LocalDate.of(1992, 03, 10));
        assertEquals("Fredrik Magnusson", person.getFullName());
    }
}
