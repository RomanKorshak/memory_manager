import math

HELP = """Available commands:
            
            help - show this help
            exit - exit this program
            print - print memory blocks map
              allocate <num> - allocate <num> cells. Returns
           block first cell number
              free <num> - free block with first cell number
           <num>"""



print('Please set memory size and max output width:')
user_input = input('>').split(' ')
mem_size, max_row = int(user_input[0]), int(user_input[1])
print("Type 'help' for additional info.")

memory = []




def allocate(size):
    if len(memory) == 0 and size <= mem_size or memory[0][0] >= size:
        memory.insert(0, [0,size])
        return 0
    elif len(memory) > 0:
        for i in range(len(memory) + 1):
            a = memory[i][0] + memory[i][1]
            if len(memory) - 1 and  memory[i + 1][0] - a >= size:
                memory.insert(i + 1, [a,size])
                return a
            last_in = len(memory) - 1

            a = memory[last_in][0] + memory[last_in][1]
            if mem_size - a >= size:
                memory.insert(last_in + 1, [a, size])
                return a



def free(block_id):
    for index, node in enumerate(memory):
        if node[0] == block_id:
            del memory[index]
        


def display():
    len_row = len(str(mem_size)) * max_row 
    row = ''
    counter = 0
    while counter < mem_size:
        for node in memory:
            length_block = len(str(mem_size)) * node[1] - len(str(node[0]))
            if counter == node[0]:
                row += f"{node[0]}{'x' * length_block}|"
                counter += node[1]
            else:
                diff = node[0] - counter
                row += f"{' ' * diff * len(str(mem_size))}|"
                row += f"{node[0]}{'x' * length_block}|"
                counter += (diff + node[1]) 
        row += f"{' ' * (mem_size - counter + 1) * len(str(mem_size))}"
        counter += (mem_size - counter)
            
    row = row.replace('||', '|')
    start = 0
    end = len_row
    for _ in range(math.ceil(mem_size / max_row)):
        line = f"|{row[start:end]}|".replace('||','|')
        print(line)
        start = end + 1
        end += len_row + 1
    







