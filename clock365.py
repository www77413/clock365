import time
import tkinter as tk

def countdown(count):
    # 显示倒计时的函数
    label['text'] = count

    if count > 0:
        # 继续倒计时
        root.after(1000, countdown, count-1)
    else:
        # 倒计时结束，发出提示音
        label['text'] = "Time's up!"
        root.bell()

# 创建窗口和标签
root = tk.Tk()
label = tk.Label(root, font=('Helvetica', 80))

# 启动倒计时
countdown(25*60)  # 25分钟

# 显示标签
label.pack(expand=True)

# 运行窗口
root.mainloop()
