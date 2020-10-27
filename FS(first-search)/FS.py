from queue import Queue
from dataform import arr3, arr5, arr7, graph
from pprint import pprint

# 깊이 우선 탐색
def DFS(graph, start_node):
    visit = dict()
    stack = list()

    stack.append(start_node)
    count = 0
    while stack:
        node = stack.pop()
        if node not in visit:
            visit[node] = True
            stack.extend(graph[node])
            count += 1

            print(f'결과{count} : {visit}\n{stack}\n')

    return list(visit.keys())

# 넓이 우선 탐색
def BFS(graph, start_node):
    visit = dict()
    queue = Queue()

    queue.put(start_node)
    count = 0
    while queue.qsize() > 0:
        node = queue.get()
        if node not in visit:
            visit[node] = True
            for nextNode in graph[node]:
                queue.put(nextNode)
            count += 1

            print(f'결과{count} : {visit}\n{queue}\n')

    return list(visit.keys())

# 주변 우선 탐색
class AFS():
    # FS 우선 탐색 알고리즘 인풋 데이터
    tree = dict()
    # 확인해야하는 좌표
    queue = Queue()
    # 확인한 좌표
    checking = list()

    def __init__(self, arr, x, y):
        self.arr = arr
        self.setStart_node(x, y)
        self.findFirst(x, y)

    # 결과 트리, 확인 상태 반환
    def getTree(self):
        return self.tree, self.arr

    # 좌표 주변 8칸 찾기
    def cal(self, num):
        return [num-1, num, num+1]

    # 좌표 주변 8칸 찾기
    # around : 주변 8칸
    # self.queue : 확인해야하는 좌표들
    def getAround(self, x, y):
        around = set()
        for getY in self.cal(y):
            for getX in self.cal(x):
                if self.x_leng > getX >= 0 <= getY < self.y_leng and (getX, getY) != (x, y):
                    cdn = (getX, getY)
                    if cdn not in self.checking and cdn not in self.tree:
                        self.checking.append(cdn)
                        around.add(cdn)
                        self.queue.put(cdn)

        return around

    # 큐의 데이터가 있으면 받아서 루프 실행
    def checkQueue(self):
        while self.queue.qsize() > 0:
            new_x, new_y = self.queue.get()
            return self.findLoop(new_x, new_y)

    # self.queue의 좌표를 통한 항목 반복 확인
    def findLoop(self, x, y):
        if (x, y) not in self.tree:
            self.tree[(x, y)] = self.getAround(x, y)
            self.arr[y][x] = True
            self.checkQueue()
        else:
            self.checkQueue()

    # self.start_node 좌표를 통한 첫 번째 항목 확인
    def findFirst(self, x, y):
        self.tree[(x, y)] = self.getAround(x, y)
        self.arr[y][x] = True

        new_x, new_y = self.queue.get()
        self.findLoop(new_x, new_y)

    # 행렬 길이 반환
    def getLeng(self):
        return len(self.arr[0]), len(self.arr)

    # 시작 노드 지정
    def setStart_node(self, x, y):
        self.x_leng, self.y_leng = self.getLeng()
        if self.x_leng >= x and self.y_leng >= y:
            self.start_node = (x, y)

if __name__ == '__main__':
    # print(DFS(graph, 'A'))
    mt = AFS(arr5, 0, 0)
    tree, arr = mt.getTree()
    pprint(arr)
    print()
    pprint(tree)