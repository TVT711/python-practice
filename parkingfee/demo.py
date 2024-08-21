from ParkingSystem import ParkingSystem


def main():
    system = ParkingSystem("data/ParkingPrice.json")
    while True:
        print("Choose an option: (1) Park, (2) Pick-up, (3) History, (4) Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            car_id = input("Enter car identity: ")
            start_time = input("Enter start time (YYYY-MM-DD HH:MM): ")
            freq_num = input("Enter frequent parking number (optional): ")
            system.park_car(car_id, start_time, freq_num)
        elif choice == '2':
            car_id = input("Enter car identity for pickup: ")
            end_time = input("Enter end time (YYYY-MM-DD HH:MM): ")
            system.pick_up_car(car_id, end_time)
        elif choice == '3':
            car_id = input("Enter car identity to view history: ")
            system.view_history(car_id)
        elif choice == '4':
            print("Exiting system.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
