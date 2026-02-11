const express = require('express')
const app = express()

app.get('/node', (req, res) => {
  res.send('Hello from Node App 🚀')
})

app.get('/', (req, res) => {
  res.send('Home Page');
});

app.get('/health', (req, res) => {
  res.send('OK')
})

app.listen(3000, '0.0.0.0', () => {
  console.log('Server running on port 3000')
})
