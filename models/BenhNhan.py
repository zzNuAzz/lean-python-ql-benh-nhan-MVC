import json
from models.BaseModel import BaseModel

class BenhNhanModel(BaseModel):
    list = []
    soThuTu = 0

    def __init__(self, hoTen, namSinh, diaChi, ngayXetNghiemF0, maBenhNhan = None, soThuTu = None):
        self.hoTen = hoTen
        self.namSinh = namSinh
        self.diaChi = diaChi
        self.ngayXetNghiemF0 = ngayXetNghiemF0
        self.maBenhNhan = maBenhNhan
        self.soThuTu = soThuTu
    
    def generateId(self):
        self.soThuTu = BenhNhanModel.soThuTu + 1

        x = self.soThuTu + 1
        y = self.hoTen[0:3]
        self.maBenhNhan = "{}{}".format(x,y)

    @staticmethod
    def create(hoTen, namSinh, diaChi, ngayXetNghiemF0):
        benhNhan = BenhNhanModel(hoTen, namSinh, diaChi, ngayXetNghiemF0)
        benhNhan.generateId()
        BenhNhanModel.list.append(benhNhan)

    @staticmethod
    def update(maBenhNhan, hoTen, namSinh, diaChi, ngayXetNghiemF0):
        pass

    @staticmethod
    def delete(soThuTu):
        BenhNhanModel.list = [x for x in BenhNhanModel.list if x.soThuTu != soThuTu]

    @staticmethod
    def get(soThuTu):
        return next((x for x in BenhNhanModel.list if x.soThuTu == soThuTu), None)

    @staticmethod
    def search(search):
        return [benhNhan for benhNhan in BenhNhanModel.list
            if benhNhan.maBenhNhan == search or
                benhNhan.hoTen == search or
                benhNhan.namSinh == search
            ]

    @staticmethod
    def get_last(n):
        return BenhNhanModel.list[-n:]
    
    def get_all():
        return BenhNhanModel.list

    @staticmethod
    def get_total():
        return len(BenhNhanModel.list)

    @staticmethod
    def save_data():
        with open(r'dataBenhNhan.txt', 'w+') as fp:
            json.dump({
                'list': [ob.toDict() for ob in BenhNhanModel.list],
                'soThuTu': BenhNhanModel.soThuTu
            }, fp, sort_keys=True, indent=4)

    @staticmethod
    def load_data():
        try:
            with open(r'dataBenhNhan.txt', 'r') as fp:
                data = json.load(fp)
                BenhNhanModel.soThuTu = int(data['soThuTu'])
                BenhNhanModel.list = [BenhNhanModel(
                    hoTen = str(x['hoTen']),
                    namSinh = str(x['namSinh']) , 
                    diaChi = str(x['diaChi']),
                    ngayXetNghiemF0 = str(x['ngayXetNghiemF0']),
                    maBenhNhan = str(x['maBenhNhan']),
                    soThuTu = str(x['soThuTu'])
                ) for x in list(data['list'])]
        except :
            pass
        

BenhNhanModel.load_data()