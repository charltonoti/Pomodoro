import time


def countdown(clock):
    while clock: 
        seconds = clock % 60
        minutes = clock // 60
        timer = '{:01d}:{:02d}'.format(minutes, seconds)
        print(timer, end = "\r")
        time.sleep(1)
        
        clock -=1
    print("It's break out and away we go!! Get working!!")
    
clock = input("Enter your countdown in seconds:")

countdown(int(clock))

def pomodoro(): 
    print("Pomodoro seesion has started")
    for i in range(5):
        session = 60 * 25
        while session: 
            seconds = session % 60
            minutes = session // 60
            timer = '{:01d}:{:02d}'.format(minutes, seconds)
            print(timer, end = "\r")
            time.sleep(1)
            session -=1
        
        print("Cool down!!")
        
        session = 5 * 25
        while session: 
            seconds = session % 60
            minutes = session // 60
            timer = '{:01d}:{:02d}'.format(minutes, seconds)
            print(timer, end = "\r")
            time.sleep(1)
            session -=1
            
        print("Back to work!!")
        
pomodoro()
        
    