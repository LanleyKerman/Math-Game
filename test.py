# this is the code for addition only.

from tkinter import *
import random


class Addition:
    def run(self):
        self.master.mainloop()

    def __init__(self):
        self.master = Tk()
        self.master.title('Addition')
        self.master.resizable(False, False)

        self.value1 = 0
        self.value2 = 0
        self.total = 0
        self.streak = 0

        self.streak1 = Label(self.master, text=f'Current streak is {self.streak}')
        self.question = Label(self.master, text='')
        self.entry = Entry(self.master, font=('Tw Cen Mt', 25), cursor='dotbox')
        self.submit = Button(self.master, text='Submit', command=self.check_answer)
        self.quit = Button(self.master, text='Quit', command=self.master.quit)
        self.next = Button(self.master, text='Next', command=self.next_question)

        self.streak1.grid(row=0, column=0, pady=10)
        self.question.grid(row=1, column=0, pady=10)
        self.entry.grid(row=2, column=0, padx=10)
        self.submit.grid(row=3, column=0, pady=10)
        self.quit.grid(row=4, column=0, pady=10)
        self.next.grid(row=3, column=1, pady=10)

        self.new_question()

    def new_question(self):
        self.entry.delete(0, END)
        self.next.config(state=DISABLED)

        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)
        self.correct_ans = self.x + self.y

        self.question.config(text=f"What is the sum of {self.x} and {self.y}?")

    def next_question(self):
        self.entry.delete(0, END)
        self.next.config(state=DISABLED)
        self.submit.config(state=NORMAL)

        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)
        self.correct_ans = self.x + self.y

        self.question.config(text=f"What is the sum of {self.x} and {self.y}?")

    def check_answer(self):
        # get user's answer
        user_ans = self.entry.get()

        # check if it's an integer
        try:
            user_ans = int(user_ans)
        except ValueError:
            self.question.config(text="Error!")
            self.submit.config(state=DISABLED)
            self.next.config(state=DISABLED)
            return

        # check if it's correct
        if user_ans == self.correct_ans:
            self.question.config(text=f"Correct! {self.x} + {self.y} = {self.correct_ans}")
            self.submit.config(state=DISABLED)
            self.next.config(state=NORMAL)
            self.streak += 1
            self.streak1.config(text=f"Current streak: {self.streak}")
        else:
            self.question.config(text=f"Incorrect! {self.x} + {self.y} = {self.correct_ans}")
            self.submit.config(state=DISABLED)


if __name__ == '__main__':
    addition = Addition()
    addition.run()
