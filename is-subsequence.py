class Solution:

    def isSubsequence(self, s: str, t: str) -> bool:
        _t = {}
        for i, char_t in enumerate(t):
            if char_t not in _t:
                _t[char_t] = [i]
            else:
                _t[char_t].append(i)

        _min = -1
        for char_s in s:
            if char_s not in _t:
                return False

            if _min == -1:
                _min = _t[char_s][0]
                continue
            else:
                if _min > _t[char_s][-1]:
                    return False

                for index_t in _t[char_s]:
                    if index_t > _min:
                        _min = index_t
                        break

        return True


if __name__ == "__main__":
    # s, t = "abc", "ahbgdc"
    s, t = "axc", "ahbgdc"

    print(Solution().isSubsequence(s, t))
