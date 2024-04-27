from http.server import HTTPServer, BaseHTTPRequestHandler
# import project1.read as read
import read
import add
import requests

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        url = add.modify_url(read.filtered_url(read.freedom()))
        # if not self.check_image(url):
        #     url = url.replace('.jpg', '.png')
        output = f"""
        <html>
            <head>
                <style>
                    img {{
                        width: 100%;
                        height: auto;
                    }}
                </style>
                <script>
                    function handleError(img) {{
                        img.onerror = null;
                        img.src = img.src.replace('.jpg', '.png');
                    }}
                </script>
            </head>
            <body>
                <img src="{url}" alt="Image">
            </body>
        </html>
        """
        self.wfile.write(output.encode())
    # def check_image(self, url):
    #     response = requests.get(url)
    #     return response.status_code == 200
# 设置服务器地址和端口
server_address = ('', 8000)

# 创建服务器对象
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

# 启动服务器
httpd.serve_forever()
