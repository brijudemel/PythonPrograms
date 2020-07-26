import csv
def writing(message):
    f= open("StudentDatabase.csv","a",newline='')
    writer=csv.writer(f)
    if f.tell()==0:
        writer.writerow(["Name","Register Number","Age","Sex","Contact Number","Email","Father's Name","Father's Number","Mother's Name","Mother's Number"])
    writer.writerow(message)
    f.close()

if __name__ == '__main__':
    c=1
    while True:
        l=[]
        print(f"Enter details of student{c}")
        l.append(input("Name:\t"))
        l.append(input("Register Number:\t"))
        while True:
            try:
                l.append(int(input("Age:\t")))
                break
            except:
                print("Age should be a number please enter again!")
        l.append(input("Sex:\t"))
        while True:
            try:
                l.append(int(input("Contact Number:\t")))
                break
            except:
                print("Contact Number should be a number please enter again!")
        l.append(input("Email:\t"))
        l.append(input("Father's Name:\t"))
        while True:
            try:
                l.append(int(input("Father's Number:\t")))
                break
            except:
                print("It should be a number please enter again!")
        l.append(input("Mother's Name:\t"))
        while True:
            try:
                l.append(int(input("Mother's Number:\t")))
                break
            except:
                print("It should be a number please enter again!")
        writing(l)
        another=input("Do you want to enter details of another student: Enter yes or no:\t")
        if another.lower()=="yes":
            c=c+1
        else:
            break
