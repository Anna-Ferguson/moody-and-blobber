from Blobber_info import Blobber
def main():
    name = input("Enter your Blobber's name: ")
    color = input("Enter your Blobber's color: ")
    radius = eval(input("Enter your Blobber's radius: "))
    height = eval(input("Enter your Blobber's height: "))
    myBlobber = Blobber(name, color, radius, height)
    done = False
    while not done:
        print()
        print("Main Menu")
        print("\t(1) Display Name")
        print("\t(2) Change Name")
        print("\t(3) Display Color")
        print("\t(4) Change Color")
        print("\t(5) Feed Blobber")
        print("\t(6) Blobber Speak")
        print("\t(7) Exit")
# Display current vitals and check to see if it has turned to dust
# This will catch cases where the Blobber was fed too much as well
        print("Your Blobber is at " + str(myBlobber.vitalsOK,) + " happiness")
        if not myBlobber.blobberOK:
            print("Your Blobber turned to dust")
            break
        choice = eval(input("Make a selection: "))
        print()
        # Check to see if the Blobber turned to dust while waiting for the user to make a selection
        if not myBlobber.blobberOK:
            print("Your Blobber is at " + format(myBlobber.vitalsOK, ".2%") + " happiness")
            print("Your Blobber turned to dust")
            break
        if choice == 1:
            myBlobber.displayName()
        elif choice == 2:
            myBlobber.changeName(name)
        elif choice == 3:
            myBlobber.displayColor()
        elif choice == 4:
            myBlobber.changeColor()
        elif choice == 5:
            myBlobber.feedBlobber()
        elif choice == 6:
            myBlobber.blobberSpeak()
        elif choice == 7:
            done = True
print("Thanks for taking care of a Blobber")


    
main()