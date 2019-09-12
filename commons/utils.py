# coding=utf-8

from list_node import ListNode
from tree_node import TreeNode


class Utils(object):

    @staticmethod
    def list_to_listnode(_l):
        root = ListNode(0)
        ptr = root
        for ele in _l:
            ptr.next = ListNode(ele)
            ptr = ptr.next

        return root.next

    @staticmethod
    def listnode_to_list(listnode):
        _l = []
        while listnode:
            _l.append(listnode.val)
            listnode = listnode.next

        return _l

    @staticmethod
    def reverse_num(num):
        _reverse_num = 0
        while num > 0:
            _reverse_num = _reverse_num * 10 + num % 10
            num = num / 10

        return _reverse_num

    @staticmethod
    def list_to_treenode(_l):
        pass
