import socket

def start_tcp_client(host='localhost', port=12345):
    # 创建 TCP 客户端套接字
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 连接到服务器
    client_socket.connect((host, port))
    
    # 发送数据
    client_socket.send("Hello,123".encode())
    
    # 接收服务器响应
    response = client_socket.recv(1024)
    print("Received from server:", response.decode())
    
    # 关闭连接
    client_socket.close()

if __name__ == "__main__":
    start_tcp_client()
