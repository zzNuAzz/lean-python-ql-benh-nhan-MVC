from controllers import BenhNhanController
import views

class TimKiemThongTin(views.BaseView):
    def __init__(self):
        self.benhNhanController = BenhNhanController()

    def render(self):
        super().render()

        search = input("Nhập thông tin tìm kiếm: ")

        listBenhNhan = self.benhNhanController.search(search)

        if len(listBenhNhan) > 0:
            for benhNhan in listBenhNhan:
                self.render_benh_nhan(benhNhan)
        else:
            print("Không tìm thấy thông tin")

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