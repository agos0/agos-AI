fin = open('chat_data/clean_chat.txt', 'r')
fout = open('chat_data/template.txt', 'w')
start = int(input('Choose a starting line: '))

def write(inp, outp, s):
    flag = False
    # with the flag, we can check where to record the next message we read 
    for idx, line in enumerate(inp):
        if idx < s or line.isspace():
            continue
        if idx >= s:
            if flag == False:
                outp.write("{'role': 'user', 'content': '" + line.strip() + "'}," + "\n")
                flag = True
                # write the next message as from the assistant
            else:
                outp.write("{'role': 'assistant', 'content': '" + line.strip() + "'}," + "\n")
                flag = False
                # write the next message as from the user
        if idx == 200:
            break

write(fin, fout, start)