import tornado.ioloop
import tornado.web
import tornado.httpserver
import os
import collections
import string

from tornado.options import define, options, parse_command_line

define('port', default=8888, help='run on the given port', type=int)
define('debug', default=False, help='run in debug mode')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/', MainHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            debug=options.debug,
        )
        super(Application, self).__init__(handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        code = self.get_argument('code')
        decrypted = self.decrypted(code)
        self.write(decrypted)

    @staticmethod
    def decrypted(code, n=3):
        code_lower = code.lower()
        alph_lower = string.ascii_lowercase
        decrypt = collections.deque(alph_lower)
        decrypt.rotate(n)
        decrypt = ''.join(list(decrypt))
        translated = code_lower.translate(
            {ord(x): y for (x, y) in zip(alph_lower,
                                         decrypt)})
        for i in code:
            if i.isupper():
                index = code.index(i)
                translated = translated[:index] + translated[index].upper() + \
                             translated[(index + 1):]

        return translated


def main():
    parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
