def arithmetic_arranger(problems, show_answers=False):
    top_list = []
    bottom_list = []
    dashes_list = []
    answer_list = []
    if len(problems) > 5:
        return 'Error: Too many problems.'
    for entry in problems:           
        parts = entry.split()
        max_width = max(len(parts[0]), len(parts[2])) + 2
        if parts[0].isdigit() == False or parts[2].isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if len(parts[0]) > 4 or len(parts[2]) >4:
            return 'Error: Numbers cannot be more than four digits.'
        num1 = int(parts[0])
        operator = parts[1]
        num2 = int(parts[2])
       
        if operator != "+" and operator != "-" :
            return "Error: Operator must be '+' or '-'."
        if str(num1).isdigit() == False or str(num2).isdigit() == False:
            return 'Error: Numbers must only contain digits.'
        if operator == '+':
            result = str(num1+num2)
        else:
            result = str(num1-num2)    
        num_1 = str(num1)
        num_2 = str(num2)
       
        num_1 = num_1.rjust(max_width)
        num_2 = num_2.rjust(max_width - 2)  # -2 for operator and space
        dashes = max_width * '-'
        top = num_1
        bottom = f'{operator} {num_2}'
        top_list.append(top)
        bottom_list.append(bottom)
        dashes_list.append(dashes)
        result = result.rjust(max_width)
        answer_list.append(result)
    top_list = '    '.join(top_list)
    bottom_list = '    '.join(bottom_list)
    dashes_list = '    '.join(dashes_list)
    answer_list = '    '.join(answer_list)
    if show_answers == False:
        answer_list = ''
    
    problems = f'{top_list}\n{bottom_list}\n{dashes_list}'
    if show_answers:
        problems += f'\n{answer_list}'
    return problems
    
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))

    