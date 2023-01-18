# 튜플 2

my_tuple = ('오예스', '몽쉘', '초코파이')  # 패킹

(pie1, pie2, pie3) = my_tuple  # 언패킹 
pie1 = '오예스'
pie2 = '몽쉘'
pie3 = '초코파이'

numbers = (1,2,3,4,5,6,7,8,9,10)
(one, two, *others) = numbers
(*others, nine, ten) = numbers
(one, *others, ten) = numbers  # 언패킹 

# *ohers = 리스트 형태 