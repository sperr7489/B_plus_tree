# -*- coding: utf-8 -*-
from __future__ import print_function

import math
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
        self.prevNode = None


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
                # print("??")
                self.root = node

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
                    # print("이부분을 읽는지 검사해보자!")
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
                    # print("{}: 12을 입력했을때 부모노드가 이상해".format(node.parent.keys))
                    # print(node.keys)

                    # print("이 else를 읽는지 검사해보자!")

                    # parent에게 키값을 전달하기 전에는 그IN전의 subTree로
                    # 9->9,11로 바뀌어야 한다.
                    # print("{} :이것이 내가 알고 싶은 노드의 추가되기 전단계".format(node.parent.keys))
                    node.parent.keys.append(temp.keys[0])
                    # print("{} :이것이 내가 알고 싶은 노드".format(node.parent.keys))
                    node.parent.subTrees.append(temp)
                    node.parent.subTrees.sort()
                    # 원래 존재하던 parent에 key값을 넣어 주었다.
                    node.parent.keys.sort()

                    # leaf node에서 분할 되어 parent로 key를 추가할 때 생기는 일.
                    # 기존에 있던 subTree가 바뀌게 되겠지?
                    self.split(node.parent)

            elif node.isLeaf == False:
                # leaf node가 아니라 index node일때,혹은 root node.
                # INDEX노드가 나눠질땐 subtree에 대한 처리도 따로 해주어야만 함.
                temp = Node()  # 분할할 노드
                temp.isLeaf = False
                up_to_parentKey = node.keys[mid]

                if node.parent is None:  # parent가 생기고 이는 root가 되겠지?
                    node.parent = Node()
                    node.parent.isLeaf = False
                    temp.parent = node.parent
                    self.root = node.parent
                    node.parent.subTrees = [node, temp]

                    node.parent.keys.append(up_to_parentKey)
                    # 여기까지 되면 parent를 만들긴함.root노드 생성
                    # 기존 서브트리가 있긴했다!
                    # 아직 분할을 하지도 않았다!!
                    self.subTree(node, temp, mid)
                else:
                    # 일단 여기는 insert 10이 되면 하자
                    # 왜 여기를 안읽지?!!?
                    temp.parent = node.parent
                    node.parent.keys.append(up_to_parentKey)
                    node.parent.keys.sort()
                    self.subTree(node, temp, mid)

                    node.parent.subTrees.append(temp)
                    node.parent.subTrees.sort()
                    # node.parent.subTrees.append(temp)
                    # node.parent.subTrees.sort()
                    self.split(node.parent)  # 재귀.
        return

    def subTree(self, node, temp, mid):  # node가 앞쪽 temp가 뒤쪽으로 분할되는것
        # split 시에 subTree를 만드는 과정.
        # leaf node일 경우에
        # 이둘은 자동완성을 위해 써둔것 후에 지울것임
        # 분할은 무조건 둘로 나뉨!! 그때 앞부분에 대한 subtree와 뒷부분에 대한 subtree를 정해주면 됨!
        # 여기서 node는 leaf노드 바로 위에 있는 인덱스 노드
        if node.subTrees[0].isLeaf == True:
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
            print("subtree 여기를 지나는 지 확인해보기 special!!")

            for i, elem in enumerate(node.subTrees):
                # subtree가 isleaf이기때문에 등호가 존재.
                if elem.keys[0] > node.keys[mid]:
                    # 처음으로 커지는 순간을 기준으로 나누면 된다!!
                    index = i
                    # 여기서 index는 2가 된다. mid는 여기서 1이다.
                    break
            temp.keys = node.keys[mid+1:]
            node.keys = node.keys[:mid]

            temp.subTrees = node.subTrees[index:]
            node.subTrees = node.subTrees[:index]

            for i in temp.subTrees:
                i.parent = temp

    def search_node(self, k):

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
        current_node = self.search_node(k)
        current_node.keys.append(k)
        current_node.keys.sort()
        # 선택된 node에 대한 분할 과정 여부를 판단하고 진행한다.
        self.split(current_node)
        # print("이것이 현재 노드의 key들 : {}".format(current_node.keys))
        # self.print_all(self.root)
        # self.temp_all(self.root)
        # self.print_leaf()

