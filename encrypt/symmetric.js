const crypto = require('crypto-js')

const _key = '3WnPp4dz'
const _iv = '0DLDUxVt'

// CBC 加密模式, PKCS7 填充模式

const des_encrypt = text => {
  const key_hex = crypto.enc.Utf8.parse(_key)
  const encrypted = crypto.DES.encrypt(text, key_hex, {
    iv: crypto.enc.Utf8.parse(_iv),
    mode: crypto.mode.ECB,
    padding: crypto.pad.Pkcs7
  })
  return encrypted.toString()
}

const des_decrypt = text => {
  const key_hex = crypto.enc.Utf8.parse(_key)
  const decrypted = crypto.DES.decrypt(text, key_hex, {
    iv: crypto.enc.Utf8.parse(_iv),
    mode: crypto.mode.ECB,
    padding: crypto.pad.Pkcs7
  })
  return decrypted.toString(crypto.enc.Utf8)
}

const text = 'Hello, world!'
const encrypted = des_encrypt(text)
const decrypted = des_decrypt(encrypted)

console.log(text)
console.log(encrypted)
console.log(decrypted)
console.log(text === decrypted)
