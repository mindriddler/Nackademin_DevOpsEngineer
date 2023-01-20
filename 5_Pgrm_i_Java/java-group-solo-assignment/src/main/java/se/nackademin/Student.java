package se.nackademin;

class Student implements Person {
    private String firstName;
    private String lastName;
    private int age;
    private String gender;
    private String studentId;

    public Student(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
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

    public void setStudentId(String studentId) {
        if (studentId.length() != 5) {
            throw new IllegalArgumentException("Invalid student ID. Student ID must be a 5-digit number.");
        }
        this.studentId = studentId;
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

    public String getStudentId() {
        return studentId;
    }
}
