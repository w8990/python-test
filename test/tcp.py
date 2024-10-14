import socket

def start_tcp_server(host='localhost', port=12345):
    # 创建 TCP 服务器套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 绑定到指定的地址和端口
    server_socket.bind((host, port))
    
    # 开始监听
    server_socket.listen(5)
    print(f"Listening for incoming connections on {host}:{port}...")

    while True:
        # 接受客户端连接
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr} has been established!")
        
        # 接收数据
        data = client_socket.recv(1024)  # 接收1024字节的数据
        if data:
            print("Received:", data.decode())  # 打印接收到的数据
            
            # 发送响应
            client_socket.send("Hello from server!".encode())
        
        # 关闭与客户端的连接
        client_socket.close()

if __name__ == "__main__":
    start_tcp_server()
