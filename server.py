import os
try:
  from CGIHTTPServer import CGIHTTPRequestHandler as Handler
  from SocketServer import TCPServer as Server
except:
  from http.server import CGIHTTPRequestHandler as Handler
  from http.server import HTTPServer as Server
# Read port selected by the cloud for our application
PORT = int(os.getenv('PORT', 8000))
# Change current directory to avoid exposure of control files
os.chdir('www')

httpd = Server(("", PORT), Handler)
try:
  print("Start serving at port %i" % PORT)
  httpd.serve_forever()
except KeyboardInterrupt:
  pass
httpd.server_close()

