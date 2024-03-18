import sys
import json
import time
import schedule
import pandas as pd
from os import environ, remove
from pathlib import Path
from ftplib import FTP_TLS

def get_ftp() -> FTP_TLS:
    #get ftp details
    FTPHOST = environ["FTPHOST"]
    FTPUSER = environ["FTPUSER"]
    FTPPASS = environ["FTPPASS"]

    # print(f"test: {FTPHOST}")

    #return authenticated FTP
    ftp = FTP_TLS(FTPHOST, FTPUSER, FTPPASS)
    ftp.prot_p()
    return ftp

def upload_to_ftp(ftp: FTP_TLS, file_source: Path):
    with open(file_source, "rb") as fp:
        ftp.storbinary(f"STOR {file_source.name}", fp)


def read_csv(config: dict) -> pd.DataFrame:
    url = config["URL"]
    params = config["PARAMS"]
    return pd.read_csv(url, **params)

def delete_file (file_source: Path):
    remove(file_source)

def pipeline():
     
    #load source config
    with open("config.json", "rb") as fp:
        config =json.load(fp)

    #to get authenticated ftp object
    ftp = get_ftp() 

    #Loop through each config to get the sourcename and its config    
    for source_name, source_config in config.items(): #iterate config.json dict
        file_name = Path(source_name + ".csv")
        df = read_csv(source_config)
        df.to_csv(file_name, index=False)

        print(f"File {file_name} has been downloaded.")

        upload_to_ftp(ftp, file_name)
        print(f"File {file_name} has been uploaded to FTP.")

        delete_file(file_name)
        print(f"File {file_name} has been deleted.")
    
if __name__ =="__main__":

    param = sys.argv[1]

    if param == "manual":
        pipeline()

    elif param == "schedule":
        schedule.every().day.at("19:00").do(pipeline)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else: 
        print("Invalid paramater. The pipeline will not run")
    
         









