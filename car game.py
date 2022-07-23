# this code is only for practise
command=""
started=False
while True:
    command=input('>').lower()
    if command=="start":
        if started:
            print('car is already started!')
        else:
            started=True
            print('car started')
    elif command =="stop":
        if not started:
            print('car is already stopped')
        else:
            started=False
            print('car stopped')
    elif command =="help":
       print( """
start-  to start a car
stop- to stop a car
quit - end a game
    """)
    elif command== 'quit':
         break
    else:
        print('i dont understand')








