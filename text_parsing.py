def clearing_line_from_bot_telegrams(line: str, search_text: str) -> str:
    
    list_string = list(line.split(" "))
    
    resalt_list = list()
    
    for count in range(0, len(list_string), 1):
        
        if list_string[count].count(search_text) == 0:
            resalt_list.append(list_string[count])
    
    resalt_text = ''
    
    for count in range(0, len(resalt_list), 1):
        if count != len(resalt_list)-1:
            resalt_text += str(resalt_list[count]) + ' '
        else:
            resalt_text += str(resalt_list[count])

    return resalt_text

'''
как будет время напишу лучше (без дублей):
'''
def print_answer_for_bot_v1(data_in: list) -> str:

        if data_in == []: 
            ansver = "по вашему запросу данные не найдены"
        else:
            ansver = ""
            for count_one in data_in:
                for count_two in count_one:
                    ansver += str(count_two) + " "
                ansver += "\n"
        
        return ansver