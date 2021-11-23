# -*- coding: utf-8 -*-
import sys


class Node:
    def __init__(self):
        # each node can have |order - 1| keys
        self.keys = []
        # |order| / 2 <= # of subTree pointers <= |order|
        self.subTrees = []
        self.parent = None
        self.isLeaf = True
        # leaf node has next node pointer
        self.nextNode = None


class B_PLUS_TREE:
    # Init함수는 객체가 생성될 때만 호출된다. 메인함수를 보면 init에만 호출됨을 확인할 수 있다.
    def __init__(self, order):
        # 차수를 정한다
        self.order = order
        self.root = Node()
        self.root.isLeaf = True  # 처음 초기화 될때는 true가 되어야겠지?

        pass

    # split 함수는 분할 가능성과 root를 알려준다.
    def split(self, node):
        if len(node.keys) <= self.order-1:
            # 이경우엔 split할 필요가 없다.
            if(node.parent is None):
                # parent가 없다면 root겠지?
                self.root = node
                print("root되었니?")

        elif len(node.keys) > self.order-1:
            # 여기서는 이제 split을 해주어야 한다.두개의 노드와 하나의
            # 이부분이 leaf node에 대한 것이라면
            node_Check = node
            if (node.isLeaf == True):
                # leaf node일때는 이제 선형 탐색이 가능해지자나? 정렬이 되어있는 상태지!
                mid = self.order/2
                temp = Node()  # 분할할 노드
                temp.keys = node.keys[mid:]  # 이부분은 뒤에꺼로
                node.keys = node.keys[:mid]  # 이부분은 앞에껄로
                node.nextNode = temp  # 이걸로 leaf node의 분할은 끝!
                if node.parent is None:  # parent가 없던 상태에서 생긴거면 root가 바뀐거겠지?
                    node.parent = Node()
                    temp.parent = node.parent
                    node.parent.isLeaf = False
                    node.parent.keys.append(temp.keys[0])
                    self.root = node.parent  # root를 여기서 변경하여 준다.
                    print(node.parent.keys)
                    print("자 root가 바뀌었니?")
                    # 앞에꺼와 뒤에꺼 subtree로 추가
                    node.parent.subTrees += [node, temp]
                elif node.parent is not None:
                    # parent가 이미 있다면
                    node.parent.keys.append(temp.keys[0])
                    print("추가가 되었는지 확인")
                    node.parent.keys.sort()
                    self.split(node.parent)
                    for element in node.parent.subTrees:
                        if(element == node_Check):  # parent의 서브트리를 수정하기 위해.
                            node.parent.subTrees.remove(element)
                            node.parent.subTrees += [node, temp]
                            node.parent.subTrees.sort()
                            break

            else:
                # leaf node가 아니라 index node일때,혹은 root node.
                mid = self.order/2
                temp = Node()  # 분할할 노드
                temp.keys = node.keys[mid:]  # 이부분은 뒤에꺼로
                node.keys = node.keys[:mid]  # 이부분은 앞에껄로
                if node.parent is None:  # parent가 생기고 이는 root가 되겠지?
                    node.parent = Node()
                    temp.parent = node.parent
                    node.parent.isLeaf = False
                    self.root = node.parent
                    node.parent.keys.append(temp.keys[0])
                    # 앞에꺼와 뒤에꺼 subtree로 추가
                    node.parent.subTrees += [node, temp]
                else:
                    node.parent.keys.append(temp.keys[0])
                    node.parent.keys.sort()
                    self.split(node.parent)  # 재귀.
                    for element in node.parent.subTrees:
                        if(element == node_Check):  # parent의 서브트리를 수정하기 위해.
                            node.parent.subTrees.remove(element)
                            node.parent.subTrees += [node, temp]
                            node.parent.subTrees.sort()
                            break
        return

    def search(self, k):
        current_node = self.root
        # 현재 노드가 child가 있다면 아래로 내려가야겠고
        # 없다면 leafnode라는 뜻이겠지.
        while current_node.isLeaf == False:
            # 만약 현재 node의 자식이 있다면?
            temp_key = current_node.keys
            for i, elem in enumerate(temp_key):
                if k < elem:
                    current_node = current_node.subTrees[i]
                    break
                elif k >= elem:
                    if (i+1 == len(current_node.keys)):
                        current_node = current_node.subTrees[i+1]
                        break
                    continue
        return current_node

    def insert(self, k):
        current_node = self.search(k)
        current_node.keys.append(k)
        current_node.keys.sort()
        self.split(current_node)

    def delete(self, k):
        pass

    def print_root(self):
        # l = "["
        # for k in self.root.keys:
        #     l += "{},".format(k)
        # l = l[:-1] + "]"
        # print(l)
        print(self.root.keys)
        pass

    def print_tree(self):
        pass

    def find_range(self, k_from, k_to):
        pass

    def find(self, k):

        pass


def main():
    myTree = None

    while (True):
        comm = sys.stdin.readline()
        comm = comm.replace("\n", "")
        params = comm.split()
        if len(params) < 1:
            continue

        print(comm)

        if params[0] == "INIT":
            order = int(params[1])
            myTree = B_PLUS_TREE(order)

        elif params[0] == "EXIT":
            return

        elif params[0] == "INSERT":
            k = int(params[1])
            myTree.insert(k)

        elif params[0] == "DELETE":
            k = int(params[1])
            myTree.delete(k)

        elif params[0] == "ROOT":
            myTree.print_root()

        elif params[0] == "PRINT":
            myTree.print_tree()

        elif params[0] == "FIND":
            k = int(params[1])
            myTree.find(k)

        elif params[0] == "RANGE":
            k_from = int(params[1])
            k_to = int(params[2])
            myTree.find_range(k_from, k_to)

        elif params[0] == "SEP":
            print("-------------------------")


if __name__ == "__main__":
    main()
