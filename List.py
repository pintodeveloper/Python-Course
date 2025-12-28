workers = ["Ana","Pinto","Coco77","Lorena"]

print(workers)

print(len(workers))

workers.append("Felipe77")

print(len(workers))


print(workers[2])

print(workers[-1])


newWorkers = ["Andry","Messi","CR7","Luiz Dias","James"]

workers.extend(newWorkers)


print(workers)

print(workers[2:6])



del workers[0] #Ana delete
workers.remove("James")


print(workers)


##to find the index of an element

print(workers.index("Messi"))

newWorkers1 = ["sister","Engineer","Pinto77","Pinto77","Pinto77"]
workers.extend(newWorkers1)


print(workers.count("Pinto77"))