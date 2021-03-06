import backend as ez
import numpy.random as random
import pandas as pd
from termcolor import colored


# converts list to string for print
def l2s4print(l):
    alpha = str(l).replace('[', '')
    bravo = alpha.replace(']', '')
    charlie = bravo.replace("'", "")

    return charlie


def display_colored_stats_with_pbar(heading, spacing, cubes, dashes, color, debug=True, stat=0):
    attribute = heading + str(spacing * ' ') + '|' + str(cubes * '█') + str(dashes * '-') + '|'
    if debug:
        attribute = attribute + ' ' + str(stat)
    c_attribute = colored(attribute, color)
    print(c_attribute)
    return


def gen_one_from_another(attribute):
    # std = std.
    std = abs(attribute - 50)
    # std unchanged if its small
    if std < random.randint(5, 16):
        pass
    # if std is high then halfs it (helps stop generating ridiculous values)
    else:
        std = int(std / 2)

    # used as random.randint(lowpoint,highpoint) for generating exepected result
    lowpoint = std
    highpoint = 100 - attribute

    if (100 - attribute) < std:
        lowpoint = 100 - attribute
        highpoint = std

    # desired value
    expected_random = random.randint(lowpoint, highpoint + 1)

    # If value exceeds 100 or is lower than 0; re-generate
    while expected_random < 0 or expected_random > 100:
        expected_random = random.randint(lowpoint, highpoint + 1)

    return expected_random


class Person:
    """And thus a life was born"""

    # sm_meter : sadist/masochist meter
    # c_meter : confidence meter
    # kb_meter : kind/bitchy meter

    def __init__(self, name, middle_name, surname, gender, age, height, proper_nouns, loves, hates,
                 s_meter, m_meter, c_meter, k_meter, b_meter, penis, vagina, ass):
        self.name = name
        self.middle_name = middle_name
        self.surname = surname
        self.gender = gender
        self.age = age
        self.height = height
        self.proper_nouns = proper_nouns
        self.loves = loves
        self.hates = hates
        self.s_meter = s_meter
        self.m_meter = m_meter
        self.c_meter = c_meter
        self.k_meter = k_meter
        self.b_meter = b_meter
        self.penis = penis
        self.vagina = vagina
        self.ass = ass

    def show(self):
        print(f'Name  : {self.name} {self.middle_name} {self.surname}\n'
              f'Gender: {self.gender} Age: {self.age} Height: {self.height} cm\n'
              f'Loves : {l2s4print(self.loves)}\n'
              f'Hates : {l2s4print(self.hates)}')

    def metrics(self, partitions=20):
        print('=' * 150)
        dash = '-'
        cube = '█'

        # Make sure 100 is divisible by 'partitions' value. Even though it runs fine for most part but by not doing
        # that it causes progress bar to display within an error range of 1
        part = 100 / partitions

        s = int(self.s_meter / part)
        s_dash = partitions - s - 1

        m = int(self.m_meter / part)
        m_dash = partitions - m - 1

        cm = int(self.c_meter / part)
        c_dash = partitions - cm - 1

        k = int(self.k_meter / part)
        k_dash = partitions - k - 1

        b = int(self.b_meter / part)
        b_dash = partitions - b - 1

        display_colored_stats_with_pbar("Sadism", spacing=6, cubes=s, dashes=s_dash, color='magenta', stat=self.s_meter)
        display_colored_stats_with_pbar("Masochism", spacing=3, cubes=m, dashes=m_dash, color='blue', stat=self.m_meter)
        display_colored_stats_with_pbar("Kind", spacing=8, cubes=k, dashes=k_dash, color='green', stat=self.k_meter)
        display_colored_stats_with_pbar("Bitchy", spacing=6, cubes=b, dashes=b_dash, color='red', stat=self.b_meter)
        display_colored_stats_with_pbar("Confidence", spacing=2, cubes=cm, dashes=c_dash, color='yellow',
                                        stat=self.c_meter)


        # Monochrome Display -------------------------------------------------------------------
        # print(f'Sadism     |{s * cube}{s_dash * dash}| Kindness   |{k * cube}{k_dash * dash}|')
        # print(f'Masochism  |{m * cube}{m_dash * dash}| Bitchiness |{b * cube}{b_dash * dash}|')
        # print(f'Confidence |{cm * cube}{c_dash * dash}|')
        print('=' * 150)


def get_s0m1_meter():
    s = random.choice(100, 1)
    # m = 100 - s
    m = gen_one_from_another(s)
    # print(f's: {s} m: {m}')
    return [s, m]


def get_c_meter():
    return random.choice(100, 1)


def get_k0b1_meter():
    k = random.choice(100, 1)
    # b = 100 - k
    b = gen_one_from_another(k)
    return [k, b]


