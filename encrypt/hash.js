const crypto = require('crypto-js')

function md5_encrypt(str) {
  return crypto.MD5(str).toString()
}

function sha1_encrypt(str) {
  return crypto.SHA1(str).toString()
}

function hmac_encrypt(str, key) {
  // return crypto.HmacMD5(str, key).toString()
  // return crypto.HmacSHA1(str, key).toString()
  return crypto.HmacSHA256(str, key).toString()
}

console.log(md5_encrypt('hello'))
console.log(sha1_encrypt('hello'))
console.log(hmac_encrypt('hello', '123456'))
