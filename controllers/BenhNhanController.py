from models.BenhNhan import BenhNhanModel
from controllers.BaseController import BaseController

class BenhNhanController(BaseController):
    def __init__(self):
        super().__init__()

    def create(self, hoTen, namSinh, diaChi, ngayXetNghiemF0):
        BenhNhanModel.create(hoTen, namSinh, diaChi, ngayXetNghiemF0)

    def search(self, search):
        return BenhNhanModel.search(search)

    def get(self, soThuTu):
        return BenhNhanModel.get(soThuTu)

    def get_total(self):
        return BenhNhanModel.get_total()

    def get_all(self):
        return BenhNhanModel.get_all()

    def get_last(self, n):
        return BenhNhanModel.get_last(n)

    def delete(self, soThuTu):
        return BenhNhanModel.delete(soThuTu)

    def save_data(self):
        return BenhNhanModel.save_data()
