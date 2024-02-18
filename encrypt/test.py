import hashlib


def md5_encrypt(text):
  md5 = hashlib.md5()
  md5.update(text.encode('utf-8'))
  return md5.hexdigest()


if __name__ == '__main__':
  text = 'hello'
  print(md5_encrypt(text))
