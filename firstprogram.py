# print("My Name is Hamiz")
# print("Hello World")
# print(23)


# name = "Hamiz"
# age = 19
# percentage = 87.8 

# print("My name is", name)
# print(type(name))
# print(type(age))
# print(type(percentage))

#Single Line

'''
Multi Line Comments 
'''



## Lists and tuples

# marks = [1,2,4,5]

# print(marks)


# marks = (1,2,4,5)
# print(marks.count(2))


# movies = []

# movie1 = input("Enter Favorite movie: ")
# movie2 = input("Enter Favorite movie: ")
# movie3 = input("Enter Favorite movie: ")


# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)
# print(movies)

# list = [1,"abc","abc",1]

# copyList = list.copy()
# copyList.reverse()

# if(copyList == list):
#     print("It is Palindrome")
# else: print("It is not")


# tuple = ("C","D","A","A","B","B","A")

# print(tuple.count("A"))


# ## Dictionary and sets 
# info = {
#     "name" : "Hamiz Muzaffer",
#     "subjects": ["DSA","DB","DDA"],
#     "age" : 20,
#     "isAdult" : True,
#     "marks": 24.4
# }

# # print(info["name2"]) #error
# # print(info.get("name")) #none

# info.update({"city" : "karachi"})
# print(info)




#sets 

# set = {1,2,4,5,4}
# print(set)

# collection = {} # empty dictionary

collection = set() # empty set 
# collection.add(2)
# collection.add(3)
# collection.add(4)
# collection.add(5)
# collection.clear()
# collection.pop()
# print(len(collection))


# set1 = {1,2,3,4}
# set2 = {4,5,6,7}

# print(set1.intersection(set2))


## Question 1 

# dict = {
#     "table" : ["list of facts and figures","a piece of furniture"],
#     "cat" : "a small animal"
# }

# print(dict)


## Question 2 

# set = {"python","java","C++","python","javascript","java","python","java","C++","c"}

# print(len(set))


## Question 3 

# dict = {}

# dsa = input("Enter Marks")
# dict.update({"DSA": dsa})
# db = input("Enter Marks")
# dict.update({"DB": db})
# daa = input("Enter Marks")
# dict.update({"DAA": daa})

# print(dict)


## Question 4 

set = {("int",9),("float",9.0)}

print(set)