def get_LH():
    list_lh = [[random.choice(ez.loves_and_hates), random.choice(ez.loves_and_hates),
                random.choice(ez.loves_and_hates), random.choice(ez.loves_and_hates)],

               [random.choice(ez.loves_and_hates), random.choice(ez.loves_and_hates),
                random.choice(ez.loves_and_hates), random.choice(ez.loves_and_hates)]]

    equality = False

    # makes love and hate unique from eachother
    for ele in list_lh[0]:
        if ele in list_lh[1]:
            # print(f'===== equality: {equality} ele: {ele} =====')
            # print(f'===== [0]: {list_lh[0]} [1]: {list_lh[1]} =====')
            if not equality:
                list_lh[1].remove(ele)
                equality = True
                continue
            elif equality:
                list_lh[0].remove(ele)
                equality = False
                continue

    list_lh[0] = list(dict.fromkeys(list_lh[0]))
    list_lh[1] = list(dict.fromkeys(list_lh[1]))

    # print(f'after list : {list_lh} \n')
    return list_lh


def create_people(total):
    lovely_people = []
    first_name = ''
    for i in range(total):
        a = random.randint(1, 4, 1)  # 0 = Female , 1 = Male, 3 = Futanari
        gender = ''
        if a == 1:
            first_name = random.choice(ez.female_names)
            gender = 'female'
        if a == 2:
            first_name = random.choice(ez.male_names)
            gender = 'male'
        if a == 3:
            first_name = random.choice(ez.female_names)
            gender = 'futanari'

        age, height = ez.assign_age_height(gender=gender)
        penis, vagina, ass = ez.assign_genital(gender=gender, age=age)
        middle_name = random.choice(ez.middle_names)
        surname = random.choice(ez.surnames)
        # setting love hate
        love, hate = get_LH()
        # setting sadist & maso meter
        s, m = get_s0m1_meter()
        # setting kind & bitchy
        k, b = get_k0b1_meter()
        p = Person(first_name, middle_name, surname, gender, age, height, '', love, hate, s, m, get_c_meter(), k, b,
                   penis, vagina, ass)
        lovely_people.append(p)
        i += 1
    return lovely_people


def showAllPeople(list_of_people, summary=True, metrics=False):
    print('=' * 150)
    for person in list_of_people:
        if summary:
            person.show()
            print('=' * 150)
        if metrics:
            person.metrics(partitions=20)


def showOnePerson(ID, list_of_people, summary=True, metrics=False):
    for person in list_of_people:
        if person.name == ID:
            if summary:
                person.show()
            if metrics:
                person.metrics(partitions=20)
    return


# Save friendly value to a pandas DataFrame
pd.set_option('display.max_rows', 500)
pd.set_option('display.width', 500)
pd.set_option('display.max_columns', 500)


def save_pandas(all_people):
    d = {'Name': [person.name for person in all_people],
         'Middle Name': [person.middle_name for person in all_people],
         'Surname': [person.surname for person in all_people],
         'Gender': [person.gender for person in all_people],
         'Age': [person.age for person in all_people],
         'Height': [person.height for person in all_people],
         'Sadist': [int(person.s_meter) for person in all_people],
         'Masochist': [int(person.m_meter) for person in all_people],
         'Confidence': [int(person.c_meter) for person in all_people],
         'Kind': [int(person.k_meter) for person in all_people],
         'Bitchy': [int(person.b_meter) for person in all_people],
         'Penis': [int(person.penis) for person in all_people],
         'Vagina': [int(person.vagina) for person in all_people],
         'Ass': [int(person.ass) for person in all_people]
         }
    df = pd.DataFrame(data=d)

    '''stats = df.groupby(['Name', 'Middle Name', 'Surname','Gender', 'Sadist', 'Masochist', 'Confidence', 'Kind', 'Bitchy'
                        ]).size().reset_index(name='Count')'''

    # Calculate Duplicate Count
    '''statsn = df.pivot_table(index=['Name'], aggfunc='size')
    statsmn = df.pivot_table(index=['Middle Name'], aggfunc='size')
    statssn = df.pivot_table(index=['Surname'], aggfunc='size')
    statsg = df.pivot_table(index=['Gender'], aggfunc='size')
    statsa = df.pivot_table(index=['Age'], aggfunc='size')
    statsh = df.pivot_table(index=['Height'], aggfunc='size')
    statss = df.pivot_table(index=['Sadist'], aggfunc='size')
    statsm = df.pivot_table(index=['Masochist'], aggfunc='size')
    statsc = df.pivot_table(index=['Confidence'], aggfunc='size')
    statsk = df.pivot_table(index=['Kind'], aggfunc='size')
    statsb = df.pivot_table(index=['Bitchy'], aggfunc='size')'''

    return df
