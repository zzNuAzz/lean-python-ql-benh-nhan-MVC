import views

class Menu(views.BaseView):
    def __init__(self):
        pass

    def render(self):
        super().render()
        print("Chức năng:")
        print("\t1. Nhập thông tin")
        print("\t2. Xuất thông tin")
        print("\t3. Tìm kiếm thông tin")
        print("\t4. Xóa thông tin")
        print("\t5. Lưu thông tin")
        print("\t0. Thoát chương trình")
        
        func = input("Nhập chức năng: ")
        match func:
            case "1": 
                return views.NhapThongTin()
            case "2": 
                return views.XuatThongTin()
            case "3": 
                return views.TimKiemThongTin()
            case "4": 
                return views.XoaThongTin()            
            case "5": 
                return views.LuuThongTin()
            case "0":
                exit()
            case _:
                print("Please input correct :3")
        
        self.press_any_key()
        return self