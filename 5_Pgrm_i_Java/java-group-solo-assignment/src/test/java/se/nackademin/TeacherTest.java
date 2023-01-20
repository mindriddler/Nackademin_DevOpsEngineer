package se.nackademin;

import org.junit.Test;
import static org.junit.Assert.*;
import java.util.List;
import java.util.ArrayList;

public class TeacherTest {

    Teacher teacher;
    Course math;
    Course science;

    @Test
    public void testTeacherFirstName() {
        Person person = new Teacher("Fredrik", "Magnusson");
        String FirstName = person.getFirstName();
        assertEquals("Fredrik", FirstName);
    }

    @Test
    public void testTeacherLastName() {
        Person person = new Teacher("Fredrik", "Magnusson");
        String LastName = person.getLastName();
        assertEquals("Magnusson", LastName);
    }

    @Test
    public void testTeacherAge() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setAge(30);
        int PersonAge = person.getAge();
        assertEquals(30, PersonAge);
    }

    @Test
    public void testAddCourse() {
        Teacher teacher = new Teacher("Fredrik", "Magnusson");
        teacher.addCourse(math);
        teacher.addCourse(science);
        List<Course> expected = new ArrayList<Course>();
        expected.add(math);
        expected.add(science);
        assertEquals(expected, teacher.getCourses());
    }

    @Test
    public void testTeacherAgeNegative() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setAge(-30);
        int PersonAge = person.getAge();
        assertEquals(0, PersonAge);
    }

    @Test
    public void testTeacherAgeZero() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setAge(0);
        int PersonAge = person.getAge();
        assertEquals(0, PersonAge);
    }

    @Test(expected = IllegalArgumentException.class)
    public void testTeacherInvalidGender() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setGender("Other");
        String PersonGender = person.getGender();
        assertEquals("", PersonGender);
    }

    @Test
    public void testTeacherGenderFemale() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setGender("Female");
        String PersonGender = person.getGender();
        assertEquals("Female", PersonGender);
    }

    @Test
    public void testTeacherGenderMale() {
        Person person = new Teacher("Fredrik", "Magnusson");
        person.setGender("Male");
        String PersonGender = person.getGender();
        assertEquals("Male", PersonGender);
    }
}
