# -*- coding: utf-8 -*-
import sys
import copy


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
    # not leaf node에서 분할 시 subtree를 재수정해주어야한다.
    # split 함수는 분할 가능성과 root를 알려준다.

    def split(self, node):
        if len(node.keys) < self.order:
            # 이경우엔 split할 필요가 없다.
            if node.parent is None:
                # parent가 없다면 root겠지?
                print("??")
                self.root = node
            else:
                print("{}: 11입력했을 때 부모노드 뭔데".format(node.parent.keys))

    # 분할이 일어나는 시점.
        elif len(node.keys) == self.order:
            mid = self.order/2

            # 여기서는 이제 split을 해주어야 한다.두개의 노드와 하나의
            # 이부분이 leaf node에 대한 것이라면
            # 이건 말이 안돼! 이미 바뀐 노드가 들어왔는데 node가 같은게 왜있음!
            if (node.isLeaf == True):
                # leaf node일때는 이제 선형 탐색이 가능해지자나? 정렬이 되어있는 상태지!
                temp = Node()  # 분할할 노드
                temp.keys = node.keys[mid:]  # 이부분은 뒤에꺼로
                node.keys = node.keys[:mid]  # 이부분은 앞에껄로
                # node의 nextnode가 존재하는 상황일때
                if node.nextNode is not None:
                    temp.nextNode = node.nextNode
                node.nextNode = temp  # 이걸로 leaf node의 분할은 끝!
                # MEMORY 위치가 같아진다.
                if node.parent is None:  # parent가 없던 상태에서 생긴거면 root가 바뀐거겠지?
                    print("이부분을 읽는지 검사해보자!")
                    node.parent = Node()
                    temp.parent = node.parent

                    node.parent.isLeaf = False
                    node.parent.keys.append(temp.keys[0])
                    self.root = node.parent  # root를 여기서 변경하여 준다.
                    # 앞에꺼와 뒤에꺼 subtree로 추가
                    # 새로 생긴 parent이기 때문에 subtree들의 정렬은 따로 해주지 않아도 된다.
                    node.parent.subTrees = [node, temp]
                else:
                    # isleaf에서 parent가 있다면 추가를 어떻게 해주어야 할까?
                    # parent가 이미 있다면

                    temp.parent = node.parent
                    print("{}: 12을 입력했을때 부모노드가 이상해".format(node.parent.keys))
                    print(node.keys)

                    print("이 else를 읽는지 검사해보자!")

                    # parent에게 키값을 전달하기 전에는 그IN전의 subTree로
                    # 9->9,11로 바뀌어야 한다.
                    print("{} :이것이 내가 알고 싶은 노드의 추가되기 전단계".format(node.parent.keys))
                    node.parent.keys.append(temp.keys[0])
                    print("{} :이것이 내가 알고 싶은 노드".format(node.parent.keys))
                    node.parent.subTrees.append(temp)
                    node.parent.subTrees.sort()
                    # 원래 존재하던 parent에 key값을 넣어 주었다.
                    node.parent.keys.sort()

                    # leaf node에서 분할 되어 parent로 key를 추가할 때 생기는 일.
                    # 기존에 있던 subTree가 바뀌게 되겠지?
                    print("여기를 지날까?재귀부분")
                    self.split(node.parent)

            elif node.isLeaf == False:
                # leaf node가 아니라 index node일때,혹은 root node.
                # INDEX노드가 나눠질땐 subtree에 대한 처리도 따로 해주어야만 함.
                temp = Node()  # 분할할 노드
                temp.isLeaf = False
                up_to_parentKey = node.keys[mid]

                if node.parent is None:  # parent가 생기고 이는 root가 되겠지?
                    print("여기 읽겠지?")
                    node.parent = Node()
                    node.parent.isLeaf = False
                    temp.parent = node.parent
                    node.parent.subTrees = [node, temp]
                    self.root = node.parent
                    node.parent.keys.append(up_to_parentKey)
                    # 여기까지 되면 parent를 만들긴함.root노드 생성
                    # 기존 서브트리가 있긴했다!
                    # 아직 분할을 하지도 않았다!!

                    self.subTree(node, temp, mid)
                else:
                    # 일단 여기는 insert 10이 되면 하자
                    # 왜 여기를 안읽지?!!?
                    temp.parent = node.parent
                    print("여기 읽어?")
                    node.parent.keys.append(up_to_parentKey)
                    node.parent.subTrees.append(temp)
                    node.parent.subTrees.sort()
                    node.parent.keys.sort()
                    self.split(node.parent)  # 재귀.
        return

    def subTree(self, node, temp, mid):  # node가 앞쪽 temp가 뒤쪽으로 분할되는것
        # split 시에 subTree를 만드는 과정.
        # leaf node일 경우에
        # 이둘은 자동완성을 위해 써둔것 후에 지울것임
        # 분할은 무조건 둘로 나뉨!! 그때 앞부분에 대한 subtree와 뒷부분에 대한 subtree를 정해주면 됨!
        print("여기는 들어오ㅓ나?")
        # 여기서 node는 leaf노드 바로 위에 있는 인덱스 노드
        if node.subTrees[0].isLeaf == True:
            print("subtree 여기를 지나는 지 확인해보기")
            # node.keys[mid] 이것이 빠져나갈 노드겠지?
            # node.keys[mid-1]이 분할되는 key의 바로 직전 key값!

            for i, elem in enumerate(node.subTrees):
                if elem.keys[0] == node.keys[mid]:
                    # 이게 앞부분 노드가 가져가야할 subTree의 마지막 노드!
                    index = i
                    # index ==3 이 된다. 4번째라는뜻.
                    # mid는 현재 2이다.
                    break
            temp.keys = node.keys[mid+1:]
            node.keys = node.keys[:mid]

            temp.subTrees = node.subTrees[index:]
            node.subTrees = node.subTrees[:index]

            # 자식 노드 입장에서 parent를 다시 지정해줘야만 한다!
            for i in temp.subTrees:
                i.parent = temp

        else:
            print("subtree 여기를 지나는 지 확인해보기")

            for i, child in enumerate(node.subTrees):
                # subtree가 isleaf이기때문에 등호가 존재.
                if node.keys[mid+1] < child.keys[0]:
                    temp_subTrees = [node.subTrees[:i], node.subTrees[i:]]
                    # 이 지점을 기준으로 subtree를 나누면 된다.
                    temp.keys = node.keys[mid+1:]  # 이부분은 뒤에꺼로
                    node.keys = node.keys[:mid]  # 이부분은 앞에껄로
                    node.subTrees.clear()
                    node.subTrees = temp_subTrees[0]
                    temp.subTrees = temp_subTrees[1]

    def search(self, k):
        current_node = self.root
        # print(current_node.keys)
        # 현재 노드가 child가 있다면 아래로 내려가야겠고
        # 없다면 leafnode라는 뜻이겠지.
        while current_node.isLeaf == False:
            # 만약 현재 node의 자식이 있다면?
            flag = 0  # 마지막 노드를 가져오기 위한 과정.
            for i, elem in enumerate(current_node.keys):
                if k < elem:
                    current_node = current_node.subTrees[i]
                    # print(current_node.keys)
                    flag = 1
                    # print("다음꺼고름 ")
                    break
            if flag == 0:
                # print(current_node.subTrees)
                current_node = current_node.subTrees[-1]
                # print(current_node.keys)
        # print(current_node.keys)
        return current_node

    def insert(self, k):
        current_node = self.search(k)
        current_node.keys.append(k)
        current_node.keys.sort()
        # 선택된 node에 대한 분할 과정 여부를 판단하고 진행한다.
        self.split(current_node)
        # print("이것이 현재 노드의 key들 : {}".format(current_node.keys))
        # self.print_all(self.root)
        self.temp_all(self.root)
        # self.print_leaf()

    def delete(self, k):
        pass

    def print_root(self):
        l = "["
        for k in self.root.keys:
            l += "{},".format(k)
        l = l[:-1] + "]"
        print(l)
        pass

    def temp_all(self, node):
        if node.isLeaf == False:
            print(node.keys)
            print("subTree의 갯수 : {}".format(len(node.subTrees)))
            for index, i in enumerate(node.subTrees):
                self.temp_all(i)

        else:
            print(node.keys)

    def print_all(self, node):
        if node.isLeaf == False:
            # leaf node가 아닐때
            print(node.keys)
            for i, tmp in enumerate(node.subTrees):
                print(tmp.keys)
                print("-------------")
                if node.isLeaf == False:
                    node = node.subTrees[i]
                    self.print_all(node)
        else:
            print(node.keys)

    def print_leaf(self):
        current_node = self.root
        # if current_node == self.root:
        #     print(current_node.keys)
        # else:
        # current_node = Node()
        while current_node.isLeaf == False:
            current_node = current_node.subTrees[0]

        if current_node == self.root:
            print(current_node.keys)
        else:
            flag = 0
            while current_node.nextNode is not None:
                print(current_node.keys)
                current_node = current_node.nextNode
            print(current_node.keys)

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
