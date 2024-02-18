## 哈希算法

摘要算法。MD5、SHA、HMAC 等。

### MD5

全称 MD5 消息摘要算法，是最常见的摘要算法之一。

* 单项加密、不能解密、不可逆；
* 密文长度固定；

* 密文32位16进制数据，128位16字节

确认算法，调用网站加密函数，模拟加密，判断是否是标准算法，有没有改动。

```javascript
npm install crypto-js
```

```javascript
const crypto = require('crypto-js');

const message = 'hello world';
const hash = crypto.MD5(message).toString();
```

```python
```

```python
```

[汽车之家](https://www.autohome.com.cn/beijing/) 登录

### SHA

全称安全哈希算法，由美国国家安全局（NSA）所设计，主要适用于数组签名标准里面定义的数字签名算法。
SHA通常指 SHA 家族的五个算法，分别是 SHA-1、SHA-224、SHA-256、SHA-384、SHA-512。
SHA是比MD5更安全的一种算法，它对原始输入数据进行了更复杂的处理，使得输入数据被更好地保护。

MD5的密文是32位，SHA-1的密文是40位，SHA-256的密文是64位。不过密文越长，计算速度越慢。

```javascript
```

```python
```

## 对称加密

## 非对称

## 国密 SM
