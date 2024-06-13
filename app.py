import sys
sys.path.append('/home/favor/LABS/END OF PHASE PROJECTS/FitLife-Harmony')

from db.set_tables import create_tables
from helpers import (
    exit_program,
    add_member,
    add_equipment,
    add_trainer,
    add_workout,
    delete_equipment,
    delete_member,
    delete_trainer,
    delete_workout,
    update_equipment,
    update_member,
    update_trainer,
    update_workout,
    view_all,
    all_equipment,
    all_trainers,
    all_workouts,
    search_member_by_id,
    search_member_by_name,
    search_equipment_by_name,
    search_trainer_by_id,
    search_trainer_by_name,
    search_workout_by_id,
    search_workout_by_time,
    workouts_by_trainer
)

def display():
    print("Select an option:")
    print("1. Leave.")
    print("2. Add a new member.")
    print("3. Remove a member.")
    print("4. Update details of a member.")
    print("5. Display all members.")
    print("6. Search for a member by name.")
    print("7. Search for a member by id.")
    print("8. Find workout by time.")
    print("9. Find a workout by its id.")
    print("10. Add a workout.")
    print("11. Delete a workout.")
    print("12. Update details of a workout.")
    print("13. View all workouts.")
    print("14. Add a trainer.")
    print("15. Delete a trainer.")
    print("16. Update details of a trainer.")
    print("17. View all trainers.")
    print("18. Display workouts by a certain trainer.")
    print("19. Find a trainer by id.")
    print("20. Find a trainer by name.")
    print("21. Add new equipment.")
    print("22. Remove equipment.")
    print("23. Update details of equipment.")
    print("24. Find equipment by name.")
    print("25. View all equipment.")

def display_welcome_image():
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
    "Welcome to FitLife Harmony"
    """
    print(welcome_ascii)

def main():
    create_tables()
    while True:
        display_welcome_image()
        display()
        choice = input("Enter your choice: ")

        if choice == '1':
            exit_program()
        elif choice == '2':
            add_member()
        elif choice == '3':
            delete_member()
        elif choice == '4':
            update_member()
        elif choice == '5':
            view_all()
        elif choice == '6':
            search_member_by_name()
        elif choice == '7':
            search_member_by_id()
        elif choice == '8':
            search_workout_by_time()
        elif choice == '9':
            search_workout_by_id()
        elif choice == '10':
            add_workout()
        elif choice == '11':
            delete_workout()
        elif choice == '12':
            update_workout()
        elif choice == '13':
            all_workouts()
        elif choice == '14':
            add_trainer()
        elif choice == '15':
            delete_trainer()
        elif choice == '16':
            update_trainer()
        elif choice == '17':
            all_trainers()
        elif choice == '18':
            workouts_by_trainer()
        elif choice == '19':
            search_trainer_by_id()
        elif choice == '20':
            search_trainer_by_name()
        elif choice == '21':
            add_equipment()
        elif choice == '22':
            delete_equipment()
        elif choice == '23':
            update_equipment()
        elif choice == '24':
            search_equipment_by_name()
        elif choice == '25':
            all_equipment()
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
