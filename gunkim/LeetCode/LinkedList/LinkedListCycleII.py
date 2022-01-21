# LinkedList에서 순환하는 구간의 첫 시작 지점이 어디인지 반환해야 한다
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: # 순환이 된다면 이제 시작 지점을 찾아야 함
                slow = head # slow의 지점을 head로 초기화 후
                while slow != fast: # slow, fast 둘 다 +1 씩 이동을 하며 같아질때를 찾는다, 그때가 시작지점
                    slow = slow.next
                    fast = fast.next
                return slow