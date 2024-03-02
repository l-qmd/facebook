from http.server import CGIHTTPRequestHandler, HTTPServer

httpd = HTTPServer(('',8080), CGIHTTPRequestHandler)
print("Demarrage du serveur web ...")
httpd.serve_forever()