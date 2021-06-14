from datetime import date

group = {
    'members': {
        'Toktogul Satylganov': {
            'role': 'komuzist',
            'date': date(1938, 8, 9)
        },
        'Mirbek Atabekov': {
            'role': 'singer',
            'date': date(1986, 5, 11)
        },
        'Symyk Beyshekeev': {
            'role': 'danser',
            'date': date(1880, 12, 12)
        }
    },
    'conserts': {
        'Bishkek': {
            'concert_date': date(2021, 1, 1),
            'income': 10000,
            'expenses': [100, 200, 300]
        },
        'Talas': {
            'concert_date': date(2021, 2, 1),
            'income': 10000,
            'expenses': [400, 500, 600]
        },
        'Karakol': {
            'concert_date': date(2021, 3, 1),
            'income': 10000,
            'expenses': [700, 800, 900]
        },
        'Osh': {
            'concert_date': date(2021, 4, 1),
            'income': 10000,
            'expenses': [1000, 1100, 1200]
        },
        'Batken': {
            'concert_date': date(2021, 5, 1),
            'income': 10000,
            'expenses': [1300, 1400, 1500]
        },
    }
}

# Добавление участника группы
def add_new_member(group, **kwargs):
    group['members'].update(kwargs)
    return group

print(group['members'])

print('-----------------------------------------------------')
new_member = {'Siezdbek Iskenaliev': {'role': 'singer2', 'date': date(1967, 2, 12)}}
print(add_new_member(group, **new_member))
print('-----------------------------------------------------')

print(group['members'])

print('%%%%%%%%%%%--------------------------%%%%%%%%%%%%%')

# Удаление участника группы
def add_del_member(group, name):
    group['members'].pop(name)
    return group

print(group['members'])

print('-----------------------------------------------------')
del_name = 'Mirbek Atabekov'
print(add_del_member(group, del_name))
print('-----------------------------------------------------')
print(group['members'])

print('%%%%%%%%%%%--------------------------%%%%%%%%%%%%%')

# Добавление концерта
def add_new_member(group, **kwargs):
    group['conserts'].update(kwargs)
    return group

print(group['conserts'])

print('-----------------------------------------------------')
new_member = {'Naryn': {'concert_date': date(2021, 5, 1), 'income': 10000, 'expenses': [1300, 1400, 1500]}}
print(add_new_member(group, **new_member))
print('-----------------------------------------------------')

print(group['conserts'])

print('%%%%%%%%%%%--------------------------%%%%%%%%%%%%%')


# Подсчет прибыли за концерт
def cash_sity(group, sity):
    price = group['conserts'][sity]['income']- sum(group['conserts'][sity]['expenses'])
    return f'В городе {sity}  приыль составила {price} долларов'



print('-----------------------------------------------------')
c_sity = 'Bishkek'
print(cash_sity(group, c_sity))

print('%%%%%%%%%%%--------------------------%%%%%%%%%%%%%')


# Общий подсчет прибыли
def all_cash(group):
    all_money = 0
    for m_sity, m_info in group['conserts'].items():
        all_money += (m_info['income'] - sum(m_info['expenses']))
    return f'Текущая прибыль во всех городах составила {all_money} долларов'

print(all_cash(group))
