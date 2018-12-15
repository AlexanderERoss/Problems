def gen_towers(no_blocks):
    towers = [[],[],[]]
    i = 1
    block_no = no_blocks
    while i <= no_blocks:
        towers[0].append(block_no)
        block_no -= 1
        i += 1
    return towers

def move_block(towers, a, b):
    # Moves block from tower a to tower b (integers)
    # If it's not possible it leaves it stationary
    if not towers[a]:
        print("Impossible move!")
        return towers
    if not towers[b]:
        towers[b].append(towers[a].pop())
        print(towers)
        return towers
    if towers[a][len(towers[a])-1] < towers[b][len(towers[b])-1]:
        towers[b].append(towers[a].pop())
        print(towers)
        return towers
    else:
        print("Impossible move!")
        return towers

def other_tower(current_towers, all_towers):
    i = 0
    while i < len(current_towers):
        j = 0
        while j < len(all_towers):
            if current_towers[i] == all_towers[j]:
                del all_towers[j]
            j += 1
        i += 1
    return  all_towers

def solve_towers(towers, a, b):
    move_stack = move_gen(towers[a], a, b)
    print(move_stack)
    c = len(move_stack)
    while c > 0:
        move = move_stack.pop()
        towers = move_block(towers, move[0], move[1])
        c -= 1

def move_gen(stack_of_blocks, indx , indx_to_move_to):
    final_move = [[indx, indx_to_move_to]]
    if len(stack_of_blocks) == 1:
        return final_move
    else:
        stack_next_returning = stack_of_blocks.copy()
        stack_next_clearing = stack_of_blocks.copy()
        del stack_next_returning[0]
        del stack_next_clearing[0]
        other_indx = other_tower([indx, indx_to_move_to],[0,1,2])[0]
        returning_moves = move_gen(stack_next_returning, other_indx, indx_to_move_to)
        clearing_moves = move_gen(stack_next_clearing, indx, other_indx)
        move_stack = returning_moves + final_move + clearing_moves
        return move_stack

# Script to run solver

a = gen_towers(4)
solve_towers(a, 0, 1)
