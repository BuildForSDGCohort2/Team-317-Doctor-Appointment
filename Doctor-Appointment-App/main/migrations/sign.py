import re
user_count = 0
users = {}
container = []


username = input('Username:')
password = int(input('Password: '))


# Patient Appointment Details
def getting_details_new_reg():
    while True:

        first_name = input('First_Name: ')
        if len(first_name) <= 0:
            print('name must not be less than 1 ')
        elif len(first_name) >= 15:
            break
            print('Name must not be longer than 15 characters')
        else:
            print('Name look good')

        last_name = input('last_name: ')
        if len(last_name) <= 0:
            print('Name must be at least 5 characters')
        elif len(last_name) >= 15:
            break
            print('Name must not be longer than 20 charaacters')
        else:
            print('Name look good')

        current_time = int(input('current_time: format 03h:23m:12s:\n'))
        if(current_time) <= 20213:
            print('Time must match hour,minutes,Seconds')
        elif(current_time) >= 120213:
            break
            print('Time should be in Hours,minutes,seconds')
        else:
            print('Good time')

        appointment_time = int(input(
            'appointment_time: In this formate 12:00pm: \n'))
        appointment_date = int(
            input('appointment_date: format 12/03/1993: \n '))

        details = [username, password, first_name, last_name,
                   current_time, appointment_time, appointment_date]
        return details


def homepage_login():

    login = int(
        input('Enter 0 for a new user to Book a medical Appointment: \n'))
    if login == 0:
        details = getting_details_new_reg()
        # compiling user for appointment
        users.append(details)
        container[user_count] = details
        print(users)
        homepage_login()


homepage_login()
