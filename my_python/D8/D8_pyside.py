


# # Pyside6

# from PySide6.QtWidgets import QApplication, QLabel, QWidget, QPushButton, QVBoxLayout

# app = QApplication()
# # Pyside6 어플리케이션에서 가장 중요한 중앙관리 객체 입니다.
# # 이 객체는 이벤트 루프를 관리합니다. (사용자의 입력, 키보드 입력, 마우스 클릭 등)
# # 위젯(윈도우)을 표시하고 렌더링하는데 필요한 환경을 초기화합니다.
# # 프로그램 실행부터 종료까지의 흐름을 관리합니다.
# # QApplication 객체는 프로그램이 실행되기 전에 반드시 생성되어야합니다.

# def on_button_click():
#     print("클릭~~")
#     label.setText("도움!! 도움!!! 살려사람")



# window = QWidget() # QWidget이라고 하는 Pyside 컴퍼넌트를 이용해서 윈도우를 구성
# layout = QVBoxLayout() # 윈도우안에 수직 격자 형태의 레이아웃을 생성

# label = QLabel("Hello, World!") # 텍스트를 표현하는 위젯입니다.

# button = QPushButton("Click Me") # 버튼에 라벨 추가
# button.clicked.connect(on_button_click)

# layout.addWidget(label)
# layout.addWidget(button)

# window.setLayout(layout)
# window.setMinimumHeight(300)
# window.setMinimumWidth(300)
# window.show()
# app.exec()