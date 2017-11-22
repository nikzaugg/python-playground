age_dic = {"John":20, "Sara":18, "Nick":32,"Nina":40}
print age_dic
print age_dic["Sara"]
del age_dic["Sara"]
print age_dic
age_dic["Nick"] = 16
print age_dic

dic1 = dict(firstname="Ben", lastname = "black", age=32)
dic2 = dict(height = 1.85, weight = 85, footsize = 43)
dic3 = dict(job = "teacher", field = "chemistry")
dic_data = dict(basic_info = dic1, size = dic2, profession =dic3)
print dic_data

age_dic.clear()
print age_dic

print age_dic.get("Nick")
print age_dic.get("Carsten")

# Key Error
# print age_dic.get["Carsten"]

age_dic = {"John":20, "Sara":18, "Nick":32,"Nina":40}
key_list = age_dic.keys()
value_list = age_dic.values()
print key_list
print value_list

age_dic = {"John":20, "Sara":18, "Nick":32,"Nina":40}
print age_dic
age_dic.pop("John")
print age_dic

print age_dic.pop("Hanna","unknown")

print age_dic.pop("Hanna",None)

print "-----------------------"
age_dic = {"John":20, "Sara":18, "Nick":32,"Nina":40}
new_dic = {"Carsten":50, "Emi":22}
age_dic.update(new_dic)
print age_dic

print "-----------------------"
age_dic = {"John":20, "Sara":18, "Nick":32,"Nina":40}
new_dic = {"John":30, "Emi":22}
age_dic.update(new_dic)
print age_dic

list_items = age_dic.items()
print list_items