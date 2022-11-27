from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = "localhost"  # 127.0.0.1
server_port = 8080


class MyServer(BaseHTTPRequestHandler):
    books = ["Pan Tadeusz", "Krzyżacy"]

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text\html")
        self.end_headers()

        self.wfile.write(bytes('<html>', "utf-8"))
        self.wfile.write(bytes('<head><title>Books</title><meta charset="UTF-8"></head>', "utf-8"))
        self.wfile.write(bytes('<body>', "utf-8"))
        self.wfile.write(bytes(f"<p>Request: {self.path}</p>", "utf-8"))

        if str(self.path) == "/books/":
            self.wfile.write(bytes(f"<p>{self.books_list()}</p>", "utf-8"))

        self.wfile.write(bytes('</body>', "utf-8"))
        self.wfile.write(bytes('</html>', "utf-8"))

        # self.wfile.write(bytes(f'''
        #     <html>
        #     <head><title>Books</title><meta charset="UTF-8"></head>
        #     <body>
        #     <p>Request: {self.path}</p>
        #     </body>
        #     </html>
        #     ''', "utf-8"))

    def books_list(self):
        return ", ".join(self.books)


if __name__ == "__main__":
    web_server = HTTPServer((host_name, server_port), MyServer)
    print(f"Server started http://{host_name}:{server_port}")

    try:
        web_server.serve_forever()
    except KeyboardInterrupt:
        pass

    web_server.server_close()

