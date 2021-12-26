# isTrue = False
# a = 2
# b = 2.5
# strone = "one"
# strthree = "three"
#
# if a > 2 and strone == "one" or not strthree == "two" : # not refer to the value of strthree ,convert true to fals and vise verca
#     print("a is greater then 2")
# elif b == 2.5:
#     print("something")
# elif strone == "3":
#     print("abc")
# else:
#     print("a is lower then 2")
# my_list = ["hen", "lior" ,"lior","ariel"]
# my_other_list = []
# if a > 0 and a <= 4 : # u can us  :
#     print ("ok")
#  #   if my_list[0] == "hen" or mylist
#
# if "hen" in my_list:   #use in to find in list
#     print("we have found hen!")
#     if my_other_list :  #check if list is empty
#         print("good")
# if len(my_list) > 0 :
#     print("hey")
#
# # c = 5
# # d = 5
# # if c is d :
# #     print("c is d") #works for pemitive
#
# c = ["aaa", "1"]
# d = ["aaa", "1"]
# e = 9
# if c is d :
#     print("c is d")
# if type(e) is int :
#     print ("e is an intiger")
#     #it's better to define a variable
# what_to_print = "hello world !"
# print("hello world !")
# print("hello world !")
# print(what_to_print)
# print(what_to_print)
# print(what_to_print * 4)
# print(list (range(9,2,-1)))
#
# list_of_names = ["michael", "noam" , "lior" , "amichai"]
# amount_of_print = 4
# for i in range(4) :
#     print(i)
#     print(what_to_print)
#
# for i in range(len(list_of_names)):
#     print(list_of_names[i])
# for name in list_of_names:
#     print(name)
#
# a = 0
# while a < 10 :
#     print(a)
#     a= a + 1
#
# for name in list_of_names:
#     if name == "hen" :
#         continue
#     print(name)

#תרגול  :
# g=0
# for i in range(1,100):
#    d= g/7
#    g=g+1
#    if d is int :
#        continue
#        els:print(d)

for i in range(1,101):
    if i % 7 ==0 or "7" in str(i):
        continue
    print(i)


a= 0
while a < 10 :
    print(a)
    a = a+1
else:
    print("finished sucsesfully")

while a != "q" :
    a = input("enter q or not : ")
else:
    print("finished sucsesfully")