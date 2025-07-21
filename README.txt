*Task Manager CLI*

-What is?
    A useful software to keep track of your everyday tasks.

-What you need to run it?
    *Python > 3.8
    *It does not require any external library
    *Just write `python main.py` in your console or directly execute the main.py
    to run it

-Use cases

#Add a task
add 'Study Python' #Outcome> 'Study Python' added successfully (ID:1)

#Update a task
update 1 'Study C++' #Outcome> 'Study Python' changed successfully to 'Study C++'

#Delete a task
delete 1 #Outcome> 'Study C++' deleted successfully.

#Mark status
mark 1 done #Outcome> 'Study Python' status changed from 'Todo' to 'Done'

#List
list #Outcome> All tasks
list [status] #Outcome> Tasks with that specific status