import sys
import math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import interval_func
import date_time
class Library:
      def __init__(self,listofbooks):#this init method is the first method to be invoked when you create an object
            #what attributes does a library in general have? - for now, let's abstract and just say it has availablebooks (we're not going to program the shelves, and walls in!)
            self.availablebooks=listofbooks
            self.lendedBooks = []

      def displayAvailablebooks(self):
                   print("The books we have in our library are as follows:")
                   print("================================")
                   df = pd.DataFrame(self.availablebooks, columns =['Book', 'Id']) 
                   df.index += 1
                   print(df)

      def lendBook(self,requestedBook):
            # Array of available books (first coloumn of available books)
            array=np.array([i[0] for i in self.availablebooks])
            if requestedBook in array:
                  x = np.where(array == requestedBook)
                  index = x[0][0]

                  print("Enter your name")
                  user_name = input()
                  
                  self.availablebooks[index].append(user_name)
                  self.availablebooks[index].append(date_time.getDate())
                  self.availablebooks[index].append(date_time.getTime())
                  # Example : ['Let us c', 231 ,'Mayank', '2021-11-09', '23:52:26.548077']
                  self.lendedBooks.append(self.availablebooks[index])
                  del self.availablebooks[index]
                  print("The book you requested has now been borrowed")
                  interval_func.no_of_books = interval_func.no_of_books + 1
            else:
                  print("Sorry the book you have requested is currently not in the library")
                  
      def addBook(self,returnedBook):
            self.availablebooks.append(returnedBook)
            array=np.array([i[0] for i in self.lendedBooks])
            # returnedBook[0] is the book name
            if returnedBook[0] in array:
                  x = np.where(array == returnedBook[0])
                  index = x[0][0]
                  del self.lendedBooks[index]
                  print("Thanks for returning your borrowed book")
            else:
                  print("Enter valid book name")
      
      def displayLendedbooks(self):
                  print("The books we have lended are as follows:")
                  print("================================")
                  df = pd.DataFrame(self.lendedBooks, columns =['Book', 'Id', 'Username', 'Date', 'Time']) 
                  df.index += 1
                  print(df)
                  # left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
                  # display(left_aligned_df)

      def lendedBooksGraph(self):
                  months = np.array(["Jan", "Feb", "Mar", "April", "May", "June", "July", "Aug", "Sep", "Oct", "Dec"])
                  x = months[0:interval_func.a.size]

                  # Forcing Matplotlib to show only integers on Y-axis
                  minimum_ele = min(interval_func.a)
                  maximum_ele = max(interval_func.a)
                  new_list = range(math.floor(min(interval_func.a)), math.ceil(max(interval_func.a))+1)

                  plt.yticks(new_list)
                  plt.ylabel("Number of books")
                  plt.title("Number of books issued every month")
                 
                  plt.bar(x,interval_func.a)
                  plt.show()

                  # print(x)
                  # print(interval_func.a)
            
class Student:
      def requestBook(self):
            print("Enter the name of the book you'd like to borrow >> ")
            self.book=input()
            return self.book

      def returnBook(self):
            print("Enter the name of the book you'd like to return >> ")
            self.book=input()
            print("Enter the code of the book you'd like to return >> ")
            self.book_code=input()
            book_info = [self.book, self.book_code]
            return book_info

def main():
      # Repeating fumction
      interval_func.RepeatFunc()  

      interval_func.a = np.delete(interval_func.a, 0) 

      library = Library([['Let us c', 231], ['Python programming', 232], 
       ['Cant hurt me', 233], ['Atomic habits', 234], ['Divergent', 235],
        ['Recursion', 236], ['Hopeless', 237], ['Revenger', 238]])

      student = Student()

      done=False
      while done==False:
            print(""" ======LIBRARY MENU=======
                  1. Display all available books
                  2. Request a book
                  3. Return a book
                  4. Display landed books
                  5. Show the graph of lended books
                  6. Exit
                  """)
            choice = int(input("Enter Choice:"))
            if choice==1:
                        library.displayAvailablebooks()
            elif choice==2:
                        library.lendBook(student.requestBook())
            elif choice==3:
                        library.addBook(student.returnBook())
            elif choice==4:
                        library.displayLendedbooks()
            elif choice==5:
                        library.lendedBooksGraph()
            elif choice==6:
                  sys.exit()
                  
main()