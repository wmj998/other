import hashlib

m = hashlib.md5()

m.update(b'123456')
print(m.hexdigest())
print(m.digest())

m = hashlib.md5()
a = '123456'
m.update(a.encode())
print(m.hexdigest())
print(m.digest())
