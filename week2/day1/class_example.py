class Person():
    def __init__(self, name :str, age: int, eye_color: str, hair_color: str):
        self.name = name
        self.age = age
        self.eye = eye_color
        self.hair = hair_color

npc_list = []
player = Person("Makayla", 27, 'icey blue', 'auburn')
npc1 = Person("Jude", 22, 'emerald green', 'strawberry')
npc2 = Person("Jake", 52, 'crimson red', 'gremmish')
npc3 = Person("Berkley", 24, 'skinny green', 'custard')
npc4 = Person("Trevor", 66, 'sunlit blue', 'low pink')
npc5 = Person("Oscar", 101, 'musk yellow', 'viscount mint')
npc6 = Person("Gunther", 23, 'gremlin brown', 'no')

npc_list.append(npc1)
npc_list.append(npc2)
npc_list.append(npc3)
npc_list.append(npc4)
npc_list.append(npc5)
npc_list.append(npc6)

def player_info(obj):
    print(f"Hello! {obj.name}, you have loverly {obj.eye} eyes, and {obj.hair} hair. You are {obj.age} years old")

def npc_info(name: str, npc_list):
    for obj in npc_list:
        if name.title() == obj.name:
            print(f"Their name:{obj.name}, they have {obj.eye} eyes, and {obj.hair} hair. they are {obj.age} years old")

def person_inspect():
    player_choice = input("Who do you want to inspect? [M]e // [O]ther")
    match player_choice.upper():
        case 'M' | 'ME': player_info(player)
        case 'O' | 'OTHER':
            print('avalible choices:')
            for obj in npc_list:
                print(obj.name)
            name_query = input('Enter their name >: ')
            npc_info(name_query, npc_list)

person_inspect()