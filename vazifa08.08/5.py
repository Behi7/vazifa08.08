from multiprocessing import Process
import string
fayl_txt = ["fayl1.txt", "fayl2.txt"]


def no_punct(filename):
    punctuation = string.punctuation
    with open(filename, 'r') as f:
        text = f.read()
    no_punctuation_text = text.translate(str.maketrans('', '', punctuation))
    print(no_punctuation_text)



if __name__ == '__main__':
    processing = []
    for fayl in fayl_txt:
        task_1 = Process(target=no_punct, args=(fayl,))
        task_1.start()
        processing.append(task_1)
    for proces in processing:
        proces.join()

