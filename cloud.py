import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BHYDD6G5kiHudtrzumrlUe5_NwgGXATt5oexHzh29BIM8P3wNKnNYDzGogvrhiqo6jCA96A6Fj7aGj9o_LK4IGJEP4LO1nGbLNStnn2dOba_Vxck1VdLmvQNTpPEL__SQORimXMf6jk1'
    transferData = TransferData(access_token)

    file_from = input("Enter File Name")
    file_to = input("Enter Full Path")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("File Uploaded")

if __name__ == '__main__':
    main()