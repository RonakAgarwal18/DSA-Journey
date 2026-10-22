class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def ops():
            for directions in product((iter, reversed), repeat=2):
                read = cycle(directions[0](nums))
                want = directions[1](range(len(nums)))
                rotations = indexOf(read, next(want))
                if all(map(eq, read, want)):
                   yield directions.count(reversed) + rotations
        return min(ops(), default=-1)