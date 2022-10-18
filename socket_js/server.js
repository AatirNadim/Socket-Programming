const net = require('net')

const server = net.createServer((socket) => {
    socket.end(`this is the end command, time --> ${Date.now()}`)
})
server.listen(3400)