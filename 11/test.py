class Player:
    type = 'Player'

    def __init__(self):
        self.x = 100
    def where(self): #self: 객체를 인자로 넘겨주는 역할
        print(self.x)

player = Player()
player.where()

# 클래스 변수 사용
print(Player.type)

# 클래스 함수 호출
#Player.where() #error
Player.where(player) #Player.where(player) == player.where()이다.

















#
# class Star: #싱글톤 : 객체를 한번만 찍어내는 용도 - global 변수처럼 access 가능
#     type = 'Star'
#     x = 100
#
#     def change():
#         x = 200
#         print('x is ', x)
# print('x IS ', Star.x)
# Star.change()
# print('x IS ', Star.x)
#
# star = Star()
# print('x IS ', star.x) #클래스 변수는 객체 변수처럼 access 가능
# star.change() #클래스 함수는 객체 함수처럼 access 불가