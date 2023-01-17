# 튜플 1

my_list = ['오예스', '몽쉘']
my_list.append('초코파이')
my_list = ['오예스', '몽쉘', '초코파이']  # 리스트 

my_tuple = ('오예스', '몽쉘')
#my_tuple.append('초코파이')
#my_tuple.remove('오예스')  # 튜플

my_tuple = ('오예스', '몽쉘', '초코파이', '초코파이')  # 중복 허용 
your_tuple = (1, 2, 3.14, True, False, '아무거나')  # 뭐든지 다 넣을 수 있음 


my_tuple = ('오예스', '몽쉘', '초코파이')  # 순서 보장!!

print(my_tuple[0])  # 인덱스

print(my_tuple[0:2])  # 슬라이싱

print('몽쉘' in my_tuple)  # 튜플에 포함되어 있는지 

print(len(my_tuple))  # 총 몇개?

# 튜플 : 읽기 전용 리스트 

#리스트 = [값1, 값2, 값3...]
#튜플 = (값1, 값2, 값3...)

#리스트 : 수정 가능, 튜플 : 수정 불가능


