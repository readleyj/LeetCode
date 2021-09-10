class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_size_map = {}
        output = []

        for idx, size in enumerate(groupSizes):
            if size not in group_size_map:
                group_size_map[size] = []

            group_size_map[size].append(idx)

            if len(group_size_map[size]) == size:
                output.append(group_size_map[size][:])
                group_size_map[size].clear()

        return output
