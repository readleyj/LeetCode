class Solution:
    def piece_hash(self, piece):
        return ''.join(map(str, piece))

    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        piece_hash_set = set([self.piece_hash(piece) for piece in pieces])

        running_hash = ''

        for num in arr:
            running_hash += str(num)

            if running_hash in piece_hash_set:
                running_hash = ''

        return running_hash == ''
