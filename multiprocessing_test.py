from multiprocessing import Pool

def job(num):
    return num * 2

if __name__ == '__main__':
    p = Pool(processes=20)
    data = p.map(job, range(20))
    p.close()
    print(data)


x = (i for i in range(5))
# we can manually move the selector
next(x)
next(x)
x.__next__()

for i in x:
    print(i)

print(dir(x))