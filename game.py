from tkinter import *
from PIL import Image,ImageTk
import random

class game():
    def __init__(self):
        self.root=Tk()
        self.root.title("Rock Paper Scissor")
        self.root.config(bg="black")
        self.root.geometry("530x350")
        self.root.resizable(False,False)
        self.pc_score=0
        self.user_score=0
        self.List=["rock","paper","scissor"]

        self.image_rock1=ImageTk.PhotoImage(Image.open("rock.jpeg").resize((80,80)))
        self.image_paper1=ImageTk.PhotoImage(Image.open("paper.jpeg").resize((80,80)))
        self.image_scissor1=ImageTk.PhotoImage(Image.open("scissor.jpeg").resize((80,80)))
        self.image_rock2=ImageTk.PhotoImage(Image.open("rock_copy.jpeg").resize((80,80)))
        self.image_paper2=ImageTk.PhotoImage(Image.open("paper_copy.jpeg").resize((80,80)))
        self.image_scissor2=ImageTk.PhotoImage(Image.open("scissor_copy.jpeg").resize((80,80)))

        self.pc=Label(self.root,text="Computer",fg="red",bg="black",font=("arial",20,"bold")).grid(row=0,column=0,pady=5)
        self.User=Label(self.root,text="You",fg="red",bg="black",font=("arial",20,"bold")).grid(row=0,column=2,pady=5)

        self.computer=Label(self.root,image=self.image_rock1)
        self.computer.grid(row=1,column=0,pady=5)
        self.vs=Label(self.root,text="VS",bg="black",fg="white",font=("arial",25,"bold"))
        self.vs.grid(row=1,column=1,ipadx=100,pady=5)
        self.user=Label(self.root,image=self.image_rock2)
        self.user.grid(row=1,column=2,pady=5) 
        self.score_1=Label(self.root,text="Score:0",bg="black",fg="red",font=("arial",25,"bold"))
        self.score_1.grid(row=2,column=0,pady=5)
        self.score_2=Label(self.root,text="Score:0",bg="black",fg="red",font=("arial",25,"bold"))
        self.score_2.grid(row=2,column=2,pady=5)
        self.rock=Button(self.root,text="Rock",bg="#feb4b2",font=("arial",15),padx=25,command=self.rock).grid(row=3,column=0,pady=6)
        self.paper=Button(self.root,text="Paper",bg="#feb4b2",font=("arial",15),padx=25,command=self.paper).grid(row=3,column=1,pady=6)
        self.scissor=Button(self.root,text="Scissor",bg="#feb4b2",font=("arial",15),padx=25,command=self.scissor).grid(row=3,column=2,pady=6)
        self.winner=Label(self.root,bg="black",fg="red",font=("arial",25,"bold"))
        self.winner.grid(row=4,column=1,columnspan=1)
        self.reset=Button(self.root,text="Reset",fg="red",bg="black",font=("arial",15),command=self.reset).place(x=180,y=300)
        self.quit=Button(self.root,text="Quit",fg="red",bg="black",font=("arial",15),command=self.root.destroy).place(x=300,y=300)
        self.root.mainloop()

    def rock(self):
        user_choce="rock"
        pc_choice=random.choice(self.List)
        if pc_choice==user_choce:
            self.winner.config(text="Draw!")
        elif user_choce=="rock" and pc_choice=="scissor":
            self.winner.config(text="You Won!")
            self.user_score+=1
            self.score_2.config(text=f"Score:{self.user_score}")
        elif user_choce=="rock" and pc_choice=="paper":
            self.winner.config(text="You Lose!")
            self.pc_score+=1
            self.score_1.config(text=f"Score:{self.pc_score}")
        self.user.config(image=self.image_rock2)
        if pc_choice=="rock":
            self.computer.config(image=self.image_rock1)
        elif pc_choice=="paper":
            self.computer.config(image=self.image_paper1)
        else:
            self.computer.config(image=self.image_scissor1)
    def paper(self):
        user_choce="paper"
        pc_choice=random.choice(self.List)
        if pc_choice==user_choce:
            self.winner.config(text="Draw!")
        elif user_choce=="paper" and pc_choice=="rock":
            self.winner.config(text="You Won!")
            self.user_score+=1
            self.score_2.config(text=f"Score:{self.user_score}")
        elif user_choce=="paper" and pc_choice=="scissor":
            self.winner.config(text="You Lose!")
            self.pc_score+=1
            self.score_1.config(text=f"Score:{self.pc_score}")
        self.user.config(image=self.image_paper2)
        if pc_choice=="rock":
            self.computer.config(image=self.image_rock1)
        elif pc_choice=="paper":
            self.computer.config(image=self.image_paper1)
        else:
            self.computer.config(image=self.image_scissor1)


        
    def scissor(self):
        user_choce="scissor"
        pc_choice=random.choice(self.List)
        if pc_choice==user_choce:
            self.winner.config(text="Draw!")
        elif user_choce=="scissor" and pc_choice=="paper":
            self.winner.config(text="You Won!")
            self.user_score+=1
            self.score_2.config(text=f"Score:{self.user_score}")
        elif user_choce=="scissor" and pc_choice=="rock":
            self.winner.config(text="You Lose!")
            self.pc_score+=1
            self.score_1.config(text=f"Score:{self.pc_score}")
        self.user.config(image=self.image_scissor2)
        if pc_choice=="rock":
            self.computer.config(image=self.image_rock1)
        elif pc_choice=="paper":
            self.computer.config(image=self.image_paper1)
        else:
            self.computer.config(image=self.image_scissor1)
    def reset(self):
        self.score_1.config(text="Score:0")
        self.score_2.config(text="Score:0")
        self.computer.config(image=self.image_rock1)
        self.user.config(image=self.image_rock2)
        


        
if __name__=="__main__":
    game()