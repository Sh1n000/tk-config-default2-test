


# class Student:
    
#     index = 0 # 클래스 변수
#     # 클래스 변수는 클래스 전체에서 공유되는 변수입니다.
#     # 모든 인스턴스가 동일한 값을 참조합니다.
#     # 클래스 정의 부분에 선언되고, 특정 인스턴스가 아니라, 클래스 자체에 속합니다.
    
#     def __init__(self, name, age=None):  # 비공개로 처리하고 싶을때
#         """생성자"""

#         self.name = name
        
#         if age is None:
#             self.age = "비밀"
#         else:
#             self.age = age

#         Student.index +=1 # 클래스명.변수명 으로 클래스변수에 접근합니다.

#     def annyeonghaseyo(self):
#         """
#         나를 소개하는 메서드
#         2개의 인스턴스 변수를 사용해서
#         나를 소개하는 문자열을 표준출력하는 함수.
#         """

#         print (f"저는 {self.name}이고, 나이는 {self.age}입니다.")

# class Academy(Student): # Student 클래스를 상속받겠습니다.
#     def __init__(self, name, age=None): 
#         super().__init__(name, age)     # 부모 클래스의 생성자를 호출하겠습니다.

#         def annyeonghaseyo(self):
#             # super() .annyeonghaseyo()
#             print ("앞으로 잘부탁드립니다.")
# std1 = Academy("형민", 25)
# std2 = Academy("도은")
# std3 = Academy("준수", 28)

# print (Academy.index) # 클래스명.변수 or 객체명.변수로 클래스 변수에 접근할 수 있습니다.

# """
# 캐릭터라는 부모 클래스를 상속받습니다.
# 여러분은 Wizard, Warrior, Archer 등의 자식 클래스를 만들어서
# 부모 클래스가 가진 attack_damage 메서드에서 선언된 self.base_damage를 
# 각 작업에 맞는 공격력으로 구할수 있도록 메서드 오바라이드를 해주세요.
# 스크립트를 실행하면 3개의 객체를 만들고 반복문으로
# 캐릭터들의 attack_damge() 메서드를 실행할 수 있도록 해주시고, 
# damage가 캐릭터의 이름과 함꼐 프린트 되게 해주세요.

# 워리어 :
# 기본 공격 데미지 2배
# 10% 확률로 데미지 2배

# 마법사:
# 기본 공격 데미지 1.5배

# 아처:
# 50% 확률로 데미지 3배
# """

# import random

# class Character:
#     def __init__(self, name, damage):
#         self.name = name
#         self.base_damage = 10 # 기본공격
        
#     def attack_damage(self):
#         """
#         기본 공격 데미지
#         (자식 클래스에서 오바라이딩 필요)
#         """
#         return self.base_damage



# class Warrior(Character):
#     def attack_damage(self):
#         # 기본공격 데미지 2배
#         damage = self.base_damage*2
#         # 10% 확률로 2배
#         print (f"데미지:{damage}")
#         if random.random() < 0.1:
#             print (f"{self.name}의 크리티컬 데미지 : {damage}")

# class Wizard(Character):
#     def attack_damage(self):
#         # 기본공격 데미지 1.5배
#         damage = self.base_damage*1.5
#         print (f"데미지:{damage}")

# class Archer(Character):
#     def attack_damage(self):
#         damage = self.base_damage
#         # 50% 확률로 3배
#         print (f"데미지:{damage}")
#         if random.random() < 0.5:
#             print (f"{self.name}의 크리티컬 데미지 : {damage*3}")


class Circles

    pi = 3.141592

    def __init__(self):
        self.radius