from controllers import BenhNhanController
import views

class LuuThongTin(views.BaseView):
    def __init__(self):
        self.benhNhanController = BenhNhanController()

    def render(self):
        super().render()
        self.benhNhanController.save_data()

        print("Lưu thông tin thành cong:\n")

        self.press_any_key()
        return views.Menu()