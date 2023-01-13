# 문자열 포맷

python = '파이썬'
java = '자바'

print(python + ' ' + java)
print(python, java)  # 둘 다 출력 = 파이썬 자바 

print('개발 언어에는 ' + python + ', ' + java + ' 등이 있어요')
print('개발 언어에는', python, ',', java, '등이 있어요')  # 다른 문장 속에 넣기 

print('개발 언어에는 {}, {} 등이 있어요'. format(python, java))  # {} + format
print('개발 언어에는 {0}, {1} 등이 있어요'. format(python, java))  
print('개발 언어에는 {1}, {0} 등이 있어요'. format(python, java))  # {N} + format  # N:0,1,2...
print(f'개발 언어에는 {python}, {java} 등이 있어요')  # f-string {변수}

