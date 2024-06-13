from models.equipment import Equipment
from models.members import Member
from models.trainers import Trainer
from models.workouts import Workout
from datetime import datetime

import re

def exit_program():
    welcome_ascii = """
      _____  
    /       \\
   |         |
   |  O   O  |
   |    ^    |
   |   '-'   |
    |_______|
      \\   /
       \\ /
    "Thanks for using my CLI!"
    """
    print(welcome_ascii)
    exit()

## MEMBER'S TABLE
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def add_member():
    name = input("Input member's name: ")
    email = input("Input member's email: ")

    if not is_valid_email(email):
        print("Invalid email format. Please try again.")
        return

    trainer_id = input("Input trainer's id: ")
    workout_id = input("Input workout id: ")

    try:
        member = Member.add(name, email, trainer_id, workout_id)
        print(f'Success: {member} added.')
    except Exception as exc:
        print("Error adding member: ", exc)

def delete_member():
    id = int(input ("Input member's id: "))
    member = Member.search_by_id(id)
    if member:
       member.delete()
       print(f"Member {id} deleted")
    else:
        print("Member not found")

def update_member():
    id = int(input("Input member's id: "))
    member = Member.search_by_id(id)
    if member:
       try:
            name = input("Member's name: ")
            member.name = name
            email = input("Input member's new email: ")
            if not is_valid_email(email):
                print("Invalid email format. Please try again.")
                return

            member.email = email
            trainer_id = int(input("Input member's new trainer id: "))
            member.trainer_id = trainer_id
            workout_id = int(input("Input member's new workout id: "))
            member.workout_id = workout_id

            member.update()
            print(f"Member {id} updated.")
       except Exception as exc:
            print("Error updating member: ", exc)
    else:
        print("Member not found.")


def view_all():
    members = Member.get_all()
    for member in members:
        print(member)

def search_member_by_name():
    name = input("Input member's name: ")
    member = Member.search_by_name(name)
    print(member) if member else print(f'Member {name} not found')

def search_member_by_id():
    id = int(input("Input member's id: "))
    member = Member.search_by_id(id)
    print(member) if member else print(f'Member {id} not found')

##WORKOUT'S TABLE
def validate_time_format(time_str):
    try:
        datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

def add_workout():
    name = input("Input workout's name: ")
    
    while True:
        scheduled_time = input("Input workout's time (HH:MM): ")
        if validate_time_format(scheduled_time):
            break
        else:
            print("Invalid time format! Please enter time in HH:MM format.")

    trainer_id = input("Input trainer's id: ")

    workout = Workout.add(name, scheduled_time, trainer_id)
    print(f'Success: {workout} added')

def search_workout_by_time():
    time = input("Input workout's time: ")
    workouts = Workout.search_by_time(time)
    if workouts:
     for workout in workouts:
      print(workout) 
    else:
        print("No workout at that time.")

def search_workout_by_id():
    id = int(input("Input workout id: "))
    workout = Workout.search_by_id(id)
    print(workout) if workout else print(
        f'{workout} not found')

def delete_workout():
    id = int(input ("Input workout id: "))
    workout = Workout.search_by_id(id)
    if workout:
       workout.delete()
       print(f"Workout {id} deleted")
    else:
        print("Workout not found")

def update_workout():
    id = input("Input workout's id: ")
    workout = Workout.search_by_id(id)
    
    if workout:
        try:
            name = input("Input workout's new name: ")
            workout.name = name
            
            while True:
                scheduled_time = input("Input workout's new time (HH:MM): ")
                if validate_time_format(scheduled_time):
                    workout.scheduled_time = scheduled_time
                    break
                else:
                    print("Invalid time format! Please enter time in HH:MM format.")

            trainer_id = input("Input workout's new trainer id: ")
            workout.trainer_id = trainer_id

            workout.update()
            print(f"Workout {id} updated.")
        except Exception as exc:
            print("Error updating workout: ", exc)
    else:
        print("Workout not found.")

