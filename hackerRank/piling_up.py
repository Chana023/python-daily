from collections import deque
    
tests = int(input())

for _ in range(tests):
    
    blocks_count = int(input())
    blocks = deque(map(int, input().split()))
    can_pile = "Yes"
    base_block = None

    while len(blocks) > 1:

        left = blocks.popleft()
        right = blocks.pop()

        if left >= right:
            if base_block is None or base_block >= left:
                base_block = left
                blocks.append(right)
            else:
                can_pile = "No"
        else:
            if base_block is None or base_block >= right:
                base_block = right
                blocks.appendleft(left)
            else:
                can_pile = "No"

        if can_pile == "No":
            break

    print(can_pile)