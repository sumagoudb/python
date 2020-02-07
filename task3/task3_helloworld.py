#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import re, git, os, argparse

# PORT_NUMBER = 8080

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
    #Handler for the GET requests
    def do_GET(self):
        if self.path == "/helloworld":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("Hello Stranger")
            return
        elif self.path.startswith("/helloworld?name"):
            name_obj = "/" + self.path.replace("/helloworld","")
            name = re.findall('[A-Z][^A-Z]*', name_obj)
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            self.wfile.write("Hello " + name[0] + " " + name[1])
            return
        if self.path == "/versionz":
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            repo = git.Repo(".", search_parent_directories=True)
            resp = {'hash': str(repo.head.object.hexsha), 'repo_name': os.path.basename(repo.working_dir)}
            self.wfile.write(resp)
            return
        else:
            self.send_response(200)
            self.send_header('Content-type','text/html')
            self.end_headers()
            # Send the html message
            self.wfile.write("Hey you are are suppose to use '/helloworld' or '/helloworld?FirstnameMiddlenameLastname'")
            return

parser = argparse.ArgumentParser(description='Process input.')
parser.add_argument('--portnumber', type=int, default=8080, help='an integer for the accumulator')
args = parser.parse_args()

try:
    #Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', args.portnumber), myHandler)
	print ('Started httpserver on port ' , args.portnumber)
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