def all_workouts():
    workouts = Workout.get_all()
    for workout in workouts:
     print(workout)

##TRAINER'S TABLE
def add_trainer():
    name = input("Input trainer's name: ")
    phone_number = input("Input trainer's phone number: ")
    
    pattern = re.compile(r'^0\d{9}$')
    if not pattern.match(phone_number):
       print("Invalid phone number.Try again.")
       return

    try:
        trainer = Trainer.add(name, phone_number)
        print(f"Success: {trainer} added.")
    except Exception as exc:
        print("Error adding trainer:", exc)

def delete_trainer():
    id = int(input ("Input trainer's id: "))
    trainer = Trainer.search_by_id(id)
    if trainer:
       trainer.delete()
       print(f"Trainer {id} deleted")
    else:
        print("Trainer not found")

def update_trainer():
    id = int(input("Input trainer's id: "))
    trainer = Trainer.search_by_id(id)
    if trainer:
        try:
            name = input("Input trainer's name: ")
            trainer.name = name
            phone_number = input("Input trainer's new phone number: ")
            
            pattern = re.compile(r'^0\d{9}$')
            if not pattern.match(phone_number):
                    print("Invalid phone number.Try again.")
                    return
           
            trainer.phone_number = phone_number
            trainer.update()
            print(f"Trainer {id} updated.")
        except Exception as exc:
            print("Error updating trainer: ", exc)
    else:
        print("Trainer not found.")


def all_trainers():
    trainers = Trainer.get_all()
    for trainer in trainers:
        print(trainer)

def workouts_by_trainer():
    id = int(input("Input trainer's id: "))
    workouts = Trainer.search_workout_by_trainer(id)
    if workouts:
        for workout in workouts:
            print(f"Workout ID: {workout['id']}, Name: {workout['name']}, Scheduled Time: {workout['scheduled_time']} ")
    else:
        print("No workouts for that trainer")

def search_trainer_by_name():
    name = input("Input trainer's name: ")
    trainer = Trainer.search_by_name(name)
    print(trainer) if trainer else print(f'{name} not found')

def search_trainer_by_id():
    id = int(input("Input trainer's id: "))
    trainer = Trainer.search_by_id(id)
    print(trainer) if trainer else print(f'{id} not found')

##EQUIPMENT'S TABLE
def add_equipment():
    name = input("Input equipment's name: ")
    quantity = int(input("Input equipment's quantity: "))
    condition = input("Input equipment's condition: ")
    user_id = int(input("Input user's id: "))
    price = int(input("Input equipment's price: "))
    
    try:
        equipment = Equipment.add(name, user_id, condition, price, quantity)
        print(f"Success: {equipment} added.")
    except Exception as exc:
        print("Error adding equipment:", exc)

def delete_equipment():
    name = (input("Input equipment's name: "))
    equipment = Equipment.search_by_name(name)
    if equipment:
        equipment.delete()
        print(f"Equipment {name} deleted")
    else:
        print("Equipment not found")

def update_equipment():
    name = input("Input equipment's name: ")
    equipment = Equipment.search_by_name(name)
    if equipment:
        try:
            new_name = input("Input equipment's new name: ")
            equipment.name = new_name
            condition = input("Input equipment's new condition: ")
            equipment.condition = condition
            user_id = int(input("Input equipment's new user's id: "))
            equipment.user_id = user_id
            price = int(input("Input equipment's new price: "))
            equipment.price = price
            quantity = int(input("Input equipment's new quantity: "))
            equipment.quantity = quantity
            equipment.update()
            print(f"Equipment {name} updated.")
        except Exception as exc:
            print("Error updating equipment: ", exc)
    else:
        print("Equipment not found.")

def search_equipment_by_name():
    name = input("Input equipment's name: ")
    equipment = Equipment.search_by_name(name)
    print(equipment) if equipment else print(f'{name} not found')

def all_equipment():
    all_equipment = Equipment.get_all()
    for equipment in all_equipment:
        print(equipment)
    