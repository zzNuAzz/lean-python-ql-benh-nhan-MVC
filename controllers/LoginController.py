from controllers.BaseController import BaseController

class LoginController(BaseController):
    def login(self, username, password):
        ten = 'sv'
        mssv = 'mssv'
        return username == ten and password == mssv