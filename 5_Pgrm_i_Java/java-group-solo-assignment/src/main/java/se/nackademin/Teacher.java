package se.nackademin;

import java.util.List;
import java.util.ArrayList;

class Teacher implements Person {
    private String firstName;
    private String lastName;
    private int age;
    private String gender;
    private List<Course> courses;

    public Teacher(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.courses = new ArrayList<>();
    }

    @Override
    public void setAge(int age) {
        if (age < 0) {
            age = 0;
        }
        this.age = age;
    }

    @Override
    public void setGender(String gender) {
        if (!("Male".equals(gender) || "Female".equals(gender))) {
            throw new IllegalArgumentException("Invalid gender: " + gender + ". Gender must be either Male or Female.");
        }
        this.gender = gender;
    }

    public void addCourse(Course course) {
        courses.add(course);
    }

    @Override
    public String getFirstName() {
        return firstName;
    }

    @Override
    public String getLastName() {
        return lastName;
    }

    @Override
    public int getAge() {
        return age;
    }

    @Override
    public String getGender() {
        return gender;
    }

    public List<Course> getCourses() {
        return courses;
    }
}
