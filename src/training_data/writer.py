# a bit faulty

fin = open('training_data/clean_chat.txt', 'r')
fout = open('training_data/template.txt', 'w')
start = int(input('Choose a starting line: '))

def write(inp, outp, s):
    flag = False
    # with the flag, we can check where to record the next message we read 
    for idx, line in enumerate(inp):
        if idx < s or line.isspace(): # bug, s-1 will actually start it at the starting line (0-based indexing)
            continue
        if idx >= s: #s-1
            if flag == False:
                outp.write("{'role': 'user', 'content': '" + line.strip() + "'}," + "\n")
                flag = True
                # write the next message as from the assistant
            else:
                outp.write("{'role': 'assistant', 'content': '" + line.strip() + "'}," + "\n")
                flag = False
                # write the next message as from the user
        if idx == 200: # this was a mistake, i meant s+200 (only read ~200 lines), but the output wasn't any different weirdly.
            break      # both times, there was an error UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 1159: character maps to <undefined>

write(fin, fout, start)