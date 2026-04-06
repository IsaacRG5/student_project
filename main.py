from functions import *

# Function that displays the main menu
def Show_menu ():
    print("""
        =========== student registration =========== 
        
        1. Add students
        2. View student list
        3. Search for student
        4. Update student information
        5. Delete student
        6. Exit
        """)
    
# Main function of the program
def main ():
    
    inventory = []
    option = 0
    
    # The program runs until the user chooses to exit
    while option != 6:
        
        Show_menu()
        
        # We tried to convert the option to a number
        try:
            option = int(input("Select an option: "))
        except ValueError: 
            print("Error, please enter a valid option")
            continue 
        
        # -------- OPTION 1: Add student --------
        if option == 1 :
            
            #valid: id, name, years, course_program, status
            try :
                id = int(input("Add your id "))
            except ValueError:
                print ("Error, the option is invalid.")
                continue
                
            name = input("Add your name: ")
            if name == " " and name.isalnum() :
                print("Error, the name cannot be empty")
                continue
            
            try :
                age = int(input("Add you age: "))
            except ValueError:
                print("Error, the option is invalid.")
                continue
            
                
            course_program = input("Add your course or program: ")
            if course_program == "" and course_program.isalnum() :
                print("Error, the name cannot be empty")
                continue
            
                
            state = input("Is the student active? (active / inactive): ")
            if state == "" and state.isalnum():
                print("Error, the name cannot be empty")
                continue
            
            # We call the function that adds the student
            Add_student(inventory,id,name,age,course_program,state)
            
        if option == 2:
            show_inventory(inventory)
            
        # -------- OPTION 3: Search for student --------    
        if option == 3:
            
            choose = input("Search for student by id or name: (id/name)")
            if choose == "" and name.isalnum() :
                print("Error, the name cannot be empty")
                continue
            
            if choose == "id":
                name = input("Student to be found: ").lower
                if  name == "" :
                    print("Error, the name cannot be empty")
                    continue
                    
                student = search_student(inventory, id, name)
                
                if student:
                    print("student found: ", student)
                else:
                    print("student not found")  
                    
            if choose == "name":
                name = input("Student to be found: ").lower
                if  name == "" :
                    print("Error, the name cannot be empty")
                    continue
                    
                student = search_student(inventory, id, name)
                if student:
                    print("student found: ", student)
                else:
                    print("student not found")
                
        # -------- OPTION 4: Update students --------        
        if option == 4:
            
            #It asks if you want to update by ID or by name.
            choose = input("Search for student by id or name: (id/name)")
            if choose == "" and name.isalnum() :
                print("Error, the name cannot be empty")
                continue
            
            
            #update and validate
            if choose == "id":
                
                name = input("student to update: ")
                if name == "" and name.isalnum() :
                    print("Error, the name cannot be empty")
                    continue
                
                try :
                    age = int(input("New Age: ")) 
                except ValueError:
                    print("Error, the option is invalid.")
                
                course_program = input("New course or program")
                if course_program == "" and course_program.isalnum() :
                    print("Error, the name cannot be empty")
                    continue
                
                state = input("the student is still active?  (active / inactive): ")
                if state == "" and state.isalnum():
                    print("Error, the name cannot be empty")
                    continue
                
            if choose == "name":
                
                name = input("student to update: ")
                if name == "" and name.isalnum() :
                    print("Error, the name cannot be empty")
                    continue
                
                try :
                    age = int(input("New Age: ")) 
                except ValueError:
                    print("Error, the option is invalid.")
                
                course_program = input("New course or program: ")
                if course_program == "" and course_program.isalnum() :
                    print("Error, the name cannot be empty")
                    continue
                
                state = input("the student is still active?  (active / inactive): ")
                if state == "" and state.isalnum():
                    print("Error, the name cannot be empty")
                    continue
                
                update_student(inventory, id,name,age,course_program,state)
                
        
        # -------- OPTION 5: Remove student --------        
        if option == 5 :
            
            #asks if you want to delete by id or by name
            choose = input("Delete student by id or name: (id/name)")
            if choose == "" and name.isalnum() :
                print("Error, the name cannot be empty")
                continue
            
            if choose == "id":
                name = input("student to be eliminated: ")
                if name == "" and name.isalnum() :
                    print("Error, the name cannot be empty")
                delete_student(inventory,id,name)
                
                
            if choose == "name":
                name = input("student to be eliminated: ")
                if name == "" and name.isalnum() :
                    print("Error, the name cannot be empty")
                delete_student(inventory,id,name)
                    


main()