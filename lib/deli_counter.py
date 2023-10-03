katz_deli=[]

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        message = "The line is currently:" 
        for i in range(len(katz_deli)):
            message += f" {i + 1}. {katz_deli[i]}"
        print(message) 
                

def take_a_number(katz_deli, new_person):
    katz_deli.append(new_person)
    position = len(katz_deli)
    print(f"Welcome, {new_person}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) == 0:
        print("There is nobody waiting to be served!")
    else:
        serving_person = katz_deli.pop(0)
        print(f"Currently serving {serving_person}.")