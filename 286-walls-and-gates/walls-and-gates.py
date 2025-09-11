class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        r = len(rooms)
        c = len(rooms[0])

        q = deque([])

        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    q.append((i,j,0))
        seen = set()
        
        while q:
            r1 , c1,dist = q.popleft()

            for r2, c2 in [(-1,0),(1,0),(0,-1),(0,1)]:
                r2 += r1
                c2 += c1

                if (0 <= r2 < r) and (0 <=c2 <c) and rooms[r2][c2] == 2147483647 and (r2, c2) not in seen:
                    seen.add((r2,c2))
                    q.append((r2,c2,dist +1))
                    rooms[r2][c2] = dist +1

