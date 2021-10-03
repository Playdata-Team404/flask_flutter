import cx_Oracle
import pandas as pd
from dto import UserDTO

class user_dao:

    # 회원가입 로직
    def user_insert(dto1):
        try:
            conn=cx_Oracle.connect(user="TEAM404", password="1234", dsn="xe")
            cur=conn.cursor()
            try:
                print(dto1)
                cur.execute("insert into USERS values (:UUID, :UPW, :UAGE, :USEX, :UHEIGHT, :UWEIGHT, :UACT, :URDC )",\
                            UUID=dto1.get_uuid(), UPW=dto1.get_pw(),\
                            UAGE=dto1.get_age(), USEX=dto1.get_sex(),\
                            UHEIGHT=dto1.get_height(), UWEIGHT=dto1.get_weight(),\
                            UACT=dto1.get_act(), URDC=dto1.get_rdc())
                conn.commit()
                cur.close()
                conn.close()
                return "회원가입 완료"
            except Exception as error:
                cur.close()
                conn.close()
                return error
        except Exception as error:
            cur.close()
            conn.close()
            return "오류2"

    def food_insert(food,food_counts):
        try:
            conn=cx_Oracle.connect(user="TEAM404", password="1234", dsn="xe")
            cur = conn.cursor()
            try:
                for i in range(food_counts):
                    cur.execute("insert into food values (:fid, :fname, :famount, :fcal, :fcarboh, :fprotein, :ffat)",\
                             fid=food['FID'][i],fname=food['FNAME'][i],famount=food['FAMOUNT'][i],
                             fcal=food['FCAL'][i],fcarboh=food['FCARBOH'][i],fprotein=food['FPROTEIN'][i],
                             ffat=food['FFAT'][i])
                conn.commit()
                cur.close()
                conn.close()
                return "성공"
            except Exception as error:
                cur.close()
                conn.close()
                return error
        except Exception as error:
            cur.close()
            conn.close()
            return error

    def food_select(food_id):
        try:
            conn=cx_Oracle.connect(user="TEAM404", password="1234", dsn="xe")
            cur = conn.cursor()
            try:
                cur.execute("select * from food where FID = :fid", fid=food_id)
                row = cur.fetchone()
                print(row)
                return row
            except Exception as error:
                print(error)
                return ''
        finally:
            cur.close()
            conn.close()
            





    # 로그인 로직
    def userone(self, user_id):
        data=""
        try:
            conn=cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
            cur=conn.cursor()

            try:
                cur.execute("select * from user_t where user_id=:v", v=user_id)
                row=cur.fetchone()
                data='{"id":"' + row[0] + '", "pw":' + str(row[1]) + '}'
            except Exception as error:
                print(error)
        finally:
            cur.close()
            conn.close()

        return data

if __name__ == "__main__":
    # user_data = {'UUID': '1234@123.com', 'UPW': '987654', 'USEX': '남', 'UAGE': '30', 'UHEIGHT': '180', 'UWEIGHT': '90', 'UACT': '주로 좌식 생활', 'URDC': '2405'}
    
    # data = UserDTO(user_data['UUID'],user_data['UPW'],int(user_data['UAGE']),\
    #                 user_data['USEX'],float(user_data['UHEIGHT']),float(user_data['UWEIGHT']),\
    #                 user_data['UACT'],float(user_data['URDC']))

    # msg = user_dao.user_insert(data)
    # print(msg)

    # xlsx = pd.read_csv('foodtable1.csv',encoding='cp949')
    # len(xlsx)
    # menus = xlsx.to_dict('list')
    # print(menus,len(xlsx))
    # print(user_dao.food_insert(menus,len(xlsx)))


    print(user_dao.food_select('F10'))

    # def userSearch(self, userid):
    #     try:
    #         conn=cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
    #         cur=conn.cursor()
    #         try:
    #             cur.execute(
    #                 "select userid, username, useremail from user where userid=:userid", userid=userid)
    #         except Exception as error:
    #             print(error)
    #     except Exception as error:
    #         print(error)
    #     finally:
    #         cur.close()
    #         conn.close()
    #     return '{userid":' + str(cur.fetchone()[1]) + ', "username":' + str(cur.fetchone()[2]) + ', "useremail":' + str(cur.fetchone()[3]) + '}'

    # def userUpdate(self, dto):
    #         try:
    #             conn=cx_Oracle.connect(
    #                 user="SCOTT", password="TIGER", dsn="xe")
    #             cur=conn.cursor()
    #             try:
    #                 cur.execute("update user set userid=:userid, username=:username, useremail=:useremail, userpassword=:userpassword", userid=dto.getUserid(
    #                 ), username=dto.getUsername(), useremail=dto.getUseremail(), userpassword=dto.getUserpassword())
    #                 conn.commit()
    #             except Exception as error:
    #                 print(error)
    #         except Exception as error:
    #             print(error)
    #         finally:
    #             cur.close()
    #             conn.close()

    # def userDelete(self, userid):
    #         try:
    #             conn=cx_Oracle.connect(
    #                 user="SCOTT", password="TIGER", dsn="xe")
    #             cur=conn.cursor()
    #             try:
    #                 cur.execute(
    #                     "delete from user where userid=:userid", userid=userid)
    #                 conn.commit()
    #             except Exception as error:
    #                 print(error)
    #         except Exception as error:
    #             print(error)
    #         finally:
    #             cur.close()
    #             conn.close()
