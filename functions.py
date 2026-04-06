# Add a student to the inventory
def Add_student (inventory,id,name,age,course_program,state):
    
    # We created a dictionary with student data
    student = {
        "id" : id,
        "name": name,
        "age" : age,
        "course_program": course_program,
        "state": state, 
    }
    
    # We saved the student on the list
    inventory.append(student)
    print("Student added correctly")
    
    
# Show all students in the inventory
def show_inventory (inventory):
    
        # If the inventory is empty, it is reported
        if not inventory :
            print("empty inventory")  
            return
        
        
        # We go through the list and print each student's name.
        for p in inventory:
            print(p["id"], "| Name: ", p["name"], "| age: ", p["age"], "| Course_Program: ", p["course_program"], "| State: ", p["state"])
            
            
# Search for a product by its ID and name           
def search_student (inventory, id , name):
    for p in inventory:
        if p["id"] == id or p["name"] == name:
            return p

    return None

#search for the student by ID and name
def update_student(inventory,id,name,age,course_program,state ):
    
    student = search_student(inventory,id,name)
    
    if student :
        student["age"] = age
        student["course_program"] = course_program
        student["state"] = state
        print("updated student")
    else:
        print("student not found")  

#Remove the student from the inventory        
def delete_student(inventory,id,name):
    
    student = search_student(inventory,id, name)   
        
    if student:
        inventory.remove(student)
        print("student removed")
    else:
        print("student not found")
        