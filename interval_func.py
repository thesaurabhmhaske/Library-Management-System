import threading
import numpy as np

stopNow = 0
a = np.array([])
no_of_books = 0
def RepeatFunc():
    global no_of_books
    global a 
    # print(a)
    # print("Running RepeatFunc")
    a = np.append(a, no_of_books)
    no_of_books = 0
    if not stopNow: threading.Timer(20,RepeatFunc).start()
