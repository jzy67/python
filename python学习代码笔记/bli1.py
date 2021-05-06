name_list=["ji","sd","yu"]
# print(name_list[0]);
# name_list[2]="空";
# print(name_list);
# for name in name_list:
#     print(f"{name}");
num=name_list.index("sd")
print(num)
name_list.append("zh")
name_list.insert(1,"SD")
print(name_list)
# del name_list[0];
# name_list.remove("sd");
print(name_list)
print(name_list[0:2])
print(name_list[-1],name_list[-2:],name_list[0:3:2])
name_list.append(["hu",24,48])
print(name_list[-1][1])
