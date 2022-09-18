from controllers import BenhNhanController
import views

class NhapThongTin(views.BaseView):
    def __init__(self):
        self.benhNhanController = BenhNhanController()

    def render(self):
        super().render()
        print("\nNhập thông tin bênh nhân thêm mới:\n")

        hoTen = input("Nhập họ tên: ")
        namSinh = input("Nhập năm sinh: ")
        diaChi = input("Nhập địa chỉ: ")
        ngayXetNghiemF0 = input("Nhập ngày xét nghiệm F0: ")

        self.benhNhanController.create(hoTen, namSinh, diaChi, ngayXetNghiemF0)
        
        print("\nThêm mới thành công.")
        self.press_any_key()
        return views.Menu()