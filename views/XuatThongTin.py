from controllers import BenhNhanController
import views

class XuatThongTin(views.BaseView):
    def __init__(self):
        self.benhNhanController = BenhNhanController()

    def render(self):
        super().render()
        print("\nXuât thông tin:\n")

        i = input("Nhập số lượng bệnh nhân: ")

        soLuong = self.benhNhanController.get_total()
        if i == "all" or int(i) <= soLuong:
            listBenhNhan =  self.benhNhanController.get_all() if i == "all" else self.benhNhanController.get_last(int(i))
            for benhNhan in listBenhNhan:
                self.render_benh_nhan(benhNhan)
        else:
            print('"')

        self.press_any_key()
        return views.Menu()

    def render_benh_nhan(self, benhNhan):
        print("\nMã bệnh nhân: {maBenhNhan}\n\tHọ tên: {hoTen}\n\tNăm sinh: {namSinh}\n\tĐịa chỉ: {diaChi}\n\tNgày xét nghiệm F0: {ngayXetNghiemF0}".format(
            maBenhNhan = benhNhan.maBenhNhan,
            hoTen = benhNhan.hoTen,
            namSinh = benhNhan.namSinh,
            diaChi = benhNhan.diaChi,
            ngayXetNghiemF0 = benhNhan.ngayXetNghiemF0,
        ))