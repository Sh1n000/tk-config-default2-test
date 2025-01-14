# from PySide6.QtWidgets import QApplication, QLabel, QWidget
# from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import Qt, QFile
# import sys

# from functools import partial

# class MyFirstUi(QMainWindow): # QMainWindow 를 상속받았습니다.
#     def __init__(self):
#         super().__init__() # QMainWindow 생성자를 실행하겠습니다.

#         ui_file_path = "/home/rapa/my_python/D8/my_first_ui.ui"
#         ui_file = QFile(ui_file_path)
#         loader = QUiLoader() # ui 파일에 있는 내용을 읽어 객체로 반환합니다.
#         self.ui = loader.load(ui_file)
#         self.ui.show()  
#         ui_file.close()  # 파일을 오픈하고나면 close해야한다 / 메모리 누수의 원인중 하나

#         self.ui.Push_Button_Click.clicked.connect(partial(self.on_button_click, "월요일")) # self.ui.옆에 이름같아야한다
#         # self.ui.Push_Button_Click.clicked.connect(lambda : self.on_button_click("월요일")) # 람다보다는 위에 버전 사용 추천!!!

#         self.ui.lineEdit_input.textChanged.connect(self.on_changed_text) # SIGNAL EVENT

#     def on_changed_text (self):
#         text = self.ui.lineEdit_input.text()
#         print (text)

#     def on_button_click(self, today):
#         print ("클릭 되었습니다~~")

#         self.ui.label_my_test.setText(f"{today}은 공부하기 너무 좋아요.")

#         input_text = self.ui.lineEdit_input.text()
#         print (input_text)



# app = QApplication()
# win = MyFirstUi()
# app.exec()



"""
회원가입 페이지

아이디와 비밀번호와 전화 번호와 이메일을 입력 받을수 있는
회원가입페이지의 폼을 만들어주시고
회원가입 버튼을 누르면 위 내용이 딕셔너리에 저장될 수 있도록 작성 부탁드립니다.
"""

# from PySide6.QtWidgets import QApplication, QLabel, QWidget
# from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtCore import Qt, QFile
# from PySide6.QtGui import QPixmap # QP ixmap 모듈 임포트
# import sys


# # from functools import partial

# class InMemberUi(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         ui_file_path = "/home/rapa/my_python/D8/inmember_ui.ui"
#         ui_file = QFile(ui_file_path)
#         loader = QUiLoader()
#         self.ui = loader.load(ui_file)
#         self.ui.show()
#         ui_file.close()
        
        
#         pixamp = QPixmap("/home/rapa/my_python/D8/Artorias.jpg") # 이미지 경로
#         scaled_pixamp = pixamp.scaled(400,250) # 이미지 리사이즈
#         self.ui.label_pic.setPixmap(scaled_pixamp) # 라벨에 이미지 넣기!
       
       
       
       
#         self.ui.Continue_pushButton.clicked.connect(self.on_button_click, "계속하기") # 이메일로그인 버튼을 눌렀을떄 이벤트 발생

#     def on_regist(self): # 인스턴스 매서드
#         """가입 버튼을 누르면 아이디, 비번이 저장되는 함수"""
#         id = self.ui.lineEdit_id.text()
#         ps = self.ui.lineEdit_password.text()
#         email = self.ui.lineEdit_email.text()

#         self.regist[id] = {
#             "패스워드" : ps,
#             "이메일"  : email
#         }
#         print (self, regist)


# app = QApplication()
# win = InMemberUi()
# app.exec()


from PySide6.QtWidgets import QApplication, QLabel, QWidget
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt, QFile
import sys

from functools import partial


class CalculationUi(QMainWindow): # QMainWindow 를 상속받았습니다.
    def __init__(self):
        super().__init__() # QMainWindow 생성자를 실행하겠습니다.

        ui_file_path = "/home/rapa/my_python/D8/calculation_ui.ui"
        loader = QUiLoader() # ui 파일에 있는 내용을 읽어 객체로 반환합니다.
        ui_file = QFile(ui_file_path)
        self.ui = loader.load(ui_file)
        self.ui.show()  
        ui_file.close()  # 파일을 오픈하고나면 close해야한다 / 메모리 누수의 원인중 하나
        
        self.susik = [] # 리스트 선언 --- 리스트와 Join을 사용해 계산을 하기위해



        self.ui.pushButton_0.clicked.connect(partial(self.one_button_click, "0"))
        self.ui.pushButton_1.clicked.connect(partial(self.one_button_click, "1"))
        self.ui.pushButton_2.clicked.connect(partial(self.one_button_click, "2"))
        self.ui.pushButton_3.clicked.connect(partial(self.one_button_click, "3"))
        self.ui.pushButton_4.clicked.connect(partial(self.one_button_click, "4"))
        self.ui.pushButton_5.clicked.connect(partial(self.one_button_click, "5"))
        self.ui.pushButton_6.clicked.connect(partial(self.one_button_click, "6"))
        self.ui.pushButton_7.clicked.connect(partial(self.one_button_click, "7"))
        self.ui.pushButton_8.clicked.connect(partial(self.one_button_click, "8"))
        self.ui.pushButton_9.clicked.connect(partial(self.one_button_click, "9"))

        self.ui.pushButton_plus.clicked.connect(partial(self.one_button_click, "+"))
        self.ui.pushButton_sub.clicked.connect(partial(self.one_button_click, "-"))
        self.ui.pushButton_mul.clicked.connect(partial(self.one_button_click, "*"))
        self.ui.pushButton_divi.clicked.connect(partial(self.one_button_click, "/"))

        # self.ui.pushButton_equal.clicked.connnect(partial(self.result_btn, "="))
        # "="는 결과 값 / C(Clear)는 초기화 / Backspace는 pop으로 리스트 오른쪽부터 제거
        self.ui.pushButton_C.clicked.connect(self.clear_btn)
        self.ui.pushButton_back.clicked.connect(self.back_spac)

    def one_button_click(self, btn):
        self.susik.append(btn) # 버튼으로 출력되는것을 리스트에 추가하는 함수
        # [ 1, 2, 3, 4, +, 5, 6, 7 ]에서 이제 1234+567로 바꾸는작업 Go!!!!!
        text = f"{''.join(self.susik)}"      # '구분자'.join(리스트)
        print(text) 
        self.ui.label_result.setText(text)

    # def result_btn(self,result):
    #     result = 



    def clear_btn(self):
        """초기화 함수"""
        del self.susik[:]
        text = f"{''.join(self.susik)}"
        self.ui.label_result.setText(text)

    def back_spac(self):
        self.susik.pop()
        text = f"{''.join(self.susik)}"
        self.ui.label_result.setText(text)





app = QApplication()
win = CalculationUi()
app.exec()