# 사원 정보를 보유하게 되는 구조의 클래스 
# 객체(복합 데이터)

class UserDTO:
    def __init__(self, UUID, UPW, UAGE,USEX,UHEIGHT,UWEIGHT,UACT,URDC):
        self.user_id = UUID
        self.user_pw = UPW
        self.user_age = UAGE
        self.user_sex = USEX
        self.user_height = UHEIGHT
        self.user_weight = UWEIGHT
        self.user_act = UACT
        self.user_rdc = URDC

    def get_uuid(self):
        return self.user_id
    
    def set_uuid(self, new_id):
        self.user_id = new_id

    def get_pw(self):
        return self.user_pw
    
    def set_pw(self, new_pw):
        self.user_pw = new_pw

    def get_age(self):
        return self.user_age
    
    def set_age(self, new_age):
        self.user_age = new_age

    def get_sex(self):
        return self.user_sex
    
    def set_sex(self, new_sex):
        self.user_sex = new_sex



    def get_height(self):
        return self.user_height
    
    def set_height(self, new_height):
        self.user_height = new_height

    def get_weight(self):
        return self.user_weight
    
    def set_weight(self, new_weight):
        self.user_weight = new_weight

    def get_act(self):
        return self.user_act
    
    def set_act(self, new_act):
        self.user_act = new_act

    def get_rdc(self):
        return self.user_rdc
    
    def set_rdc(self, new_rdc):
        self.user_rdc = new_rdc

    # def __str__(self):
    #     return 'id : ' + self.user_id + '- pw : ' + self.user_pw + '- 이름 : ' + self.user_name + '- email : ' + self.user_email


class menuDTO:
    def __init__(self, menuid, menuname, menuprice):
        self.menuid = menuid
        self.menuname = menuname
        self.menuprice = menuprice

    def getMenuid(self):
        return self.menuid
    
    def setMenuid(self, newmenuid):
        self.menuid = newmenuid

    def getMenuname(self):
        return self.menuname

    def setMenuname(self, newmenuname):
        self.menuname = newmenuname

    def getMenuprice(self):
        return self.menuprice

    def setMenuprice(self, newmenuprice):
        self.menuprice = newmenuprice


class orderDTO:
    def __init__(self, orderid, userid, menuid, orderquantity):
        self.orderid = orderid
        self.userid = userid
        self.menuid = menuid
        self.orderquantity = orderquantity

    def getOrderid(self):
        return self.orderid

    def setOrderid(self, neworderid):
        self.orderid = neworderid

    def getUserid(self):
        return self.orderid

    def setUserid(self, newuserid):
        self.userid = newuserid

    def getMenuid(self):
        return self.menuid

    def setMenuid(self, newmenuid):
        self.menuid = newmenuid

    def getOrderquantity(self):
        return self.orderquantity

    def setOrderquantity(self, neworderquantity):
        self.orderquantity = neworderquantity
