ma = 6
mb = 1

maa = 5
mbb = 2

function receive1(sock, data)
	if data ~= nil then
		print(data)
		predznak = string.sub(data,1,1)
		broj = math.abs(tonumber(data))

		if predznak=="-" then
			pwm.setduty(maa, broj-1)
			gpio.write(mbb,gpio.LOW)
		else
			pwm.setduty(maa, 1023-broj)
			gpio.write(mbb,gpio.HIGH)
		end

		print("clock: "..pwm.getclock(maa))
		print("duty: ".. pwm.getduty(maa))
		print("predznak: ".. gpio.read(mbb))
	end
end

function receive(sock,data)
	b1 = tonumber(string.match(data,"^(.+) "))
	b2 = tonumber(string.match(data," (.+)$"))
	gpio.mode(b1, gpio.OUTPUT)
	gpio.write(b1, b2)
	--broj = math.abs(tonumber(data))
end

server=net.createServer(net.TCP, 30)

server:listen(6666, function(conn)
	print(conn:getpeer())
	conn:on("receive", receive1)
end)


--Pocetni shit
gpio.write(1, gpio.HIGH)

pwm.setup(maa,50,1023)
pwm.start(maa)


gpio.mode(mbb, gpio.OUTPUT)
gpio.write(mbb, gpio.HIGH)
gpio.write(0, gpio.LOW)
--print("da")