import people as p
import time
start_time = time.time()


def menu():
    print(f'How many people are living here: ')
    total_people_no = int(input())
    all_people = p.create_people(total_people_no)

    while True:
        print(f'Here are your options:')
        print(f'1) Display All')
        print(f'2) Look for extra details for someone ')
        print(f'3) Show in sheet form ')
        choice = int(input())

        if choice == 1:
            p.showAllPeople(all_people)

        if choice == 2:
            print(f'Find by first name basis')
            name = input()
            p.showOnePerson(name, all_people, metrics=True)

        if choice == 3:
            stat_sheet = p.save_pandas(all_people=all_people)
            if choice == 3:
                print(stat_sheet)


if __name__ == '__main__':
    # █ █ █ █

    menu()
    print(f'---------- Time Elapsed: {round(time.time() - start_time, 6)} ----------')
