from urllib.request import urlopen
from pathlib import Path
from defaults import  *



class PayLoadProcessing(object):

    def __init__(self, config_file):
        self.config_file = config_file

    def download_file(self,download_dir):

        with urlopen(self.config_file) as url:
            content = url.read()

        #now write the content to a file and save to the download folder
        f = open(download_dir+"sample-text-file.txt", "a")
        f.write(str(content))

        f.close()

        return "File saved"

    def read_file(self,download_dir):
        sample_file = Path(download_dir + "sample-text-file.txt")
        if sample_file.is_file():
            #open the file and read the content
            f = open(download_dir + "sample-text-file.txt", "r")
            return f.read()
        else:
            return "Please perform the download action first to read the file"
