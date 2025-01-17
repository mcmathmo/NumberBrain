from abc import ABC, ABCMeta, abstractmethod
from tkinter import *

class Quizzer(ABC):
    __metaclass__ = ABCMeta

    def __init__(self, numeracyapp):
        self.numeracyapp = numeracyapp

        # Clear previous menu
        numeracyapp.display_menu(clean=True)

        # Create elements, first time setup
        self.game_frame = Frame(numeracyapp.root, bg='red')

        self.header = Frame(self.game_frame, bg='green')
        self.timer = Button(self.header, text='timer', font=('Arial Bold', 25))
        self.ctr = Button(self.header, text='CTR', font=('Arial Bold', 25))
        self.meta = Button(self.header, text='hiscore, ma', font=('Arial Bold', 25))
        self.problem_bar = Label(self.game_frame, text='gottem', font=('Helvetica', 40))
        self.input_box = Entry(self.game_frame, font=('Helvetica', 20))

        # Wire a StringVar to the input box for input checking
        self.input_var = StringVar()
        self.input_var.trace_add('write', self.input_callback)
        self.input_box.configure(textvariable = self.input_var)

        # Create a variable pertaining to current valid timer, all others die 
        self.timer_id = 0

        # Pack into place
        self.game_frame.pack(fill=BOTH, expand=YES)
        self.header.pack(side=TOP, fill=X)
        self.timer.pack(side=LEFT, fill=X)
        self.ctr.pack(side=LEFT, fill=X)
        self.meta.pack(side=RIGHT, fill=X)
        self.problem_bar.pack(side=TOP)
        self.input_box.pack(side=TOP)
        self.input_box.pack(side=TOP)
    
        # Init for first problem
        self.init_state()
        self.run_game()

    def run_game(self):
        self.answer = None
        self.next_problem()
        self.solved_ctr = 0
        self.countdown(120)

    @abstractmethod
    def init_state(self):
        raise NotImplementedError("Must override this method")
    @abstractmethod
    def input_callback(self, var, idx, mode):
        raise NotImplementedError("Must override this method")
    @abstractmethod
    def next_problem(self):
        raise NotImplementedError("Must override this method")
    @abstractmethod
    def sample(self):
        raise NotImplementedError("Must override this method")
    
    def countdown(self, val):
        def _countdown(val, timer_id):
            if not (timer_id < self.timer_id):
                if val < 1:
                    print('done')
                    self.end_game()
                else:
                    print(val)
                    self.timer.configure(text=str(val))
                    self.numeracyapp.root.after(1000, _countdown, val - 1, timer_id)

        self.timer_id += 1
        _countdown(val, self.timer_id)

    def restore_game(self):
        self.end_frame.pack_forget()
        self.game_frame.pack(fill=BOTH, expand=YES)
        self.run_game()

    def restore_mainmenu(self):
        self.end_frame.pack_forget()
        self.numeracyapp.display_menu('main')
    
    def end_game(self):
        # Invalidate current timer
        self.timer_id += 1

        # Remove game_frame
        self.game_frame.pack_forget()

        # Get end screen
        self.end_frame = Frame(self.numeracyapp.root, bg='purple')
        self.end_frame.pack(fill=BOTH, expand=YES)

        self.end_score = Label(self.end_frame, text = str(self.solved_ctr), font=('Helvetica', 40))
        self.end_score.pack(side=TOP, fill=Y, expand=YES)

        self.end_options = Frame(self.end_frame, bg='maroon')
        self.go_again = Button(self.end_options, text='AGAIN', command=self.restore_game)
        self.go_mainmenu = Button(self.end_options, text='MAINMENU', command=self.restore_mainmenu)

        self.go_again.pack(side=LEFT, fill=Y, expand=YES)
        self.go_mainmenu.pack(side=LEFT, fill=Y, expand=YES)

        self.end_options.pack(side=TOP, fill=Y, expand=YES)

