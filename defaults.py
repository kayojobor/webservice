from yacs.config import CfgNode as CN

_C = CN()
#########################################################################################
# System Parameters
#########################################################################################
_C.WEBSERVICE = CN()
_C.WEBSERVICE.USER_NAME = ""
_C.WEBSERVICE.PASSWORD = ""
_C.WEBSERVICE.PORT = 8080
_C.WEBSERVICE.RESPONSE_TIME=300
_C.WEBSERVICE.SSL=False
_C.WEBSERVICE.BASIC_AUTHENTICATION= True
_C.WEBSERVICE.SSL_PORT=443
_C.WEBSERVICE.SAMPLE_FILE="https://www.learningcontainer.com/wp-content/uploads/2020/04/sample-text-file.txt"



def get_cfg_defaults():
  """Get a yacs CfgNode object with default values for my_project."""
  return _C.clone()

