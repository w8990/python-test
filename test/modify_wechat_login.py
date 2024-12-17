from mitmproxy import http

# 设置要监听的目标IP地址
target_ip = "120.232.51.95"  # 替换为你要监听的IP地址

def request(flow: http.HTTPFlow) -> None:
    # 检查目标IP地址，过滤请求
    if flow.server_conn.address and flow.server_conn.address[0] == target_ip:
        print(f"Captured request to {target_ip}")
        print(f"URL: {flow.request.url}")
        print(f"Request Headers: {flow.request.headers}")
        print(f"Request Content: {flow.request.content.decode('utf-8', errors='ignore')}")

def response(flow: http.HTTPFlow) -> None:
    # 检查目标IP地址，过滤响应
    if flow.server_conn.address and flow.server_conn.address[0] == target_ip:
        print(f"Captured response from {target_ip}")
        print(f"Response Headers: {flow.response.headers}")
        print(f"Response Content: {flow.response.text}")
