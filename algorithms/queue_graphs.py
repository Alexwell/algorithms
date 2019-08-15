from collections import deque


def search_seller(**kwargs):
    search_queue = deque()
    search_queue += kwargs['you']
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print(f'{person} is a mango seller!')
                return True
            else:
                search_queue += kwargs[person]
                searched.append(person)

    print('no sellers')
    return False


def person_is_seller(name):
    return name[-1] == 'm'
