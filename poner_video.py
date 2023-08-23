import time
import webbrowser

total_breaks = 1
break_count = 0

while(break_count < total_breaks):
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=LMI_m7WxRZ0")
    break_count = break_count + 1