import cherrypy
from payload_processing import *
from webservice import *
from defaults import *



@cherrypy.expose
@cherrypy.tools.json_out()
@cherrypy.tools.json_in()
class ManageFileService(object):
    def __init__(self, args):
        self.args = args

    def POST(self):
        data = cherrypy.request.json

        payload_processing = PayLoadProcessing(self.args)

        if 'action' not in data:
            output = "No action in json data, this simple service must contain the key word action"
        else:
            if data['action']== "download":

                output = payload_processing.download_file(DOWNLOAD_DIR)
            elif data['action'] == "read":
                output = payload_processing.read_file(DOWNLOAD_DIR)
            else:
                output  ="Request not found, this webservice only allow download and read action"

        return output