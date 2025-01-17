from tkinter import *
from quizzer import Quizzer
from random import randrange

class Zetamac(Quizzer):
    def init_state(self):
        self.addn_spec = [(2,101),(2,101)]
        self.multn_spec = [(2,13),(2,101)]

    def next_problem(self):
        self.input_box.delete(0, END)
        self.problem_bar.configure(text = self.sample())

    def input_callback(self, var, idx, mode):
        # Check whether can be parsed as an int
        if self.input_var.get().isdigit():
            v = int(self.input_var.get())

            if v == self.answer:
                self.solved_ctr += 1
                self.next_problem()
        else:
            if self.input_var.get() == 'r':
                self.run_game()
            elif self.input_var.get() == 'e':
                self.end_game()

    def sample(self):
        # Grab pairs uniformly out of the distr,
        # return a string to display
        c = randrange(0,4)
        if c == 0:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            self.answer = a + b
            return ' + '.join((str(a), str(b)))
        elif c == 1:
            a,b = randrange(*self.addn_spec[0]), randrange(*self.addn_spec[1])
            c = a + b
            self.answer = a
            return ' - '.join([str(c), str(b)])
        elif c == 2:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a * b
            return ' * '.join([str(a), str(b)])
        elif c == 3:
            a,b = randrange(*self.multn_spec[0]), randrange(*self.multn_spec[1])
            self.answer = a
            return ' / '.join([str(a*b), str(b)])
   
