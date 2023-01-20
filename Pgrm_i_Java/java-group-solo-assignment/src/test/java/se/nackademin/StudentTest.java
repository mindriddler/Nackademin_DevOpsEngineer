package se.nackademin;

import org.junit.Test;
import static org.junit.Assert.*;

public class StudentTest {

    @Test
    public void testStudentFirstName() {
        Person person = new Student("Fredrik", "Magnusson");
        String FirstName = person.getFirstName();
        assertEquals("Fredrik", FirstName);
    }

    @Test
    public void testStudentLastName() {
        Person person = new Student("Fredrik", "Magnusson");
        String LastName = person.getLastName();
        assertEquals("Magnusson", LastName);
    }

    @Test
    public void testStudentAge() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setAge(30);
        int PersonAge = person.getAge();
        assertEquals(30, PersonAge);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testInvalidStudentId() {
        Student student = new Student("Fredrik", "Magnusson");
        student.setStudentId("123");
    }

    @Test
    public void testValidStudentId() {
        Student student = new Student("Fredrik", "Magnusson");
        student.setStudentId("12345");
        assertEquals("12345", student.getStudentId());
    }

    @Test
    public void testStudentAgeNegative() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setAge(-30);
        int PersonAge = person.getAge();
        assertEquals(0, PersonAge);
    }

    @Test
    public void testStudentAgeZero() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setAge(0);
        int PersonAge = person.getAge();
        assertEquals(0, PersonAge);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testStudentInvalidGender() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setGender("Other");
        String PersonGender = person.getGender();
        assertEquals("", PersonGender);
    }

    @Test
    public void testStudentGenderFemale() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setGender("Female");
        String PersonGender = person.getGender();
        assertEquals("Female", PersonGender);
    }

    @Test
    public void testStudentGenderMale() {
        Person person = new Student("Fredrik", "Magnusson");
        person.setGender("Male");
        String PersonGender = person.getGender();
        assertEquals("Male", PersonGender);
    }
}