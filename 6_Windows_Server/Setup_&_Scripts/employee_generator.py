import csv
import datetime
import os
import random

firstnames = [
    "Alexander",
    "Alfred",
    "Andrew",
    "Arthur",
    "Benjamin",
    "Charles",
    "Christopher",
    "Daniel",
    "David",
    "Edward",
    "Elliot",
    "Ethan",
    "Frederick",
    "George",
    "Harry",
    "Henry",
    "Isaac",
    "Jack",
    "James",
    "Jasper",
    "John",
    "Joseph",
    "Joshua",
    "Leo",
    "Lewis",
    "Louis",
    "Lucas",
    "Matthew",
    "Michael",
    "Nathaniel",
    "Oliver",
    "Oscar",
    "Patrick",
    "Paul",
    "Peter",
    "Philip",
    "Richard",
    "Robert",
    "Samuel",
    "Simon",
    "Stephen",
    "Theodore",
    "Thomas",
    "Timothy",
    "Tristan",
    "William",
    "Winston",
    "Zachary",
    "Angus",
    "Graham",
    "Abigail",
    "Alexandra",
    "Alice",
    "Amelia",
    "Annabelle",
    "Annalise",
    "Arabella",
    "Beatrice",
    "Caroline",
    "Catherine",
    "Charlotte",
    "Daisy",
    "Diana",
    "Edith",
    "Eleanor",
    "Elizabeth",
    "Ella",
    "Emilia",
    "Emily",
    "Emma",
    "Evelyn",
    "Florence",
    "Francesca",
    "Georgina",
    "Grace",
    "Harriet",
    "Hazel",
    "Imogen",
    "Isabella",
    "Jemima",
    "Jessica",
    "Josephine",
    "Katherine",
    "Kitty",
    "Lily",
    "Louisa",
    "Lucy",
    "Margaret",
    "Matilda",
    "Miranda",
    "Molly",
    "Natalia",
    "Olivia",
    "Penelope",
    "Philippa",
    "Rebecca",
    "Rose",
    "Sarah",
    "Victoria",
    "Madeleine",
]


lastnames = [
    "Adams",
    "Allen",
    "Anderson",
    "Baker",
    "Banks",
    "Barnes",
    "Bell",
    "Bennett",
    "Bishop",
    "Black",
    "Blair",
    "Booth",
    "Bradley",
    "Brown",
    "Butler",
    "Campbell",
    "Carter",
    "Clark",
    "Clarke",
    "Collins",
    "Cook",
    "Cooper",
    "Cox",
    "Crawford",
    "Cross",
    "Davies",
    "Davis",
    "Dawson",
    "Dean",
    "Dixon",
    "Doyle",
    "Dunn",
    "Edwards",
    "Evans",
    "Fisher",
    "Foster",
    "Fox",
    "Fraser",
    "Freeman",
    "Gallagher",
    "Gibson",
    "Gilbert",
    "Gordon",
    "Graham",
    "Grant",
    "Gray",
    "Green",
    "Griffiths",
    "Hall",
    "Hamilton",
    "Hancock",
    "Harrison",
    "Harvey",
    "Hayes",
    "Henderson",
    "Henry",
    "Hill",
    "Holmes",
    "Hopkins",
    "Hughes",
    "Hunter",
    "Jackson",
    "James",
    "Jenkins",
    "Johnson",
    "Jones",
    "Kelly",
    "Kennedy",
    "King",
    "Knight",
    "Lane",
    "Lawrence",
    "Lee",
    "Lewis",
    "Lloyd",
    "Long",
    "Lowe",
    "Mackenzie",
    "Marshall",
    "Martin",
    "Mason",
    "Matthews",
    "McDonald",
    "McKay",
    "McKenzie",
    "Miller",
    "Mills",
    "Mitchell",
    "Moore",
    "Morgan",
    "Morris",
    "Murphy",
    "Murray",
    "Nelson",
    "Newman",
    "Palmer",
    "Parker",
    "Patel",
    "Nicholson",
]


def generate_random_int():
    """Generate a random integer between 1000 and 9999"""
    return random.randint(1000, 9999)


def personnummer():
    """Generate a random swedish personnummer in the format YYYYMMDD-XXXX, not valid, just random"""
    start = datetime.date(1958, 1, 1)
    end = datetime.date(2005, 12, 31)
    return f"{(start + (end - start) * random.random()).strftime('%Y%m%d')}-{generate_random_int()}"


def random_adress():
    """Generate a random swedish adress in the format Väg 1, 12345 Stad"""
    city = ["PepeLaugh", "TriHard"]
    street = [
        "Kappa",
        "PogChamp",
        "LUL",
        "CoolStoryBro",
        "FeelsGoodMan",
        "PJSalt",
        "monkaS",
        "SwiftRage",
        "NotLikeThis",
        "BibleThump",
        "Keepo",
        "Kreygasm",
        "DansGame",
        "FailFish",
        "4Head",
        "Jebaited",
        "MingLee",
        "SMOrc",
        "Bigglesworth",
        "ResidentSleeper",
    ]
    street_number = random.randint(1, 100)
    post_code = f"{random.randint(10, 99)}{random.randint(100, 999)}"
    return (
        f"{random.choice(street)} {street_number}, "
        + f"{post_code}, "
        + f"{random.choice(city)}"
    )


def employees():
    """Generate a random tenant choosing a random name from the lists of names, and other functions"""
    first = random.choice(firstnames)
    last = random.choice(lastnames)
    social = personnummer()
    address = random_adress()
    role = position()
    # the phone can be generated in one randint but i wanted every number randomly generated
    phone = f"072{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}"
    email_type = ["@itscrap.io"]
    email = f"{first}.{last}{random.choice(email_type)}".lower()
    # Modify this for your own needs and type of data. Here everything is a string
    return f"{first}, {last}, {address}, {social}, {phone}, {email}, {role}"


def create_column():
    firstname = "Firstname"
    lastname = "Lastname"
    address = "Street_name"
    postalcode = "Postalcode"
    location = "Location"
    social = "Social"
    phone = "Phone"
    email = "Email"
    position = "Position"
    return f"{firstname}, {lastname}, {address}, {postalcode}, {location}, {social}, {phone}, {email}, {position}"


def position():
    roles = ["Management", "Sales", "Consultant", "Accounting", "IT"]
    role = random.choice(roles)
    return role


def csv_export():
    """This function skips the sorting and just exports the tenants to a csv file"""
    with open("dupe_employees.csv", "a", encoding="UTF-8") as f:
        f.write(f"{create_column()}\n")
        for i in range(200):
            data = employees()
            f.write(f"{data}\n")
        f.close()


def remove_duplicates(input_file, output_file):
    emails_seen = []
    rows_to_write = []

    with open(input_file, "r", newline="") as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            email = row[" Email"]
            if email not in emails_seen:
                emails_seen.append(email)
                rows_to_write.append(row)

    with open(output_file, "w", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        for row in rows_to_write:
            writer.writerow(row)

    print(f"{input_file} processed. Unique rows written to {output_file}")


def delete_files(files_to_delete):
    for file_to_delete in files_to_delete:
        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)
            print(f"The file {file_to_delete} has been deleted.")
        else:
            print(f"The file {file_to_delete} does not exist.")


def main():
    """Just comment out the functions you don't want to use"""
    files_to_delete = ["employees.csv", "dupe_employees.csv"]
    delete_files(files_to_delete)
    csv_export()
    remove_duplicates("dupe_employees.csv", "employees.csv")


if __name__ == "__main__":
    main()
