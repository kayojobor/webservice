import cherrypy
import logging.config
from defaults import *
from manage_file import *


LOCAL_DIR = '/webservice/'
KEY_DIR= LOCAL_DIR + "keys/"
DOWNLOAD_DIR= LOCAL_DIR + "download/"
LOG_DIR = LOCAL_DIR + 'logs/'
CONFIG_FILE = LOCAL_DIR + "config.yaml"



# CherryPy Log Server
logging.config.dictConfig(
    {
    'version' : 1,

    'formatters': {
        'void': {
            'format': ''
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {

        'cherrypy_access': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': LOG_DIR + 'cp_access.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'cherrypy_error': {
            'level':'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'formatter': 'void',
            'filename': LOG_DIR + 'cp_errors.log',
            'maxBytes': 10485760,
            'backupCount': 20,
            'encoding': 'utf8'
        },
        'cherrypy_console': {
                    'level':'INFO',
                    'class':'logging.StreamHandler',
                    'formatter': 'void',
                    'stream': 'ext://sys.stdout'
                },
    },
    'loggers': {

        'cherrypy.access': {
            'handlers': ['cherrypy_access'],
            'level': 'INFO',
            'propagate': False
        },
        'cherrypy.error': {
            'handlers': ['cherrypy_error','cherrypy_console'],
            'level': 'INFO',
            'propagate': False
        },
    }
})


cfg = get_cfg_defaults()
cfg.merge_from_file(CONFIG_FILE)




def validate_password(realm,username, password):

    if username ==cfg.WEBSERVICE.USER_NAME and cfg.WEBSERVICE.PASSWORD ==password:
       return True
    else:
        raise cherrypy.HTTPError(401, 'Unauthorized')




def http_error(status, message, traceback, version):
    http_code= status.split(' ')[0]

    cases = {
        401: lambda: "Authorised, please request for login details",
        405: lambda: "The method you specified is not allowed. This simple web service has only the download and read action method",
        415: lambda: "Unsupport payload format, please send a json format only",
        403 : lambda: "YOu dont have the necessary permission",
    }
    output = cases.get(int(http_code), lambda:"Please contact supoport if you keep having issue using this web service")()
    return output




@cherrypy.expose
class HomeService(object):
    def GET(self):
        return 'Welcome to this simple webservice.'


if __name__ == '__main__':

    # SSL enabled
    if cfg.WEBSERVICE.SSL :
        cherrypy.config.update({'server.ssl_module' : 'builtin',
                            'server.ssl_certificate' : KEY_DIR + 'cert.pem',
                            'server.ssl_private_key' : KEY_DIR + 'privkey.pem'})
    else:
        cherrypy.config.update({'server.socket_port': cfg.WEBSERVICE.PORT,
                                'server.socket_host': '0.0.0.0'})


    # Web Service config
    conf = {
        '/': {
            'response.timeout': cfg.WEBSERVICE.RESPONSE_TIME,
            'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
            'tools.sessions.on': True,
            'tools.response_headers.on': True,
            'tools.response_headers.headers': [('Content-Type', 'text/plain')],

            # Basic Authentication
            'tools.auth_basic.on': cfg.WEBSERVICE.BASIC_AUTHENTICATION,
            'tools.auth_basic.realm': 'om',
            'tools.auth_basic.checkpassword': validate_password,
            'error_page.default': http_error  #to disply error
        }
    }


    start = HomeService()
    start.manage_file = ManageFileService(cfg.WEBSERVICE.SAMPLE_FILE)
    cherrypy.quickstart(start, config=conf)
