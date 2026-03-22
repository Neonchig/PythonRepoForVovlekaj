import subprocess, threading, time

def open_browser(link: str, *args):
    subprocess.run(["firefox-esr", link])

thread = threading.Thread(target=open_browser, kwargs={"link":""})
thread.start()

while True:
    print("test")
    time.sleep(2)