package se.nackademin;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.List;

public class CourseTest {

    Course course;
    Student student1;
    Student student2;

    @Before
    public void setUp() {
        course = new Course("Math101");
        student1 = new Student("Fredrik", "Magnusson");
        student2 = new Student("Alexandru", "Roman");
    }

    @Test
    public void testGetName() {
        assertEquals("Math101", course.getName());
    }

    @Test
    public void testAddStudent() {
        course.addStudent(student1);
        course.addStudent(student2);
        List<Student> expected = new ArrayList<Student>();
        expected.add(student1);
        expected.add(student2);
        assertEquals(expected, course.getStudents());
    }
}
