from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/greeting")
def greeting():
    return """
    <h1>안녕하세요</h1>
        <ul>
            <li>한식</li>
        </ul>
        """
    
@app.route("/index")
def index():
    return render_template('index.html')
    
@app.route("/lunch")
def lunch():
    menus = ["짜장면","투움바파스타","김치찜","굴국밥","만두라면"]
    pick  = random.choice(menus)
    return render_template('lunch.html',pick = pick, one_pick = pick)
    
@app.route("/lotto")    
def lotto():
   numbers = list(range(1,46))
   lotto = random.sample(numbers,6)
   lotto.sort()
   return render_template('lotto.html',lotto = lotto,one_lotto= lotto)
   
@app.route("/student/<string:name>")
def student(name):
    return render_template('student.html',name=name, one_name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    num = num**3
    return render_template("cube.html",num = num, cube_num = num)

@app.route("/naver")
def naver():
    return render_template("naver.html")

@app.route("/google")
def google():
    return render_template("google.html")
   
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')