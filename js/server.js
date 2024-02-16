const express = require('express')
const app = express()
const port = 3000

// 编码 btoa Buffer.from().toString('base64')
// 解码 atob Buffer.from(str, 'base64').toString()

app.get('/', (req, res) => {
  res.send('Hello World!')
})
app.get('/api', (req, res) => {
  res.send('API response')
})

app.listen(port, () => {
  console.log(`Server running on port ${port}`)
})
