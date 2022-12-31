# 문자열 포맷

python = '파이썬'
java = '자바'

print(python + ' ' + java)
print(python, java)

print('개발 언어에는 ' + python + ', ' + java + ' 등이 있어요')
print('개발 언어에는', python, ',', java, '등이 있어요')

print('개발 언어에는 {}, {} 등이 있어요'. format(python, java))
print('개발 언어에는 {0}, {1} 등이 있어요'. format(python, java))
print('개발 언어에는 {1}, {0} 등이 있어요'. format(python, java))
print(f'개발 언어에는 {python}, {java} 등이 있어요')

