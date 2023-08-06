import http.server
import socketserver

# 设置服务器端口
PORT = 8502

# 创建一个简单的Web服务器
Handler = http.server.SimpleHTTPRequestHandler

# 指定服务器地址和端口
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Server running at http://localhost:{PORT}/")
    httpd.serve_forever()