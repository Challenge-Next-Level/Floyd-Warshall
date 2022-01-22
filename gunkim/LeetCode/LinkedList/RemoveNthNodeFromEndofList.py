class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = slow = head
        # fast와 slow의 간격을 n만큼 벌리기 위해 하는 과정 <- best idea!!!
        for _ in range(n):
            fast = fast.next
        # 연결 리스트의 크기와 n이 같아 head를 delete하는 경우
        # head를 제외한 head.next 부터의 연결 리스트를 반환하면 된다
        if fast is None:
            return head.next
        # fast와 slow를 동시에 움직인다 (fast가 연결 리스트 끝까지 이동될 때 까지)
        while fast.next:
            fast = fast.next
            slow = slow.next
        # slow의 다음 node가 delete를 해야 될 node가 된다 (next를 변경한다)
        slow.next = slow.next.next
        return head