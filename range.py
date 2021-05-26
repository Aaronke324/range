#range 範圍，python內建功能:清單產生器

range(5) #[0, 1, 2, 3, 4]  結尾不包含該數字
range(3) #[0, 1, 2]

range(2, 5) #[2, 3, 4]
range(8, 10) #[8, 9] 
range(2, 10, 3) #[2, 5, 8] 第三個數值為階梯(遞增/可為正或負)數
range(3, 8 ,2) #[3, 5, 7]
range(10, 3, -2) #[10, 8, 6, 4]


import random

for i in range(100):
	r = random.randint(1, 1000)
	print('這是第', i + 1, '次產生的隨機變數:', r)

# range practice
for i in range(100):
    print('這是第', i + 1, '次說hi')