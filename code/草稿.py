"""
@File    : 草稿.py
@Time    : 2019-11-15 16:05
@Author  : 李浩然
@Software: PyCharm
@Email: 1901210423@pku.edu.cn
"""

if __name__=="__main__":
    n=int(input())
    str=input()
    str_list=str.split(' ')
    num_list=[int(i) for i in str_list]
    for i in range(1,len(num_list)):
        for j in range(len(num_list)-i):
            if num_list[j]>num_list[j+1]:
                temp=num_list[j]
                num_list[j]=num_list[j+1]
                num_list[j+1]=temp
    for i in num_list:
        print(i,end=' ')
