function startup()
    if file.open("init.lua") == nil then
        print("init.lua deleted or renamed")
    else
        print("Running")
        file.close("init.lua")
        -- the actual application is stored in 'application.lua'
        dofile("application.lua")

    end
end

--Pocetni shit
gpio.write(1, gpio.HIGH)


--print("Setting up WiFi access point...")
wifi.setmode(wifi.STATION)
wifi.sta.config("Novi Wifi", "4.sup.ina")
--wifi.sta.connect() -- not necessary becau

--cfg={}
--cfg.ssid="nodeMCU"
--cfg.pwd=""

--wifi.ap.config(cfg)

tmr.alarm(1, 3000, 1, function()
    if wifi.sta.getip() == nil then
        print("Waiting for IP address...")
    else
        wifi.sta.setip({ip = "192.168.2.40", netmask = "255.255.255.0", gateway = "192.168.2.1"})
        tmr.stop(1)

        print("WiFi connected: ")
        print("MAC addr: "..wifi.sta.getmac())
        ip, nm, gw = wifi.sta.getip()
        print("IP: "..ip)
        print("netmask: "..nm)
        print("gateway: "..gw)
        print("\nCekam 3 sekund...")
        
        tmr.alarm(0, 3000, 0, startup)
    end
end)
