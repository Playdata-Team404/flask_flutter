from flask import Flask, jsonify, request,json

from dto import UserDTO
import werkzeug
from dao import user_dao
import food_model_1


application = Flask(__name__)

@application.route('/foodselect', methods = ['POST','GET'])
def foodselect():
    if(request.method == 'POST'):
        fid = ''
        imagefile = ''
        result = ''
        food = []
        filename =''
        ans = ''
        imagefile = request.files['image']
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        imagefile.save('./photos/' + filename)
        fid = food_model_1.image_data(filename)
        print('아이디입니다',fid,'==='*50)

    # 음식 분류 후
        # print(filename)
    # fid = 'F10'
        result = user_dao.food_select(fid)

        food = list(map(str,result[2:]))
        food.insert(0,result[1])
        ans = ','.join(food)
        print('전송데이터',ans)

        return jsonify({'data':ans})
    # else:
    #     return json.dumps('')
        # return jsonify({
        #     'fid' : result[0],'fname' : result[1],'famount' : result[2],'fcal' : result[3],
        #     'fcarboh' : result[4],'fprotein' : result[5],'ffat' : result[6]
        #     })


@application.route('/signup', methods = ['POST'])
def signup_page():
    if(request.method == 'POST'):
        user_data = request.get_json()
        print(user_data, type(user_data))

        data = UserDTO(user_data['UUID'],user_data['UPW'],int(user_data['UAGE']),\
                    user_data['USEX'],float(user_data['UHEIGHT']),float(user_data['UWEIGHT']),\
                    user_data['UACT'],float(user_data['URDC']))

    msg = user_dao.user_insert(data)
    print(msg)
    if msg:
        return jsonify(result= "id :" +request.form.get("id") 
        +"회원가입 완료. 로그인 페이지로 이동합니다.")
    else:
        return ""



if __name__ == "__main__":
    application.run(debug=True, port=4000)