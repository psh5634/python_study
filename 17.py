# 리스트 2

my_list = ['오예스', '몽쉘', '초코파이']  # 순서 보장!!
your_list = ['빅파이', '오뜨']

print(my_list[0])  # 인덱스

print(my_list[0:2])  # 슬라이싱

print('몽쉘' in my_list)  # 리스트에 포함되어 있는지

print(len(my_list))  # 총 몇개?

my_list[1] = '몽쉘카카오'
print(my_list)  # 값 수정

my_list.append('빅파이')
print(my_list)  # 값 추가

my_list.remove('오예스')
print(my_list)  # 값 삭제

my_list.extend(your_list)
print(my_list)  # 리스트 확장 