# coding=utf-8

from commons.list_node import ListNode


class Solution(object):

    """
    21. 合并两个有序链表
    (https://leetcode-cn.com/problems/merge-two-sorted-lists/description/)

    将两个有序链表合并为一个新的有序链表并返回。
    新链表是通过拼接给定的两个链表的所有节点组成的。

    示例：

    输入：1->2->4, 1->3->4
    输出：1->1->2->3->4->4
    """

    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode(0)
        merge_listnode = root
        while l1:
            if l2 is not None:
                while l2:
                    if l1.val <= l2.val:
                        merge_listnode.next = l1
                        merge_listnode = merge_listnode.next
                        break
                    else:
                        merge_listnode.next = l2
                        merge_listnode = merge_listnode.next
                        l2 = l2.next

                if l2 is None:
                    merge_listnode.next = l1
                    merge_listnode = merge_listnode.next

            else:
                merge_listnode.next = l1
                merge_listnode = merge_listnode.next

            l1 = l1.next

        while l2:
            merge_listnode.next = l2
            merge_listnode = merge_listnode.next
            l2 = l2.next

        return root.next

    def mergeTwoListsForList(self, l1, l2):
        """
        :type l1: List
        :type l2: List
        :rtype: List
        """
        merge_nums = []
        one_nums, two_nums = l1, l2
        for one_num in one_nums:
            try:
                while True:
                    if one_num <= two_nums[0]:
                        merge_nums.append(one_num)
                        break
                    else:
                        merge_nums.append(two_nums.pop(0))

            except Exception:
                merge_nums.append(one_num)
                break

        return merge_nums + two_nums
