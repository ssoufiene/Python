def arithmetic_arranger(problems,second=False):
    topline = []
    downline = []
    dashesline = []
    sumline = []
    if len(problems) > 5:
        return("Error: Too many problems.")


    for item in problems:
        
        item = item.replace(' ', '')
        if ('+' in item):
            sign = '+'
        elif '-' in item:
            sign = '-'
        else:
            return("Error: Operator must be '+' or '-'.")
        new = item.partition(sign)
        if (new[0]).isdigit() == False or new[2].isdigit() == False:
            return("Error: Numbers must only contain digits.")
        if (len(new[0]) > 4) or len(new[2]) > 4:
            return("Error: Numbers cannot be more than four digits.")
            
        if len(new[0]) >= len(new[2]):
            ns = 2
        else:
            ns = len(new[2]) - len(new[0]) + 2
        top = ns * ' ' + new[0]
        topline.append(top)
        if len(new[0]) > len(new[2]):  # nsis number of spaces in the downline
            ns2 = 1 + len(new[0]) - len(new[2])
        else:
            ns2 = 1
        down = new[1] + ns2 * ' ' + new[2]
        downline.append(down)
        nd = len(down)  # number of dashes
        dashes = nd * '-'
        dashesline.append(dashes)
        if sign == '+':
            sum = int(new[0]) + int(new[2])
        else:
            sum = int(new[0]) - int(new[2])
        sum = str(sum)
        ns3 = nd - len(sum)
        suml = ns3 * ' ' + sum
        sumline.append(suml)

    if second==True:
        arranged_problems=('    '.join(topline) + '\n' + '    '.join(downline) + '\n' + '    '.join(dashesline) + '\n' + '    '.join(sumline))
    else :
        arranged_problems = ('    '.join(topline) + '\n' + '    '.join(downline) + '\n' + '    '.join(  dashesline))

    return arranged_problems
