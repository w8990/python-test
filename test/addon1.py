import time
import os
from mitmproxy import http
from datetime import datetime

# 日志文件路径
LOG_FILE = "api_log.txt"

# 将拦截到的API请求与响应写入日志文件
def log_to_file(data: str) -> None:
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(data + "\n")

# 拦截请求
def request(flow: http.HTTPFlow) -> None:
    # 记录请求开始的时间
    flow.metadata["start_time"] = datetime.now()

# 拦截响应
def response(flow: http.HTTPFlow) -> None:
    # 获取当前时间
    current_time = flow.metadata["start_time"].strftime("%Y-%m-%d %H:%M:%S")
    
    # 获取请求的 URL
    url = flow.request.pretty_url
    
    # 获取响应内容，确保是字符串格式
    response_content = flow.response.text if flow.response.content else ""

    # 记录日志：时间、URL、响应内容
    log_entry = f"{current_time}\n{url}\n{response_content}"
    log_to_file(log_entry)
    
    # 打印日志到控制台，便于调试
    print(f"URL: {flow.request.pretty_url}")
    print(f"发送: {flow.request.text}")
    # print(f"内容: {flow.response.text}")
    
    # 延时5秒后清除屏幕
    # time.sleep(5)
    # # 清除屏幕 (适用于不同的操作系统)
    # os.system('cls' if os.name == 'nt' else 'clear')
