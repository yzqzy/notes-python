const crypto = require('crypto-js')

function md5_encrypt(str) {
  return crypto.MD5(str).toString()
}

function sha1_encrypt(str) {
  return crypto.SHA1(str).toString()
}

console.log(md5_encrypt('hello'))
console.log(sha1_encrypt('hello'))
