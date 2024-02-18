import hashlib
import hmac


def md5_encrypt(text):
  md5 = hashlib.md5()
  md5.update(text.encode('utf-8'))
  return md5.hexdigest()


def sha1_encrypt(text):
  sha1 = hashlib.sha1()
  sha1.update(text.encode('utf-8'))
  return sha1.hexdigest()


def hmac_encrypt(text, key):
  # content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.md5)
  # content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.sha1)
  content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.sha256)
  return content.hexdigest()


if __name__ == '__main__':
  text = 'hello'
  print(md5_encrypt(text))
  print(sha1_encrypt(text))
  print(hmac_encrypt('hello', '123456'))
