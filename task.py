import sys
# print("Hello, World!")


def helpMsg():
    msg='''Usage :-
$ ./task add 2 hello world    # Add a new item with priority 2 and text "hello world" to the list
$ ./task ls                   # Show incomplete priority list items sorted by priority in ascending order
$ ./task del INDEX            # Delete the incomplete item with the given index
$ ./task done INDEX           # Mark the incomplete item with the given index as complete
$ ./task help                 # Show usage
$ ./task report               # Statistics'''
    sys.stdout.buffer.write(msg.encode('utf8'))

def displayList():
    task={"":""}
    try:
        with open("task.txt","r") as file:
            for line in file:
                if(line.strip()):
                    it=line.strip().split()                
                    task[it[-1]]=' '.join([var for var in it[:-1]])    
        taskSorted=sorted(task.items())
        return taskSorted
    except:
        return 1

def addItem(priority,task):
    sys.stdout.buffer.write(f'Added task: "{task}" with priority {priority}'.encode('utf8'))
    with open("task.txt","a") as file:
        items=task+" "+priority
        file.write(items)
        file.write("\n")
        
        
def deleteTask(index):
    taskSorted=displayList()
    if(index == 0):
        sys.stdout.buffer.write(f"Error: task with index #{index} does not exist. Nothing deleted.".encode('utf8'))
    try:
        deletedtask=taskSorted[index][1]+" "+taskSorted[index][0]
        with open("task.txt", "r") as f:
            lines = f.readlines()
        with open("task.txt", "w") as f:
            for line in lines:
                if line.strip("\n") !=deletedtask:
                    f.write(line)
        sys.stdout.buffer.write(f"Deleted task #{index}".encode('utf8'))
    except:
        sys.stdout.buffer.write(f"Error: task with index #{index} does not exist. Nothing deleted.".encode('utf8'))

def completedTask(index):
    taskSorted=displayList()
    # completed=[]
    if(index == 0):
        sys.stdout.buffer.write(f"Error: no incomplete item with index #{index} exists.".encode('utf8'))
    try:
        completedTask=taskSorted[index][1]+" "+taskSorted[index][0]
        with open("completed.txt","a") as file:
            file.write(taskSorted[index][1])
            file.write("\n")
        with open("task.txt", "r") as f:
            lines = f.readlines()
        with open("task.txt", "w") as f:
            for line in lines:
                if line.strip("\n") !=completedTask:
                    f.write(line)
        sys.stdout.buffer.write(f"Marked item as done.".encode('utf8'))     
    except:
        sys.stdout.buffer.write(f"Error: no incomplete item with index #{index} exists.".encode('utf8'))


if __name__ == "__main__":
    var1 = sys.argv[1] if len(sys.argv) >= 2 else ''
    var2 = sys.argv[2] if len(sys.argv) >= 3 else ''
    var3 = sys.argv[3] if len(sys.argv) >= 4 else ''

    if(var1=='' or var1=='help'):
        helpMsg()
    if(var1=="add"):
        addItem(var2,var3)
    if(var1 == "add" and not var2):
        sys.stdout.buffer.write(f"Error: Missing tasks string. Nothing added!".encode('utf8'))
        
        
    if(var1=="ls"):
        taskSorted=displayList()
        if(taskSorted == 1):
            sys.stdout.buffer.write(f"There are no pending tasks!".encode('utf8'))
        else:
            for index in range(len(taskSorted)):
                if index==0:
                    continue
                sys.stdout.buffer.write(f"{index}. {taskSorted[index][1]} [{taskSorted[index][0]}]\n".encode('utf8'))
    if(var1 == "del"):
        if(not var2):
            sys.stdout.buffer.write(f"Error: Missing NUMBER for deleting tasks.".encode('utf8'))
        else:
            deleteTask(int(var2))
            
    # if (var1=='del'):
    #     deleteTask(int(var2))
        
    if(var1=='done'):
        if(not var2):
            sys.stdout.buffer.write(f"Error: Missing NUMBER for marking tasks as done.".encode('utf8'))
        else:
            com=completedTask(int(var2))
                
    if (var1=='report'):
        pending=displayList()
        sys.stdout.buffer.write(f"Pending : {(len(pending)-1)}\n".encode('utf8'))
        for index in range(len(pending)):
            if index==0:
                continue
            sys.stdout.buffer.write(f"{index}. {pending[index][1]} [{pending[index][0]}]\n\n".encode('utf8'))    
        # print(" ")
        with open("completed.txt", "r") as f:
            lines = f.readlines()
            sys.stdout.buffer.write(f"Completed : {len(lines)}\n".encode('utf8'))
            counter=1
            for line in lines:
                line=line.strip()
                sys.stdout.buffer.write(f"{counter}. {line.strip()}\n".encode('utf8'))
                counter+=1
