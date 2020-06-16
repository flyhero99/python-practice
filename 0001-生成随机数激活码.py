# python练习题项目 --- 第0001题
# 做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？

# 使用random库的，或者使用uuid库

# 方法1 使用随机数，random类中的choice方法
# import string as s
# import random as r

# print(s.ascii_uppercase)
# def randNum():
# 	f = open('/Users/flyhero/Desktop/随机数激活码.txt', 'w+')
# 	for i in range(200):
# 		randomStr = ''.join(r.choice(s.ascii_uppercase + s.digits) for x in range(10)) + '\n'
# 		f.write(randomStr)
# 	f.close()

# if __name__ == '__main__':
# 	randNum()


# 方法2 使用uuid库
# import uuid as u

# def rand_uuid():
# 	f = open('/Users/flyhero/Desktop/UUID随机数激活码.txt', 'w+')
# 	for i in range(200):
# 		ID = str(u.uuid1()) + '\n'
# 		f.write(ID)

# 	f.close()

# if __name__ == '__main__':
# 	rand_uuid()


# 方法3 使用主键和随机码
import string as s
import random as r

def rand_ID():
	f = open('/Users/flyhero/Desktop/主键+随机码随机数激活码.txt', 'w+')

	for i in range(200):
		ID = id(i)
		rand_id = str(ID)[5:]
		null = ''
		for j in rand_id:
			null += j + r.choice(s.ascii_uppercase)

		f.write(null+'\n')
	f.close()

if __name__ == '__main__':
	rand_ID()