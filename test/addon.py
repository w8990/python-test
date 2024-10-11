from mitmproxy import http

# 处理请求函数
def request(flow: http.HTTPFlow) -> None:
    # 检查 URL 是否是你要拦截的那个
    target_url = "https://dev-01.blcloud.jp/bizcmn/api/v1/pmpartssearchreq/all/async/"
    
    # 如果请求的 URL 匹配
    if flow.request.pretty_url.startswith(target_url):
        print(f"拦截到请求: {flow.request.pretty_url}")
        
        # 这里你可以修改请求内容，如修改请求头或请求参数
        # 例如：修改User-Agent
        flow.request.headers["User-Agent"] = "CustomUserAgent"
        
        # 你也可以修改其他内容，视需求而定
        # flow.request.query["p"] = "2"  # 改变分页参数为2

# 处理响应函数
def response(flow: http.HTTPFlow) -> None:
    target_url = "https://dev-01.blcloud.jp/bizcmn/api/v1/pmpartssearchreq/all/async/"
    
    # 如果响应的 URL 匹配
    if flow.request.pretty_url.startswith(target_url):
        print(f"拦截到响应，状态码: {flow.response.status_code}")
        
        # 修改响应内容
        # 比如：将响应内容改为 "已修改的响应内容"
        flow.response.status_code = 400
