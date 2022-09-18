import views
from controllers import LoginController

class Login(views.BaseView):
    MAX_RETRY = 5
    def __init__(self):
        self.loginController = LoginController()
        self.retry = 0

    def render(self):
        super().render()
        print("\nLogin\n")
        username = input("Nhập username: ")
        password = input("Nhập password: ")

        if self.login(username, password):
            return views.Menu()
        else:
            input("Bạn đã nhập sai {} lần. Mời bạn nhập lại".format(self.retry))
            if self.retry == Login.MAX_RETRY:
                input("Bạn đã nhập sai quá {} lần. Vui lòng liên hệ hỗ trợ 18001919".format(Login.MAX_RETRY))
                exit()
            else:
                return self

    def login(self, username, password):
        success = self.loginController.login(username, password)
        if success:
            self.retry = 0
        else:
            self.retry += 1
        return success