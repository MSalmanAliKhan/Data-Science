# Read from a file and Write part of it in another file.
with open("Chapter 19 Exercise 1 Read File.txt","r") as rf:
    with open("Chapter 19 Exercise 1 Write File.txt","w") as wf:
        for line in rf.readlines():
            name,salary = line.split(",")
            wf.write(f"{name} has a salary of {salary}")
wf.close()
rf.close()