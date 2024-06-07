from multiprocessing import Process
import requests
listt = ["https://www.google.com/url?sa=i&url=https%3A%2F%2Fmimigram.ru%2Fblog%2Fchto-takoe-foto-tekhnologiya-ili-iskusstvo%2F&psig=AOvVaw0X45lzj7XSD8-pSrILl78r&ust=1717875503291000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNCM4oyfyoYDFQAAAAAdAAAAABAE",
         "https://www.google.com/url?sa=i&url=https%3A%2F%2Ffotoapp.co%2F&psig=AOvVaw0X45lzj7XSD8-pSrILl78r&ust=1717875503291000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCNCM4oyfyoYDFQAAAAAdAAAAABAJ"]


def download_image(image_url, save_path):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            f.write(response.content)
    else:
        print(f'hatolik {response.status_code}')


if __name__ == '__main__':
    processing = []
    number = 1
    for fayl in listt:
        name = "image"
        name += str(number)
        name += ".jpg"
        task_1 = Process(target=download_image, args=(fayl, name))
        task_1.start()
        processing.append(task_1)
    for proces in processing:
        proces.join()

