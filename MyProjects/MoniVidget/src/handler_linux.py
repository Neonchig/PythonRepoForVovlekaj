import evdev

def handler():
    for i in evdev.list_devices():
        print(evdev.device.InputDevice.capabilities(evdev.InputDevice(i)))
                

handler()