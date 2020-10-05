class Person:

    def __init__(self, first_name, last_name, sex, age, address):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex 
        self.age = age
        self.address = address
        self.email = first_name + '.' + last_name + '@company.com'

def menu():
    print("[1] Enter New User")
    print("[2] View Users")
    print("[3] Exit Program")
    print()

def main():
    menu()

    option = int(input("Enter Your Choice: "))

    persons = []
    while option != 3:
        if option == 1:
            first_name = input("Enter First Name - ")
            last_name = input("Enter Last Name - ")
            sex = input("Enter Sex - ")
            age = input("Enter Age - ")
            address = input("Enter Address - ")

            persons.append(Person(first_name, last_name, sex, age, address))


        elif option == 2:
            for person in persons:
                print(person.first_name)
                print(person.last_name)
                print(person.sex)
                print(person.age)
                print(person.address)
                print(person.email)

        
        else:
                print()
                print("Invalid Option")

    
        print()
        menu()
        option = int(input("Enter Your Choice: "))

    print("Exiting Program. Goodbye")


if __name__ == "__main__":
    main()

            

            
