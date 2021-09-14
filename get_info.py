import requests

def word_ending(num):
    if num == 1:
        return 'task'
    else:
        return 'tasks'

def res():
    ident = {'Anonim': '75475616', 'BOPOH': '80943547', 'Redrum': '61508683', 'Pitonshik': '67071989', 'Elendil': '1437407', 'TechoViking': '332751846'}
    answer = {'Anonim': 0, 'BOPOH': 0, 'Redrum': 0, 'Pitonshik': 0, 'Elendil': 0}
    url = 'https://stepik.org:443/api/user-activities/'
    top = str()
    lazy_guys = str()
    result_list = list()
    for key, value in ident.items():
        res = requests.get(url + value)
        answer[key] = res.json()['user-activities'][0]['pins'][0]
    # answer['BOPOH'] = 10000
    result_list = sorted(answer.values(), reverse=True)
    answer = list(answer.items())
    count = 0

    for i in range(len(result_list)):
        if result_list[i] != 0 and result_list[i] != result_list[i-1]:
            count += 1
            for j in range(len(answer)):
                if result_list[i] == answer[j][1]:
                    # if answer[j][0] == 'BOPOH':
                    #     top += f'{count} place - {answer[j][0]} ({answer[j][1]} кирпичей)\n'
                    # else:
                    t = word_ending(result_list[i])
                    top += f'{count} place - {answer[j][0]} ({answer[j][1]} {t})\n'
    

    for account in answer:
        if account[1] == 0:
            lazy_guys += ('\n' + account[0])

    return ('TOP:\n' + top + '\nLazy guys:' + lazy_guys)

