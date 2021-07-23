from pathlib import Path
from defaults import  *
import requests


class PayLoadProcessing(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def download_file(self,download_dir):

        r = requests.get(self.config_file, allow_redirects=True)

        open(download_dir+'sample-text-file.txt', 'wb').write(r.content)


        return "File saved"

    def read_file(self,download_dir):
        sample_file = Path(download_dir + "sample-text-file.txt")
        if sample_file.is_file():
            #open the file and read the content
            f = open(download_dir + "sample-text-file.txt", "r")
            return f.read()
        else:
            return "Please perform the download action first to read the file"
