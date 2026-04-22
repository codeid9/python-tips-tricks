import speedtest

speed = speedtest.Speedtest()
print(f"Download :{speed.download()/8000000:.2f}mb")
print(f"Upload :{speed.upload()/8000000:.2f}mb")

