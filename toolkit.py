import socket

print("PENETRATION TESTING TOOLKIT")
print("---------------------------")

while True:
    print("\n1. Port Scanner")
    print("2. Brute Force Demo")
    print("3. Exit")

    choice = input("Select option: ")

    if choice == "1":
        target = input("Enter target host: ")
        ports = [21,22,23,25,53,80,110,443]

        print("\nScanning ports...\n")

        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                print("Port", port, "is OPEN")
            else:
                print("Port", port, "is closed")

            s.close()

    elif choice == "2":

        print("\nBrute Force Demo")

        password = "admin123"
        wordlist = ["12345","password","admin","admin123","welcome"]

        for guess in wordlist:
            print("Trying:", guess)

            if guess == password:
                print("Password Found:", guess)
                break

    elif choice == "3":
        print("Exiting Toolkit")
        break

    else:
        print("Invalid option")