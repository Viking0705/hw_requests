import requests

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)        
        data = response.json()
        url = data.get ('href')
        response = requests.put(url=url, data=open(file_path, 'rb'))        



if __name__ == '__main__':
    path_to_file = 'test2.txt'
    token = ""
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)