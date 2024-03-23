import os

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def upload_file(dir_path):
    try:
        drive = GoogleDrive(gauth)

        for file_name in os.listdir(dir_path):
            file = drive.CreateFile({"title": f"{file_name}"})
            file.SetContentFile(os.path.join(dir_path, file_name))
            file.Upload()

    except Exception as er:
        print(er)


if __name__ == "__main__":
    upload_file("D:/Coding/PYTHON/TGBOTS/VysotaBot/data/name_01.01.2024")
