import re
import sys

    
def replace_tables(contents):
    #inpt = sys.stdin.read()
    #print(inpt)
    result = re.sub(r'(\.---.*?---\.)', table_replacer, contents, flags=re.S)


    return result

def table_replacer(match):
    table_contents = match.group(0)
    #print(contents)
    input_lines = table_contents.split('\n')
    
    table_start = '.---'
    table_end = '---.'
    cell_separators = ('---', '===')
    span_col_separators = ('--', '==')
    rows = 1 # not used
    cols = 2

    contents = []
    lens = [0] * cols
    row_separators = []
    # [row][col] = '|' or ''
    col_separators = []
    #print(lens)

    table_ended = False

    #print(input_lines)
    output = ''
    r = 0
    while not table_ended:
        contents.append([])
        col_separators.append([])
        row_separator = '-'
        for c in range(cols):
            maxlen = lens[c]
            lines = []
            while True:
                if len(input_lines) == 0: break
                try:
                    inp = input_lines.pop(0)
                    if inp == table_start: continue
                    if inp == table_end:
                        table_ended = True
                        break
                    if inp in cell_separators + span_col_separators:
                        if inp in span_col_separators:
                            col_separators[r].append(' ')
                        else:
                            col_separators[r].append('|')
                        row_separator = inp[0]
                        break
                    lines.append(inp)
                    if len(inp) > maxlen:
                        maxlen = len(inp)
                except EOFError:
                    break
            lens[c] = maxlen

            contents[r].append('\n'.join(lines))
        row_separators.append(row_separator)
        r += 1

    for i in range(len(lens)):
        lens[i] += 2
    #print(contents)
    #print(lens)

    def get_row_separator(lens, line='-'):
        return '+' + '+'.join(line * l for l in lens) + '+'

    def get_row(cells, lens, col_seps):
        lines = []
        celllines = [c.split('\n') for c in cells]
        maxlines = max([len(x) for x in celllines])
        for linenr in range(maxlines):
            line = '|'
            for i, c in enumerate(celllines):
                cellcontents = ''
                if len(c) > linenr:
                    cellcontents = ' ' + c[linenr]
                #print('{:<' + str(lens[i]) + '}')
                #print(cellcontents)
                sep = '|'
                if i < len(col_seps): sep = col_seps[i]
                line += ('{:<' + str(lens[i]) + '}').format(cellcontents) + sep
            lines.append(line)

        return '\n'.join(lines)

     

    table_output = ""
    #print(col_separators)

    #print(get_row_separator(lens))
    table_output += get_row_separator(lens) + "\n"
    
    #print(get_row(['' for _ in contents[0]], lens))
    #print(get_row_separator(lens, '='))
    for r, row in enumerate(contents):
        #print(get_row(row, lens, col_separators[r]))
        table_output += get_row(row, lens, col_separators[r]) + "\n"
        #print(get_row_separator(lens, row_separators[r]))
        table_output += get_row_separator(lens, row_separators[r]) + "\n"
    #print(get_row_separator(lens))

    return table_output
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("   {} input_file [> output_file]".format(sys.argv[0]))
        print("         input_file - input file to be parsed")
        exit()

    brdir = """.. |br| raw:: html

   <br />

   """
   
    target = ''
    if len(sys.argv) > 2:
        target = ' {}'.format(sys.argv[2])
    comment = '.. generated using "python3 {} {}{}"'.format(sys.argv[0], sys.argv[1], target)
    
    with open(sys.argv[1], encoding='utf-8') as f:
        input_contents = f.read()
        result = replace_tables(input_contents)
        
        if '|br|' in result:
            result = brdir + result
        
        result += "\n\n" + comment
        if len(sys.argv) > 2:
            with open(sys.argv[2], 'w', encoding='utf-8') as fout:
                fout.write(result)
        else:
            print(result)
    