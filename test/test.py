import tkinter as tk
from pynput import mouse, keyboard

# 初始圆环的半径和正三角形的边长
radius = 100
side_length = 200

# 创建一个透明背景的窗口
root = tk.Tk()
root.overrideredirect(True)  # 去除窗口边框
root.geometry(f"{2*radius}x{2*radius}+0+0")  # 设置窗口大小
root.wm_attributes("-topmost", True)  # 窗口置顶
root.wm_attributes("-transparentcolor", "white")  # 设置透明背景

# 创建一个画布并设置鼠标指针样式为小手
canvas = tk.Canvas(root, width=2*radius, height=2*radius, bg='white', highlightthickness=0)
canvas.pack()

# 标记当前形状，初始为圆环
current_shape = 'circle'

# 绘制圆环的函数
def draw_circle():
    canvas.delete("all")
    canvas.create_oval(10, 10, 2*radius-10, 2*radius-10, outline='red', width=1)

# 绘制正三角形的函数
def draw_triangle():
    canvas.delete("all")
    height = (3 ** 0.5 / 2) * side_length
    points = [
        radius, radius - height / 2,
        radius - side_length / 2, radius + height / 2,
        radius + side_length / 2, radius + height / 2
    ]
    canvas.create_polygon(points, outline='red', width=1, fill='white')

# 更新窗口位置和大小的函数
def update_window(x, y):
    root.geometry(f"{2*radius}x{2*radius}+{x-radius}+{y-radius}")
    canvas.config(width=2*radius, height=2*radius)

# 监听鼠标事件
def on_move(x, y):
    update_window(x, y)

mouse_listener = mouse.Listener(on_move=on_move)
mouse_listener.start()

# 切换形状和调整半径的函数
def on_press(key):
    global current_shape, radius, side_length
    try:
        if key == keyboard.Key.shift:
            if current_shape == 'circle':
                current_shape = 'triangle'
                draw_triangle()
            else:
                current_shape = 'circle'
                draw_circle()
        elif key.char == '+':
            radius += 2
            update_window(*mouse_controller.position)
            if current_shape == 'circle':
                draw_circle()
            else:
                draw_triangle()
        elif key.char == '-':
            radius = max(10, radius - 2)
            update_window(*mouse_controller.position)
            if current_shape == 'circle':
                draw_circle()
            else:
                draw_triangle()
    except AttributeError:
        pass

# 监听键盘事件
keyboard_listener = keyboard.Listener(on_press=on_press)
keyboard_listener.start()

# 设置鼠标指针为小手
def set_hand_cursor(event):
    root.config(cursor="hand2")

# 监听鼠标在画布上的移动事件并设置鼠标指针为小手
# canvas.bind("<Enter>", set_hand_cursor)

# 获取当前鼠标位置并设置窗口初始位置
mouse_controller = mouse.Controller()
x, y = mouse_controller.position
update_window(x, y)

# 初始绘制圆环
draw_circle()

# 运行窗口主循环
root.mainloop()
