import numpy as np
np.random.seed(42)

student = np.array(["rahul","priya","amit","neha"
                    ,"ravi","pooja","karan","sneha","arjun","divya"])

marks = np.random.randint(40,100,size=(10,5))
subject = np.array(["math","science","english","hindi","coputer"])

print("shape:",marks.shape)
print(marks)

total_marks = np.sum(marks,axis=1)
avg_marks = np.mean(marks,axis=1)
subject_avg = np.mean(marks,axis=0)

print("total pre student:",total_marks)
print("avg per student:",np.round(avg_marks))
for sub,avg in zip(subject,subject_avg):
    print(f"{sub}:{avg:}.1f")

print(f'Class Avg: {np.mean(marks):.2f}') 
print(f'Std Dev  : {np.std(marks):.2f}') 
print(f'Max Mark : {np.max(marks)}')
print(f'Min Mark : {np.min(marks)}')

grades = np.where(avg_marks >= 90, 'A+', 
                          np.where(avg_marks >= 80, 'A', 
                                 np.where(avg_marks >= 70, 'B',
                                        np.where(avg_marks >= 60, 'C', 'D'))))

for name, avg ,grade in zip(student, avg_marks,grades):
    print(f"{name:<8}|avg :{avg:5.1f}| grade:{grades}")

failed_any = np.any(marks < 50, axis=1)
print("\nfailed student:",student[failed_any])

rank_order = np.argsort(total_marks)[::-1]

print(f"{"rank": <5} {"name":<10} {"total":>6} {"avg": >6} {"grade ": >6}")
print("-" * 42)
for rank,idx in enumerate(rank_order,start = 1):
    print(f"{rank:<5}{student[idx]:<10}{total_marks[idx]:> 6}")

print("\ntop 3:",student[rank_order[:3]])

print("needs help:", student[rank_order[-3:]])
best_sub_idx = np.argmax(marks, axis=1)
worst_sub_idx = np.argmin(marks, axis = 1)

for i , name in enumerate(student):
    best = subject[best_sub_idx[i]]
    worst = subject[worst_sub_idx[i]]
    print(f"{name:<8}|best : {best : <10}| improve:{worst}")

topper = np.argmax(marks, axis = 0)
for sub , idx in zip(subject,topper):
    score = marks [idx, list(subject).index(sub)]
    print(f"{sub:<10}: {student [idx]}({score})")

normalized = (marks - np.min(marks))/(np.max(marks) - np.min(marks))
print("normalized(first row):", np.round(normalized[0]),2)

z_score = (marks - np.mean(marks)) / np.std(marks)
print("z_score(first row ):",np.round(z_score[0],2))

clipped = np.clip(marks,0,100)

percentage = (total_marks / 500) * 100
for name , pct in zip (student , percentage):
    print(f"{name}:{pct :.1f}%")


ranks = np.argsort(np.argsort(-total_marks)) + 1 
report = np.column_stack([total_marks, np.round(avg_marks,1), ranks]) 
print('=' * 55)
print('      FINAL STUDENT REPORT SUMMARY')
print('=' * 55)
print(f'{"Name":<10}{"Total":>7}{"Avg":>7}{"Rank":>6}{"Grade":>7}')
print('-' * 55)
for i, name in enumerate(student): 
       print(f'{name:<10}{int(report[i,0]):>7}{report[i,1]:>7}'     
                  f'{int(report[i,2]):>6}{grades[i]:>7}')
       print('=' * 55)
       print(f'Class Avg : {np.mean(avg_marks):.2f}')
       print(f'Pass Rate : {np.sum(~failed_any)}/10')
       print(f'A Grades  : {np.sum(grades=="A") + np.sum(grades=="A+")}')
       print(f'Top Student: {student[np.argmax(total_marks)]}')