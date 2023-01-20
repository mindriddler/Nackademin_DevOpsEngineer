package se.nackademin;

class Main {
    public static void main(String[] args) {
        Student student = new Student("Fredrik", "Magnusson");
        student.setAge(30);
        student.setGender("Male");
        student.setStudentId("12345");

        Course course = new Course("Programmering i Java");
        course.addStudent(student);

        Teacher professor = new Teacher("Martin", "Fröjd");
        professor.setAge(40);
        professor.setGender("Male");
        professor.addCourse(course);
    }
}
