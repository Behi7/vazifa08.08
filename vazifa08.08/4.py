from multiprocessing import Process

fayl_txt = ["fayl1.txt", "fayl2.txt"]


def count_words(filename):
    longest_word = ""
    with open(filename, "r") as f:
        for line in f:
            for word in line.split():
                if len(word) > len(longest_word):
                    longest_word = word
    print(f"{filename} dagi eng uzun soz {longest_word}")


if __name__ == '__main__':
    processing = []
    for fayl in fayl_txt:
        task_1 = Process(target=count_words, args=(fayl,))
        task_1.start()
        processing.append(task_1)
    for proces in processing:
        proces.join()

