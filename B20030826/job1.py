import datetime
import email
import html
import http.server
import io
import mimetypes
import os
import posixpath
import re
import shutil
import sys
import urllib.error
import urllib.parse
import urllib.request
import hashlib
from http import HTTPStatus
 
__version__ = "0.1"
__all__ = ["SimpleHTTPRequestHandler"]
 
class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    
    server_version = "SimpleHTTP/" + __version__
    extensions_map = _encodings_map_default = {
        '.gz': 'application/gzip',
        '.Z': 'application/octet-stream',
        '.bz2': 'application/x-bzip2',
        '.xz': 'application/x-xz',
    }
 
    def __init__(self, *args, directory=None, **kwargs):
 
        if directory is None:
            directory = os.getcwd()
        self.directory = os.fspath(directory)
        super().__init__(*args, **kwargs)
 
    def do_GET(self):
        f = self.send_head()
        if f:
            try:
                self.copyfile(f, self.wfile)
            finally:
                f.close()
 
    def do_HEAD(self):
        f = self.send_head()
        if f:
            f.close()
 
    def send_head(self):
        path = self.translate_path(self.path)
        f = None
        if os.path.isdir(path):
            parts = urllib.parse.urlsplit(self.path)
            if not parts.path.endswith('/'):
                # redirect browser - doing basically what apache does
                self.send_response(HTTPStatus.MOVED_PERMANENTLY)
                new_parts = (parts[0], parts[1], parts[2] + '/',
                             parts[3], parts[4])
                new_url = urllib.parse.urlunsplit(new_parts)
                self.send_header("Location", new_url)
                self.end_headers()
                return None
            for index in "index.html", "index.htm":
                index = os.path.join(path, index)
                if os.path.exists(index):
                    path = index
                    break
            else:
                return self.list_directory(path)
 
        ctype = self.guess_type(path)
        if path.endswith("/"):
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None
        try:
            f = open(path, 'rb')
        except OSError:
            self.send_error(HTTPStatus.NOT_FOUND, "File not found")
            return None
        try:
            fs = os.fstat(f.fileno())
            # Use browser cache if possible
            if "If-Modified-Since" in self.headers and "If-None-Match" not in self.headers:
                # compare If-Modified-Since and time of last file modification
                try:
                    ims = email.utils.parsedate_to_datetime(self.headers["If-Modified-Since"])
                except (TypeError, IndexError, OverflowError, ValueError):
                    # ignore ill-formed values
                    pass
                else:
                    if ims.tzinfo is None:
                        # obsolete format with no timezone, cf.
                        # https://tools.ietf.org/html/rfc7231#section-7.1.1.1
                        ims = ims.replace(tzinfo=datetime.timezone.utc)
                    if ims.tzinfo is datetime.timezone.utc:
                        # compare to UTC datetime of last modification
                        last_modif = datetime.datetime.fromtimestamp(fs.st_mtime, datetime.timezone.utc)
                        # remove microseconds, like in If-Modified-Since
                        last_modif = last_modif.replace(microsecond=0)

                        if last_modif <= ims:
                            self.send_response(HTTPStatus.NOT_MODIFIED)
                            self.end_headers()
                            f.close()
                            return None

                self.send_response(HTTPStatus.OK)
                self.send_header("Content-type", ctype)
                self.send_header("Content-Length", str(fs[6]))
                self.send_header("Last-Modified", self.date_time_string(fs.st_mtime))
                self.send_header("Cache-Control", "public, max-age=86400")
                self.end_headers()
                return f

                        
def list_directory(self, path):
    try:
        list = os.listdir(path)
    except OSError:
        self.send_error(HTTPStatus.NOT_FOUND, "No permission to list directory")
        return None
    list.sort(key=lambda a: a.lower())
    r = []
    try:
        displaypath = urllib.parse.unquote(self.path,
                                           errors='surrogatepass')
    except UnicodeDecodeError:
        displaypath = urllib.parse.unquote(path)
    displaypath = html.escape(displaypath, quote=False)
    enc = sys.getfilesystemencoding()
    title = 'Directory listing for %s' % displaypath
    r.append('<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" '
             '"http://www.w3.org/TR/html4/strict.dtd">')
    r.append('<html>\n<head>')
    r.append('<meta http-equiv="Content-Type" '
             'content="text/html; charset=%s">' % enc)
    r.append('<title>%s</title>\n</head>' % title)
    r.append('<body>\n<h1>%s</h1>' % title)
    r.append('<hr>\n<ul>')
    for name in list:
        fullname = os.path.join(path, name)
        displayname = linkname = name
        # Append / for directories or @ for symbolic links
        if os.path.isdir(fullname):
            displayname = name + "/"
            linkname = name + "/"
        if os.path.islink(fullname):
            displayname = name + "@"
            # Note: a link to a directory displays with @ and links with /
        r.append('<li><a href="%s">%s</a></li>'
                 % (urllib.parse.quote(linkname,
                                       errors='surrogatepass'),
                    html.escape(displayname, quote=False)))
    r.append('</ul>\n<hr>\n</body>\n</html>\n')
    encoded = '\n'.join(r).encode(enc, 'surrogateescape')
    f = io.BytesIO()
    f.write(encoded)
    f.seek(0)
    self.send_response(HTTPStatus.OK)
    self.send_header("Content-type", "text/html; charset=%s" % enc)
    self.send_header("Content-Length", str(len(encoded)))
    self.send_header("Last-Modified", self.date_time_string())
    self.send_header("Cache-Control", "public, max-age=86400")
    self.end_headers()
    return f

def translate_path(self, path):
    # abandon query parameters
    path = path.split('?', 1)[0]
    path = path.split('#', 1)[0]
    path = posixpath.normpath(urllib.parse.unquote(path))
    words = path.split('/')
    words = filter(None, words)
    path = self.directory
    for word in words:
        drive, word = os.path.splitdrive(word)
        head, word = os.path.split(word)
        if word in (os.curdir, os.pardir):
            continue
        path = os.path.join(path, word)
    return path

def copyfile(self, source, outputfile):
    shutil.copyfileobj(source, outputfile)

def guess_type(self, path):
    base, ext = posixpath.splitext(path)
    if self.extensions_map:
        return self.extensions_map.get(ext.lower(), self.default_type)
    else:
        return self.default_type
class ThreadingHTTPServer(ThreadingMixIn, HTTPServer):
    daemon_threads = True

def test(HandlerClass=SimpleHTTPRequestHandler,
    ServerClass=ThreadingHTTPServer):
    port = 8000
    server_address = ('', port)
if __name__ == '__main__':
    test()