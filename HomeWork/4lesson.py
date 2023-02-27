# class Category:
#     categories=[]
#
#     @classmethod
#     def add (cls, name_categiriya):
#         if name_categiriya in categories:
#             categories.append(name_categiriya)
#         else:
#             raise 162016\
#                 ("Value error")
#
# cat=Category()
# cat.add("C")


# class RegisterForm:
#     def __init__(self, username, password):
#         self.username=username
#         self.password=password
#
#     def is_valid(self):
#         if len(self.username)>=2 and isinstance(self.username, str) \
#         and len(self.password)>=8 and isinstance(self.password, str):
#
#             print(1)
#         else:
#             print(0)
#
# reg= RegisterForm('sss','ddd55555')
# print(reg.is_valid())


# password='q23dq23fdqwef3'
# for i in filter(str.isdigit, password):
#     print(1)
#     break
# for i in filter(str.isupper(), password):
#     print(1)
#     break


class Number:
    def __init__(self, *args):
        self.ll=args
    def average():
        kol=len(self.ll)
        sum=0
        for i in self.ll:
            sum+=i
        print(sum/kol)


n=Number([2,3,4,5,6,7,8,9,45,4])
n.average()