## 哈希算法

摘要算法。MD5、SHA、HMAC 等。

### MD5

全称 MD5 消息摘要算法，是最常见的摘要算法之一。

* 单项加密、不能解 密、不可逆；
* 密文长度固定；

* 密文32位16进制数据，128位16字节

确认算法，调用网站加密函数，模拟加密，判断是否是标准算法，有没有改动。

```javascript
npm install crypto-js
```

```javascript
const crypto = require('crypto-js')

function md5_encrypt(str) {
  return crypto.MD5(str).toString()
}
```

```python
import hashlib

def md5_encrypt(text):
  md5 = hashlib.md5()
  md5.update(text.encode('utf-8'))
  return md5.hexdigest()
```

[汽车之家](https://www.autohome.com.cn/beijing/) 登录

### SHA

全称安全哈希算法，由美国国家安全局（NSA）所设计，主要适用于数组签名标准里面定义的数字签名算法。
SHA通常指 SHA 家族的五个算法，分别是 SHA-1、SHA-224、SHA-256、SHA-384、SHA-512。
SHA是比MD5更安全的一种算法，它对原始输入数据进行了更复杂的处理，使得输入数据被更好地保护。

MD5的密文是32位，SHA-1的密文是40位，SHA-256的密文是64位。不过密文越长，计算速度越慢。

```javascript
function sha1_encrypt(str) {
  return crypto.SHA1(str).toString()
}
```

```python
def sha1_encrypt(text):
  sha1 = hashlib.sha1()
  sha1.update(text.encode('utf-8'))
  return sha1.hexdigest()
```

sha1 40位, sha224 56位，sha256 64位，sha384 96位，sha512 128位。

都是 8 的倍数。

### HMAC

HMAC全称散列消息认证码、密钥相关的哈希运算消息认证码。HMAC加密算法是一种安全的基于加密 Hash 函数和共享密钥的消息认证协议，它要求通信双方共享密钥 key、约定算法、对报文进行 Hash 运算，形成固定长度的认证码。

存在 key 文件。

```javascript
function hmac_encrypt(str, key) {
  // return crypto.HmacMD5(str, key).toString()
  // return crypto.HmacSHA1(str, key).toString()
  return crypto.HmacSHA256(str, key).toString()
}
```

```python
def hmac_encrypt(text, key):
  # content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.md5)
  # content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.sha1)
  content = hmac.new(key.encode('utf-8'), text.encode('utf-8'), hashlib.sha256)
  return content.hexdigest()
```

如果是 hmac 加密，需要 key 文件。key 文件可能是在页面写死，或者由后端某个接口返回。

## 对称加密

## 非对称

## 国密 SM
