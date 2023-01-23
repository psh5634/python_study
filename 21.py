# 세트 2  

#리스트 
my_list = ['오예스', '몽쉘', '초코파이']
print(my_list[0])  # 인덱스를 통해서 첫 번째 값을 얻을 수 있음
my_list[0] = '빅파이'  # 첫 번째 인덱스 해당하는 값을 직접 바꿀 수 있음 

#튜플 
my_tuple = ('오예스', '몽쉘', '초코파이')
print(my_tuple[0])  # 인덱스를 통해서 첫 번째 값을 얻을 수 있음 
#my_tuple[0] = '빅파이'  -->  수정 불가

#세트 
my_set = {'오예스', '몽쉘', '초코파이'}
#print(my_set[0])  -->  접근 불가 (순서가 보장되어 있지 않기 때문에)
#my_set[0] = '빅파이'  -->  수정 불가  


my_set = {'돈까스', '보쌈', '제육덮밥'}

my_set.add('닭갈비')
print(my_set)  # 값 추가

my_set.remove('제육덮밥')
print(my_set)  # 값 삭제 

my_set.clear()  
print(my_set)  # 모든 값 삭제

del my_set   
print(my_set)  # 완전 삭제  -->  mt_set이라는 세트 자체를 완전 삭제해버림 

#리스트 : 수정 가능, 튜플 : 수정 불가능, 세트 : 수정 불가능 
