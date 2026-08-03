# 0(1) - Constant time

bookself = ["book1","book2"]

def get_first_book(books):
    print(books[0])
get_first_book (bookself)



# 1(1)- linear time 

def read_all_books(books):
    for book in books:
        print(book)
read_all_books(bookself)




#Array vs list

#list example 

my_list = [10,"Eftekhar",3.15, True]
print(my_list)

#Array example 
import array

my_array= array.array('i',[10, 20,30,90])
print(my_array)


#Indexing Tecnique

#1. positive indexing 
#2. negative indexing 



fruits=["apple","banana","orange","mango"]

#positive indexing [0,1,2,3]
#negative indexing [-4,-3,-2,-1]

print(fruits[0])#positive indexing
print(fruits[-4])#negative indexing

#array operation 
#1.Access/Read 
#2.Search
#3.Insertion 
#4.Deletion 
#5.Append

