from tkinter import* 
from random import randint  
from tkinter import ttk

root=Tk()
root.title("my window name")
label=Label(root,font=("Arial",21),text="game of rock,paper,scissoir",bg="black",fg="white")
label.pack()
root.geometry("800x900+300+200")
root.resizable(0,0)
# root.mainloop()

rock=PhotoImage(file="/home/anushka/Downloads/ocks.pngr")
paper=PhotoImage(file="/home/anushka/Downloads/papers.png")
scissoir=PhotoImage(file="/home/anushka/Downloads/scissorss.png")
var = StringVar()
image_list=[rock,paper,scissoir]
pick_number=randint(0,2)

image_label=Label(root,image=image_list[pick_number])
image_label.pack(pady=20)

#create spin function
    
def spin():
    pick_number=randint(0,2)
    image_label.config(image=image_list[pick_number])
    def win():
        print("you win!")

    def lose():
        print("you loss!")
    while True:
        player_choice=input("what do you pick?(rock,paper,scissors)")
        player_choice.strip()
        random_moves=randint(0,2)
        moves=["rock","paper","scissors"]
        computer_choice=moves[random_moves]
        print(computer_choice)
        # if computer_choice == 1:
        #     computer_choice = 'rock'
        # elif computer_choice ==2:
        #     computer_choice = 'paper'
        # else:
        #     computer_choice= 'scissors'

        if player_choice==computer_choice:
            print("choice your option")
        elif player_choice=="rock" or computer_choice=="scissors":
            win()
        elif player_choice=="paper" or computer_choice=="scissors":
            lose()
        elif player_choice=="scissors" or computer_choice=="paper":
            win()
        elif player_choice=="scissors" or computer_choice=="rock":
            lose()
        elif player_choice=="paper" or computer_choice=="rock":
            win()
        again=input("do you want play again? (y or no").strip()
        if again=="n":
            break

        if player_choice==0:
            if pick_number==0:
                win_lose_label.config(text="Its A Tie! spin again...")
            elif pick_number==1:
                win_lose_label.config(text="paper cover rock! you lose....")
            elif pick_number==2:
                win_lose_label.config(text="rock cutes smashes scissors! you win")

        #if user piks paper
        if player_choice==1:
            if pick_number==1:
               win_lose_label.config(text= "Its A Tie! spin again...")
            elif pick_number==0:
                win_lose_label.config(text ="paper cover rock! you win....")
            elif pick_number==2:
                win_lose_label.config(text= "scissors cutes paper! you loss")

        #if user piks scissors
        if player_choice==2:
            if pick_number==2:
                win_lose_label.config(text="Its A Tie! spin again...")
            elif pick_number==0:
                win_lose_label.config(text = "rock smashes scissors! you lose....")
            elif pick_number==1:
               win_lose_label.config(text="scissors cutes paper! scissors! you win")
            
            
#make our choice
player_choice=ttk.Combobox(root,value=("rock","paper","scissoir"))
player_choice.current(0)
player_choice.pack(pady=20)

#create a spin button
spin_button=Button(root,text="spin!",command=spin)
spin_button.pack(pady=10)

exit_button=Button(root,text="exit!",command=exit)
exit_button.pack(pady=100)

#label for showing if you won or not
win_lose_label=Label(root,text=var.get(),font=("Helvetica",18))
win_lose_label.pack(pady=50)


root.mainloop()


