#Trie에 사용할 Node Class 직접 정의.
class Node:
    def __init__(self):

        self.child = {} #Hash map을 통하여 child 노드 관리

        self.is_end = False

class Trie:

    def __init__(self):
        self.root = Node() #root를 지정하여 언제든 조회를 위하여 초기화 할 수 있게 설정

    def insert(self, word: str) -> None:
        current_node = self.root
        for char in word:
            if char not in current_node.child: #Hashmap에서 in 을 통한 확인은 O(1)이다.
                current_node.child[char] = Node() #존재하지 않는다면 Hashmap과 위에서 정의한 노드를 활용하여 생성
            current_node = current_node.child[char] #만들어진 혹은 존재하는 다음 자식으로 이동
        current_node.is_end = True #마지막에 도달하면 is_end를 True로 바꾸고 마무리

    def search(self, word: str) -> bool:
        current_node = self.root
        for char in word:
            if char not in current_node.child: #Hashmap에서 in을 사용한 방법은 위와 동일하지만 요소가 없으면 바로 False를 return.
                return False
            current_node = current_node.child[char] #False가 return 되지 않았다면, 즉 존재했다면 다음 자식으로 이동.
        return current_node.is_end #지정한 단어의 끝까지 도달했으며, 그 단어의 끝이 실제 마지막 노드인지 확인하기 위하여 is_end로 반환.

    def startsWith(self, prefix: str) -> bool:
        current_node = self.root
        for char in prefix:
            if char not in current_node.child:
                return False
            current_node = current_node.child[char]
        return True #전반적인 작동은 search와 유사하나 단어의 끝이 실제 마지막노드일 필요가 없으니 바로 True를 반환.
