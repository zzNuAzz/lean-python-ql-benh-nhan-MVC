from controllers import BenhNhanController
import views

class XoaThongTin(views.BaseView):
    def __init__(self):
        self.benhNhanController = BenhNhanController()

    def render(self):
        super().render()
        print("\Xóa thông tin:\n")

        stt = int(input("Nhập số thứ tự bệnh nhân: "))

        benhNhan = self.benhNhanController.get(stt)
        if benhNhan is None:
            print("Bệnh nhân không tồn tại")
        else:
            self.benhNhanController.delete(stt)
            print("Xóa thành công")

        self.press_any_key()
        return views.Menu()