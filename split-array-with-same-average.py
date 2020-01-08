class Solution:

    def splitArraySameAverage(self, A) -> bool:
        if len(A) <= 2:
            return False

        mean = sum(A) / len(A)
        for 
        print(mean)
        s = mean * 2
        for int_a in A:
            if s - int_a in A:
                return True

        return False


if __name__ == "__main__":
    a = [0, 13, 13, 7, 5, 0, 10, 19, 5]
    print(Solution().splitArraySameAverage(a))
