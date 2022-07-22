import pprint as p
student_mark={}
with open('D:\\Python Project\\medical-project\\python_basics_code\\10_file_handling\\student_marks.csv','r') as f:
    lines= f.readline()
    #print(lines)
    key = lines.split(',')
    key[-1]=key[-1][:-1]
    #print(key)
    for k in key:
        student_mark[k] = []
    #print(student_mark)
    for d in f.readlines():
        data = d.split(',')
        data[-1] = data[-1][:-1]
        #print(data)
        i=0
        for k in student_mark:
            student_mark[k].append(data[i])
            i= i+1

#print(student_mark)
student_mark['total_marks'] = [0]*5
#print(student_mark)
subject_all = ['Maths', 'Physics', 'Chemistry', 'English', 'Biology', 'Economics', 'History', 'Civics']
#print(subject_all)
for n in range(0,5):

        sum = 0
        for i in subject_all:
            try:
                sum = sum + int(student_mark[i][n])
                print(sum)
            except:
                pass
        student_mark['total_marks'][n]= sum
print(student_mark)

student_mark['Avg'] = [0]*5
print(student_mark)
total_len = len(subject_all)
for i in range(0,5):
    student_mark['Avg'][i]= student_mark['total_marks'][i]/total_len
print(student_mark)



