from mitmproxy import http

# 定义目标 URL 和本地文件路径
target_js_url = "https://staging01.blcloud.jp/menu/main.7b80a02772e671545230.bundle.js"
local_file_path = r"C:\\Users\\x_wuht\\Desktop\\main.7b80a02772e671545230.bundle.js"

def response(flow: http.HTTPFlow) -> None:
    # 检查是否是目标 URL 的请求
    if flow.request.pretty_url == target_js_url:
        print(f"拦截到目标 URL 的响应: {target_js_url}")
        try:
            # 从本地文件读取内容
            with open(local_file_path, "rb") as f:
                local_js_content = f.read()
            
            # 替换响应的内容为本地文件内容
            flow.response.content = local_js_content
            print("成功替换响应内容为本地文件内容。")
        except Exception as e:
            print(f"替换内容时发生错误: {e}")