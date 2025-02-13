import drills
from functools import partial
from tkinter import *

class NumeracyApp:
    def __init__(self):
        self.root = Tk()
        self.root.title('NumberBrain')
        self.root.geometry('640x480')
        self.root['background']='grey'
        self.current_menu = None

        # A dictionary of menus, name to frame
        self.menus = dict()

        self.menus['main'] = self.init_main()
        
        self.display_menu('main')
        self.root.mainloop()

    def display_menu(self, targmenu=None, clean=None):
        # First purge the previous menu from view
        if self.current_menu:
            self.menus[self.current_menu].grid_remove()
        
        if not clean:
            # Then onboard the target menu as desired
            self.menus[targmenu].grid()
            self.current_menu = targmenu

    def init_main(self):
        ret = Frame(self.root)
        
        # Drills menu items
        drills_menu = Frame(ret)
        drills_menu.grid(column=0, row=0)

        drills_header = Label(drills_menu, text='DRILLS', font=('Arial Bold', 30))
        drills_header.pack(side=TOP)

        timestable = Button(drills_menu, text='times tables', font=('Arial Bold', 20))
        timestable.pack(side=TOP)

        addition = Button(drills_menu, text='rapid addition', font=('Arial Bold', 20))
        addition.pack(side=TOP)

        zetamac = Button(drills_menu, text='zetamac vanilla', font=('Arial Bold', 20), command=partial(drills.Zetamac, self))
        zetamac.pack(side=TOP)

        # Analysis Menu items 
        analysis_menu = Frame(ret)
        analysis_menu.grid(column=1, row=0)

        analysis_header = Label(analysis_menu, text='ANALYSIS', font=('Arial Bold', 30))
        analysis_header.pack(side=TOP)

        return ret

if __name__=='__main__':
    NumeracyApp()
