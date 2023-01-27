# Table of content 
- [Table of content](#table-of-content)
- [Flyget](#flyget)
- [Notes](#notes)
- [Project requirements](#project-requirements)
  - [1. Requirements](#1-requirements)
    - [1.1. Functional requirements](#11-functional-requirements)
    - [1.2. Non-functional requirements](#12-non-functional-requirements)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
      - [JDK 17 or later](#jdk-17-or-later)
      - [Maven](#maven)
  - [Installing](#installing)
- [Usage](#usage)
  - [Running the tests](#running-the-tests)
  - [Built With](#built-with)
  - [Authors](#authors)
    - [Fredrik Magnusson \[fredrik.magnusson2@yh.nackademin.se\]](#fredrik-magnusson-fredrikmagnusson2yhnackademinse)

# Flyget
This project is seat reservation system. It includes the following features:

* Displaying the seating plan of the plane
* Booking a seat
* Cancelling a booking
* Displaying a list of passengers
* Saving and loading bookings
* Deleting the bookings file
* A method that generates already booked seats for a more accurate real life situation

# Notes
* The program uses ANSI escape codes to print the seating plan in color.
* The program uses the Scanner class to read input from the user, so make sure to enter the input in the correct format as prompted by the program.
* The program uses the LocalDate class to handle dates, so make sure to enter the birthdate in the format yyyy-MM-dd.

# Project requirements
## 1. Requirements
### 1.1. Functional requirements
* The program shall be able to display the seating plan of the plane with the following information:
  * Whether the seat is booked or not
* The program shall only let the user book a seat if the seat is not already booked by:
  * Specifying the seat number
  * Specifying the passenger's name
  * Specifying the passenger's birthdate
* The program shall be able to save the current bookings to a file.
* The program shall be able to load bookings from a file.
* The program shall be able to show a list of passengers on a flight with the following information:
  * The passenger's name
  * The passenger's birthdate
  * The passenger's seat number
* The program shall be able to be loaded with a number of already booked seats to simulate a real flight.
* The program shall have a user-friendly interface.
* The program shall be able to book multiple seats at once.

### 1.2. Non-functional requirements
* The project shall be written in Java.
* The project shall be written in an object-oriented way.
* The project shall be written in english.
* The project require the usage of Git and GitHub.
* The project shall be setup using Maven.
* The project shall use multiple classes.
  * and the classes shall be structured in a logical way.
* The project shall have documented classes and methods.
* The project shall have usage of Java's standard API
* The project shall have unit tests.
* The project shall have correct usage of polymorphism and encapsulation with the help of:
  * Inheritance
  * Abstract classes
  * Interfaces
  * Getters and setters
  * Access modifiers
* The projecet shall have a class diagram and/or other design documentation.


# Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
You will need to have the following software installed on your machine:

#### JDK 17 or later
* [Download here](https://www.oracle.com/java/technologies/downloads/#java17)
#### Maven
* [Download here](https://maven.apache.org/download.cgi)
* * [Find install instructions here](https://maven.apache.org/install.html)
## Installing
1. Clone the repository to your local machine
```bash
git clone https://github.com/mindriddler/flyget_FredrikMagnusson.git
```
2. Navigate to the project directory
```bash
cd flyget_FredrikMagnusson
```
3. Compile and package the project using Maven
```bash
mvn clean package
```
4. Run the project
```bash
mvn exec:java
```
# Usage
When you run the program, you will be presented with a menu of options:

* View seats: Allows you to view the seating plan of the plane.
* Book seat: Allows you to book a seat on the plane.
* Cancel booking: Allows you to cancel a booking.
* View passenger list: Allows you to view the list of passengers on a flight.
* Save bookings: Allows you to save the current bookings to a file.
* Load bookings: Allows you to load bookings from a file.
* Delete bookings file: Allows you to delete the bookings file.
* Exit program: Exits the program and deletes the bookings file.
## Running the tests
To run the tests, use the following command:
```bash
mvn test
```
You can find a coverage report in the target/site/jacoco/index.html file.

## Built With
* Maven - Dependency Management
* JUnit - Testing Framework

## Authors
### Fredrik Magnusson [fredrik.magnusson2@yh.nackademin.se]