# leaf에서 prev_node를 만들기 위한 함수
    def make_prev(self):
        cur_node = self.root
        flag = 0
        while cur_node.isLeaf == False:
            cur_node = cur_node.subTrees[0]
            flag = 1  # 한번이라도 바꼈다면 node가 root 노드만 있는것이 아님.
        # leaf의 첫번째까지 옴.

        if flag != 0:
            prev_node = cur_node
            cur_node = cur_node.nextNode

            while cur_nod is not None:
                cur_node.prevNode = prev_node
                cur_node = cur_node.nextNode
                prev_node = prev_node.nextNode
            cur_node.prevNode = prev_node

    def search_key(self, k, flag):
        head_node = self.root
        while head_node.isLeaf == False:
            # 만약 자식이 존재한다면?
            head_node = head_node.subTrees[0]

        while head_node.nextNode is not None:
            for key in head_node.keys:
                if key == k:
                    flag = 1  # 해당 key값이 있다는 것을 뜻한다.
                    return head_node
            head_node = head_node.nextNode
        # 여기까지 온거면 마지막 node를 가리킨다는 뜻이다.
        for key in head_node.keys:
            if key == k:
                flag = 1
                return head_node
        flag = 0
        return flag  # 0을 반환함으로써 해당 키가 없다는 것을 의미한다.

    def search_indexNode(self, k, index):
        # index node 찾기
        cur_node = self.root
        flag = 0
        for i, elem in enumerate(cur_node.keys):
            # 우선 root 부터 검사한다.
            if elem == k:
                index = i
                return [cur_node, index]
        while cur_node.isLeaf == False:
            # 현재 노드가 leaf가 아닐 때에만!
            for i, elem in enumerate(cur_node.keys):
                if k < elem:
                    cur_node = cur_node.subTrees[i]
                    flag = 1
                    break
                elif k == elem:
                    index = i  # 이것은 그 노드에서 그 k값이 몇번째인지 알려주기 위함.
                    return [cur_node, index]
            if flag == 0:
                cur_node = cur_node.subTrees[-1]

    def delete(self, k):
        self.make_prev()
        # 루트노드를 제외한 노드에 최소 key 갯수.
        min_num = int(math.ceil(float(self.order)/2)-1)
        flag = 0
        merge_point = 0
        # 성공적으로 반환되었다면 해당 leaf node가 반환되었을 터이다.
        cur_node = self.search_key(k, flag)
        if cur_node == 0:
            print("해당 키값은 존재하지 않는다. ")
        # else:
            # 여기서부터 delete에 대한 과정을 시작하면된다.
            # 해당 key가 leaf_node에만 존재하는 경우.
        elif cur_node == self.root:
            # 만약 leaf node 자체가 root라면 그냥 단순히 삭제해도 괜찮겠지!
            cur_node.keys.remove(k)
            return
        elif self.check_only_leaf(cur_node, k) == 0:
            # print("그럼 여기는?")
            # print(min_num)
            # k가 leaf node에만 존재하는 경우!
            if len(cur_node.keys) > min_num:
                cur_node.keys.remove(k)
            elif len(cur_node.keys) == min_num:
                # 지우려고 하는 key의 갯수가 최소 갯수만큼이면 지웠을 때 문제가 생기므로
                # borrow를 하든 merge를 하든 해야한다.
                # 이는 단순히 borrow의 방향을 결정짓는 것뿐
                if cur_node == cur_node.parent.subTrees[0]:
                    # 해당 부모노드의 자식중 첫번째라면 오른쪽에서 가져온다.
                    cur_node.keys.remove(k)  # 우선 지워준다.
                    # 지우고 무조건 최소갯수보다 적어지겠지? 이 조건문의 조건절을 보면 확인 가능
                    # merge 혹은 borrow상황이 발생한다.
                    # borrow시 문제가 발생하는지 안하는지 판단
                    if len(cur_node.nextNode.keys) == min_num:
                        # 그럼 borrow했을 때도 문제가 발생
                        # print("merge를 해야함")
                        tmp = cur_node.nextNode.keys[0]
                        cur_node.nextNode.keys += cur_node.keys
                        cur_node.nextNode.keys.sort()
                        cur_node.parent.subTrees.remove(cur_node)
                        cur_node.nextNode.prevNode = None
                        for i, key in enumerate(cur_node.parent.keys):
                            if key == tmp:
                                cur_node.nextNode.parent.keys.remove(key)
                                if cur_node.nextNode.parent == self.root:
                                    if len(cur_node.nextNode.parent.keys) == 0:
                                        self.root = cur_node.nextNode
                                        self.root.isLeaf = True
                                        #
                                break

                    elif len(cur_node.nextNode.keys) > min_num:
                        cur_node.keys.append(cur_node.nextNode.keys[0])
                        # borrow를 일단 함.
                        for i, key in enumerate(cur_node.parent.keys):
                            if key == cur_node.nextNode.keys[0]:
                                cur_node.parent.keys[i] = cur_node.nextNode.keys[1]
                                del cur_node.nextNode.keys[0]
                                break
                        # print("borrow만 해도됨")
                else:  # 단순히 여기선 오른쪽 왼쪽 노드로부터!
                    cur_node.keys.remove(k)  # 우선 지워준다.
                    if len(cur_node.prevNode.keys) == min_num:
                        if(cur_node.nextNode is not None):
                            # 왼쪽 노드에서 가져오는 건 문제가 발생한다. 그럼 다음 노드에서 가져온다면?
                            # 지금 여긴 prev,next 모두에서 문제가 발생하는 경우다.
                            # 그럴땐 그냥 왼쪽에서 처리를 해준다.
                            if len(cur_node.nextNode.keys) > min_num:
                                # print("오른쪽에서 borrow를 해준다.")
                                cur_node.keys.append(cur_node.nextNode.keys[0])
                                # borrow를 일단 함.
                                for i, key in enumerate(cur_node.parent.keys):
                                    if key == cur_node.nextNode.keys[0]:
                                        cur_node.parent.keys[i] = cur_node.nextNode.keys[1]
                                        del cur_node.nextNode.keys[0]
                                        break
                                return
                        # 그럼 오른쪽에서 borrow했을 때도 문제가 발생
                        # 부모의 첫번째 자식이 아닐경우 무조건 merge는 왼쪽과 일어남.
                        # print("왼쪽에서 merge를 해야함")
                        tmp = cur_node.keys[0]
                        node = cur_node.prevNode
                        node.keys += cur_node.keys
                        node.parent.subTrees.remove(cur_node)
                        node.nextNode = cur_node.nextNode
                        for i, key in enumerate(node.parent.keys):
                            if tmp == key:
                                cur_node.prevNode.parent.keys.remove(key)
                                # 삭제할 때 문제가 발생할 수 있음.
                                if cur_node.prevNode.parent == self.root:
                                    if len(cur_node.prevNode.parent.keys) == 0:
                                        self.root = cur_node.prevNode
                                        self.root.isLeaf = True

                                break
                        return

                    elif len(cur_node.prevNode.keys) > min_num:
                        # print("왼쪽에서 borrow만 해도됨")
                        key = cur_node.prevNode.keys[-1]
                        cur_node.keys.append(key)
                        cur_node.keys.sort()
                        # print(cur_node.prevNode.keys[-1])
                        # print(cur_node.keys)
                        for i, key in enumerate(cur_node.parent.keys):
                            if key == cur_node.keys[1]:
                                cur_node.parent.keys[i] = cur_node.keys[0]
                                del cur_node.prevNode.keys[-1]
                                break

        elif self.check_only_leaf(cur_node, k) == 1:
            # k가 index node에도 존재하는 경우라면?
            index = 0
            if len(cur_node.keys) > min_num:
                # 현재 노드가 index 노드에 있는데 그 현재노드의 키 갯수가 최소값보다 많을 경우엔
                # 그 key값을 지우고 그 인덱스에 그 key값 다음에 있는것을 넣으면 된다.
                # changed_key는 index가 바뀌게 될 값이다.
                changed_key = cur_node.keys[1]
                cur_node.keys.remove(k)  # 우선 지워준다.
                index_node = self.search_indexNode(k, index)[0]
                index = self.search_indexNode(k, index)[1]
                index_node.keys[index] = changed_key
            elif len(cur_node.keys) == min_num:
                # 지우려고하는 key의 Node가 최소 갯수일때 그냥 지우면 클남!!
                if cur_node == cur_node.parent.subTrees[0]:
                    # 해당 부모노드의 자식중 첫번째라면 next노드로 처리해준다.
                    cur_node.keys.remove(k)  # 우선 지워준다.
                    # print("index node까지 처리를 해주어야 한다는 게 중요하다. ")
                    if len(cur_node.nextNode.keys) == min_num:
                        # 그럼 borrow했을 때도 문제가 발생
                        # print("merge를 해야함")
                        changed_key = cur_node.nextNode.keys[0]
                        index_node = self.search_indexNode(k, index)[0]
                        index = self.search_indexNode(k, index)[1]
                        cur_node.keys += cur_node.nextNode.keys
                        # 이부분 잘봐야한다.
                        cur_node.parent.subTrees.remove(cur_node.nextNode)
                        cur_node.nextNode = cur_node.nextNode.nextNode
                        for i, key in enumerate(cur_node.parent.keys):
                            if key == changed_key:
                                cur_node.nextNode.parent.keys.remove(key)
                                break
                        index_node.keys[index] = changed_key
                    elif len(cur_node.nextNode.keys) > min_num:
                        # print("오른쪽에서 borrow만 해도됨")
                        changed_key = cur_node.nextNode.keys[0]
                        index_node = self.search_indexNode(k, index)[0]
                        index = self.search_indexNode(k, index)[1]
                        # index가 어디에서 대응되는 지에 대한 노드
                        cur_node.keys.append(cur_node.nextNode.keys[0])

                        for i, key in enumerate(cur_node.parent.keys):
                            if key == cur_node.nextNode.keys[0]:
                                cur_node.parent.keys[i] = cur_node.nextNode.keys[1]
                                del cur_node.nextNode.keys[0]
                                break
                        index_node.keys[index] = changed_key

                else:  # subTree의 첫번째가 아니고 index_node를 건들때
                    # print("index node까지 처리를 해주어야 한다는 게 중요하다. ")
                    cur_node.keys.remove(k)  # 우선 지워준다.
                    if len(cur_node.prevNode.keys) == min_num:
                        if(cur_node.nextNode is not None):
                            # 왼쪽 노드에서 가져오는 건 문제가 발생한다. 그럼 다음 노드에서 가져온다면?
                            # 지금 여긴 prev,next 모두에서 문제가 발생하는 경우다.
                            # 그럴땐 그냥 왼쪽에서 처리를 해준다.
                            if len(cur_node.nextNode.keys) > min_num:
                                # print("오른쪽에서 borrow를 해준다.")
                                # print(cur_node.keys)

                                changed_key = cur_node.nextNode.keys[0]
                                index_node = self.search_indexNode(k, index)[0]
                                index = self.search_indexNode(k, index)[1]
                                index_node.keys[index] = changed_key
                                # print(index_node.keys)
                                cur_node.keys.append(changed_key)
                                cur_node.nextNode.keys.remove(changed_key)

                                cur_node.parent.keys[index +
                                                     1] = cur_node.nextNode.keys[0]

                                return
                        # 그럼 오른쪽에서 borrow했을 때도 문제가 발생
                        # 부모의 첫번째 자식이 아닐경우 무조건 merge는 왼쪽과 일어남.
                        # print("왼쪽에서 merge를 해야함")
                        changed_key = cur_node.prevNode.keys[-1]
                        index_node = self.search_indexNode(k, index)[0]
                        index = self.search_indexNode(k, index)[1]
                        del index_node.keys[index]
                        cur_node.parent.subTrees.remove(cur_node)
                        cur_node.prevNode.nextNode = cur_node.nextNode
                        cur_node.prevNode.keys += cur_node.keys

                    elif len(cur_node.prevNode.keys) > min_num:
                        # print("왼쪽에서 borrow만 해도됨")
                        changed_key = cur_node.prevNode.keys[-1]
                        index_node = self.search_indexNode(k, index)[0]
                        index = self.search_indexNode(k, index)[1]
                        cur_node.keys.append(changed_key)
                        cur_node.keys.sort()
                        index_node.keys[index] = changed_key
                        cur_node.prevNode.keys.remove(changed_key)

    def check_only_leaf(self, node, k):
        # node 자체가 root일 것은 생각안해도됨. 그건 이미 걸렀음.
        ret = 0
        while node != self.root:
            for i in node.parent.keys:
                if i == k:
                    # index 노드에도 존재한다.
                    ret = 1
                    return ret
            node = node.parent
        ret = 0  # leaf node에만 존재한다는 뜻이다.
        return ret

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
        if self.root.isLeaf == True:
            print(self.root.keys)
        elif node.isLeaf == False:
            # root 노드가 자식이 있을 때
            print(node.keys, end="-")
            for i in node.subTrees:
                if i == node.subTrees[-1]:
                    print(i.keys)
                else:
                    print(i.keys, end=",")
            for i in node.subTrees:
                self.print_all(i)

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

    # def print_T(self, node):
    #     while node.isLeaf == False:
    #         # 들어온 노드가 leaf node가 아니라면?
    #         print(node.keys, end="-")
    #         for i, elem in enumerate(node.subTrees):
    #             if i+1 == len(node.subTrees):
    #                 print(elem.keys)
    #             else:
    #                 print(elem.keys, end=",")
    #             node = elem

    def print_tree(self):
        # self.print_all(self.root)
        self.temp_all(self.root)
        pass

    def find_range(self, k_from, k_to):
        cur_node = self.root
        while cur_node.isLeaf == False:
            cur_node = cur_node.subTrees[0]
        # 조건문이 끝나면 cur_node는 가장 앞에 있는 node이다.
        while cur_node.nextNode is not None:
            for i in cur_node.keys:
                if i >= k_from and i < k_to:
                    print(i, end=",")
                elif i == k_to:
                    print(i)
                    return
            cur_node = cur_node.nextNode
        # 조건문을 빠져나왔을 땐 마지막 노드가 되어 있을 것이다.
        for i in cur_node.keys:
            if i >= k_from and i < k_to:
                print(i, end=",")
            elif i == k_to:
                print(i)
                return

    def find(self, k):
        flag = 0
        if self.search_key(k, flag) == 0:
            print("NONE")
            return

        if self.root.isLeaf == True:
            for i in self.root:
                if i == k:
                    print(self.root.keys)
                    return
        current_node = self.root
        # print(current_node.keys)
        # 현재 노드가 child가 있다면 아래로 내려가야겠고
        # 없다면 leafnode라는 뜻이겠지.
        while current_node.isLeaf == False:
            # 만약 현재 node의 자식이 있다면?
            print(current_node.keys, end="-")
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
        print(current_node.keys)


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
