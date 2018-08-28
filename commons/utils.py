# coding=utf-8

from list_node import ListNode


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
