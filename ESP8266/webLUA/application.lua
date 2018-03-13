print("da")

function send(sock,f)
	data = f:read(1024)
	if data ~= nil then
		sock:send(data, function(sock) send(sock,f) end)
	else
		sock:close()
		print("Zatvaram konekciju")
	end
end

function receive(sock,data)
	path = string.match(data, 'GET (.-) ')
	print("received: \n"..data)

	if path=="/" then
		loc = "www/index.html"
	else
		loc = "www"..path
	end

	f = file.open(loc, "r")
	if f ~= nil then
		sock:send("HTTP/1.1 200 OK\r\n", function(sock) print("poslano") send(sock,f) end)
	else
		sock:send("HTTP/1.1 404 Not Found\r\n", function(sock) print("nema fajla") sock:close() end)
	end
end

server=net.createServer(net.TCP, 80)

server:listen(80, function(conn)
	print(conn:getpeer())
	conn:on("receive", receive)
end)