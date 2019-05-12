flag=0
with open(r'C:\Users\29110\Desktop\text-file-process-pengmingxiao3759-master\text-file-process-pengmingxiao3759-master\log_files\201811123022.log',encoding='utf8') as f:
    for line in f:
        list1=line.split(' ')
        str1=list1[1]
        list2=str1.split('：')
        str2=list2[1]
        list3=str2.split(',')
        str3=list3[0]
        if str3=='201811123022':
            flag+=1
            
print(flag)