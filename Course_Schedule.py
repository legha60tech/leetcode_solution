from collections import deque,defaultdict
import ast
def canFinish(numCourses, prerequisites):
    g, indeg = defaultdict(list), [0]*numCourses
    for a,b in prerequisites:
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(numCourses) if indeg[i] == 0])
    cnt = 0
    while q:
        x = q.popleft()
        cnt += 1
        for y in g[x]:
            indeg[y] -= 1
            if indeg[y] == 0:
                q.append(y)
    return cnt == numCourses
numCourses = int(input("Enter number of course: "))
prereq_input = input("enter prerequisites as pairs, eg:[[1,0],[0,]]: ")
prerequisites = ast.literal_eval(prereq_input)
if canFinish(numCourses,prerequisites):
    print("true")
else:
    print("false")
