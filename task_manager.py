import json


def load_tasks():
    with open('tasks.json' , 'r') as file:
        tasks = json.load(file)
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks,file)

while True:
    print("1.Add task")
    print("2.View tasks")
    print("3.Exit")
    print()
    user_input = int(input("Enter your choice: "))
    if user_input == 1:
        print("Mention task description")
        my_tasks = load_tasks()
        new_tasks = input()
        my_tasks.append(new_tasks)
        save_tasks(my_tasks)
    
    elif user_input == 2:
        my_tasks = load_tasks()
        if len(my_tasks) == 0:
            print("nothing in here")
        for i in range(len(my_tasks)):
            print( i + 1, my_tasks[i])
        
    elif user_input == 3:
        break

    elif user_input == 4:
        my_tasks = load_tasks()
        if len(my_tasks) == 0:
            print("Empty!")
        else:
            print("Enter task number to delete: ")
            deletion = int(input())
            index = deletion - 1
            my_tasks.pop(index)
            save_tasks(my_tasks)
        
        
        
   
     







