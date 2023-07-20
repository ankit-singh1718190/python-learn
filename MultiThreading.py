# MultiThreading is a techniqu which allow a cpu to 
# excute Multipal Threads of one process
# run Multipal task and funations  at the same time .
# single threading and mulitpal threading
# thread class methods 
# rUn(), start(),join(), isalive(), setname(), getname()
# class A:
#     def run(self):
#         for i in range(5):
#             print("ankit Singh")
# class B:
#     def run(self):
#         for i in range(5):
#             print("shivi singh") 
# t1=A()
# t2=B()
# t1.run()
# t2.run() 

# from time import sleep
# class A:
#     def run(self):
#         for i in range(5):
#             print("ankit Singh")
#             sleep(1)
# class B:
#     def run(self):
#         for i in range(5):
#             print("shivi singh")
#             sleep(1)
# t1=A()
# t2=B()
# t1.run()
# t2.run()                     

from threading import Thread
class A(Thread):
    def run(self):
        for i in range(5):
            print("ankit Singh")
class B(Thread):
    def run(self):
        for i in range(5):
            print("shivi singh")
t1=A()
t2=B()
t1.start()
t2.start()                     