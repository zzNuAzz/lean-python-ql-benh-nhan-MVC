import os

class BaseView:
    # return a View to render next
    def render(self):
        self.clear()
        return self

    def clear(self):
        # posix is os name for linux or mac
        if(os.name == 'posix'):
            os.system('clear')
        # else screen will be cleared for windows (os.name = nt)
        else:
            os.system('cls')

    def press_any_key(self):
        input("Press any key to continue...")