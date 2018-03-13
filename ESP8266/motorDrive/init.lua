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


print("Setting up WiFi access point...")
wifi.setmode(wifi.SOFTAP)
--wifi.sta.config("test", "sajeta10")
--wifi.sta.connect() -- not necessary becau

cfg={}
cfg.ssid="nodeMCU"
--cfg.pwd=""

wifi.ap.config(cfg)

print("Waiting 3 seconds.")
tmr.alarm(1, 3000, 1, function()
    if wifi.ap.getip() == nil then
        print("Waiting for IP address...")
    else
        tmr.stop(1)

        print("WiFi station established: ")
        print("MAC addr: "..wifi.ap.getmac())
        ip, nm, gw = wifi.ap.getip()
        print("IP: "..ip)
        print("netmask: "..nm)
        print("gateway: "..gw)
        print("\nCekam 3 sekund...")
        
        tmr.alarm(0, 3000, 0, startup)
    end
end)
