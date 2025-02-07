'''
This is the code of the product "File Upload Server" by alex.
这是Alex软件©系列中“文件上传服务器”的源码。

------------------------------
We will write in Chinese below.
------------------------------

请查看License.txt来查看条款，并查看README.md来查看使用方法。
'''

# add or change your username or password here in dict

UserPw={
'Alex':'youcannotguessthis',
'HelloWorld':'123'    
}

# add or change your username or password here in dict

from flask import Flask, request,  redirect, render_template,session
from flask import jsonify

import os

app = Flask(__name__)
 
app.secret_key='QWERTYUIOP'#对用户信息加密


@app.route('/login',methods=['GET',"POST"])#路由默认接收请求方式位POST，然而登录所需要请求都有，所以要特别声明。
def login():
     if request.method=='GET':
         return  render_template('login.html')
     user=request.form.get('user')
     pwd=request.form.get('pwd')
     if user in UserPw and UserPw[user]==pwd:#这里可以根据数据库里的用户和密码来判断，因为是最简单的登录界面，数据库学的不是很好，所有没用。
         session['user_info']=user
         return redirect('/index')
     else:
         return  '用户名或密码输入错误'

@app.route('/')
def index1():
     print(1)
     user_info=session.get('user_info')
     if not user_info:
         return redirect('/login')
     return redirect('/upload')

@app.route('/index')
def index2():
     print(1)
     user_info=session.get('user_info')
     if not user_info:
         return redirect('/login')
     return redirect('/upload')
 
 
 
@app.route('/logout')
def logout_():
     del session['user_info']
     return redirect('/login')
 
#upload:



FILE_DIR=os.path.abspath('.')


UPLOAD_FOLDER = FILE_DIR+'/uploads'  # 上传文件保存的目录

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload')

def indexx():
    print(2)
    user_info=session.get('user_info')
    if not user_info:
         return redirect('/login')
    return  render_template('upload.html')

@app.route('/upload', methods=['POST'])

def upload():
    print(3)
    user_info=session.get('user_info')
    if not user_info:
         return redirect('/login')
    file = request.files['file']

    if file:

        filename = file.filename

        file_path = app.config['UPLOAD_FOLDER']+"/"+session['user_info']
        if not os.path.exists(file_path):
             os.makedirs(file_path)
             print(f"创建路径：{file_path}")
        else:
             print(f"路径已存在：{file_path}")
        print(file_path)
        file_path = os.path.join(app.config['UPLOAD_FOLDER']+"/"+session['user_info'], filename)
        file.save(file_path)
        return '文件上传成功！'

@app.route('/progress', methods=['POST'])

def progress():

    uploaded_bytes = request.form['uploadedBytes']

    total_bytes = request.form['totalBytes']

    progress = int(uploaded_bytes) / int(total_bytes) * 100

    return jsonify(progress=progress)

#end.
 
if __name__ == "__main__":
     app.run(host='0.0.0.0')
