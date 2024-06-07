from multiprocessing import Process

fayl_txt = ["fayl1.txt", "fayl2.txt"]


def count_words(filename):
    with open(filename, 'r') as f:
        text = f.read()
    words = text.split()
    print(f"{filename} fayldagi sozlar {len(words)} ta")


if __name__ == '__main__':
    processing = []
    for fayl in fayl_txt:
        task_1 = Process(target=count_words, args=(fayl,))
        task_1.start()
        processing.append(task_1)
    for proces in processing:
        proces.join()

