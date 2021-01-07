import argparse
import sys
import datetime

def printTD():
    with open("todo.txt","r") as f:
        d = f.readlines()
        count=len(d)
        for i in d[::-1]:
            print("[%s]"%(count),i.strip('\n'))
            count-=1
    f.close()

def printD():
    with open("done.txt",'r') as f:
        d = f.readlines()
        count=1
        for i in d:
            print("[%s]"%(count),i.strip('\n'))
            count+=1
    f.close()

def addD(s):
    date = datetime.date.today()
    with open("done.txt",'a') as f:
        # f.seek(2)
        f.write('x'+' '+str(date)+' '+s)
    f.close()

def done(l):
    with open("todo.txt","r+") as f:
        d = f.readlines()
        if len(d)<l:
            print("Error todo #%s does not exist. Nothing deleted."%(l))
            f.close()
            return
        f.seek(0)
        for i,j in enumerate(d):
            if i!=l-1:
            # if i.strip('\n')!=ltr:
                f.write(j)
            else:
                temp = j
                addD(temp)
        f.truncate()
    f.close()
    print("Marked todo #%s as done."%(l))

def delete(l):
    with open("todo.txt","r+") as f:
        d = f.readlines()
        if len(d)<l:
            print("Error todo #%s does not exist. Nothing deleted."%(l))
            f.close()
            return
        f.seek(0)
        for i,j in enumerate(d):
            if i!=l-1:
                f.write(j)
        f.truncate()
    f.close()
    print("Deleted todo #%s"%(l))

def addTD(s):
    with open("todo.txt",'a') as f:
        f.write(s+'\n')
    f.close()
    print("Added todo: \"%s\""%(s))

def report():
    date = datetime.date.today()
    with open("todo.txt",'r') as f:
        l = f.readlines()
        pending = len(l)
    f.close()
    with open("done.txt",'r') as f:
        l = f.readlines()
        done = len(l)
    f.close()
    print(date,"Pending : %s Completed : %s"%(pending,done))

def help():
    print('''Usage :-
$ ./todo add "todo item"  # Add a new todo
$ ./todo ls               # Show remaining todos
$ ./todo del NUMBER       # Delete a todo
$ ./todo done NUMBER      # Complete a todo
$ ./todo help             # Show usage
$ ./todo report           # Statistics''')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation',nargs='?',default='help')
    parser.add_argument('work',nargs='?',default='')
    args = parser.parse_args()
    o = args.operation
    if o=='add':
        addTD(args.work)
    elif o=='done':
        done(int(args.work))
    elif o=='del':
        delete(int(args.work))
    elif o=='report':
        report()
    elif o=='help':
        help()
    elif o=='ls':
        printTD()
    else:
        sys.stdout.write("Something went wrong")

if __name__=="__main__":
    main()