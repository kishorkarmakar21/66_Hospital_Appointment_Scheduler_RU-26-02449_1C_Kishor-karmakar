appointment_id = 101
appointments = {}

while True:

    print("\n================================")
    print(" HOSPITAL APPOINTMENT SCHEDULER")
    print("================================")

    print("1. Book Appointment")
    print("2. View All Appointments")
    print("3. Reschedule Appointment")
    print("4. Cancel Appointment")
    print("5. Exit")

    choice = input("Enter your choice: ")

    print("You selected:", choice)

    if choice == "1":

        print("\n--- Book Appointment ---")

        name = input("Enter Patient Name: ")
        doctor = input("Enter Doctor Name: ")
        date = input("Enter Appointment Date: ")
        time = input("Enter Appointment Time: ")

        appointments["A" + str(appointment_id)] = {
            "name": name,
            "doctor": doctor,
            "date": date,
            "time": time
        }

        print("\nAppointment ID: A" + str(appointment_id))
        print("Appointment Details")
        print("Patient:", name)
        print("Doctor:", doctor)
        print("Date:", date)
        print("Time:", time)

        appointment_id = appointment_id + 1

    elif choice == "2":

        print("\n--- All Appointments ---")

        if len(appointments) == 0:
            print("No appointments found.")

        else:
            for app_id, details in appointments.items():

                print("\nAppointment ID:", app_id)
                print("Patient:", details["name"])
                print("Doctor:", details["doctor"])
                print("Date:", details["date"])
                print("Time:", details["time"])
    elif choice == "3":

        print("\n--- Reschedule Appointment ---")

        app_id = input("Enter Appointment ID: ")

        if app_id in appointments:

            new_date = input("Enter New Date: ")
            new_time = input("Enter New Time: ")

            appointments[app_id]["date"] = new_date
            appointments[app_id]["time"] = new_time

            print("Appointment Rescheduled Successfully!")

        else:
            print("Appointment ID not found.")
    elif choice == "4":

        print("\n--- Cancel Appointment ---")

        app_id = input("Enter Appointment ID: ")

        if app_id in appointments:

            del appointments[app_id]

            print("Appointment Cancelled Successfully!")

        else:
            print("Appointment ID not found.")
    elif choice == "5":

        print("Thank you for using Hospital Appointment Scheduler!")
        break

    else:
        print("This option is not available yet.")
