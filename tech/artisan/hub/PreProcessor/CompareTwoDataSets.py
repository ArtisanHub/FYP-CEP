

file1 = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/full-game-test.txt'
file2 = '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/proccesed-full-game-test.txt'

with open(file1,"r") as f:
    t1 = f.read().splitlines()
    t1s = set(t1)

with open(file2,"r") as f:
    t2 = f.read().splitlines()
    t2s = set(t2)

#in file1 but not file2
print("Only in file1")
for diff in t1s-t2s:
    print(t1.index(diff), diff)

#in file2 but not file1
print("Only in file2")
for diff in t2s-t1s:
    print(t2.index(diff), diff)