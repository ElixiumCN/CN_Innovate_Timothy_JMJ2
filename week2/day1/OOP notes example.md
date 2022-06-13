Factory assembly line, at each step some material gets processed by a system component resulting in producing a final product out of a raw material.
Like raw materials at each stage of an assembly line, an object will contain data and with the likeness of an assembly component an object will also perform behaviors.
-realpython.com-

Everything in Python with a very small amount of exceptions are objects, with their porperties and methods.
A class can be referred to as a 'blueprint' for an object, like an object constructor.
-w3schools.com-

I understand that the creation of the majority of content within Python will be an object; classes being a large part of manipulating objects once created.

2.

Object Orientated Programming Notes:


Breif:
Object orientated programming or OOP for short is a methodolgy of forming code, incombersing design elements as well as modularity OOP is used in order to keep code formatted as to make it easy to read and decypher to people new to said code.

Structure:
OOP makes use of included components of a given language if that language supports OOP, for example in Python you have objects themselfs, which is almost everything including classes, and classes are used to construct new objects, for example, the data type 'int' or integer is an object that is used for referancing or instancing new versions of the int datatype, this means that it is also a class, and a class is can include both variables and functions, for example, the 'str' or string datatype has functions for capitalizaztion is various forms.

We can also create classes of our own, this is formatted as such;

class Person():     <-- This is how we delcare the name of the class as well as begin constructing our code.
    def __init__(self, name :str, age: int, eye_color: str, hair_color: str): <-- This is where we define our pass in data
        self.name = name            ]
        self.age = age              ] ----- This section is used to append the pass in data to the self referance
        self.eye = eye_color        ] ----- this creates a new instace when called later on in the code.
        self.hair = hair_color      ]

    def set_name(self, name):                   ]
        self.name = name                        ]
                                                ]
    def set_age(self, age):                     ]
        self.age = int(age)                     ] ----- This section of the class is used to define our functions, here you can see some
                                                ]       examples of 'setter' functions, this just means that we can change each attribute
    def set_eye(self, eye):                     ] ----- of a class instace later on by calling these functions and passing in our changes
        self.eye = eye                          ]
                                                ]
    def set_hair(self, hair):                   ] ----- You can also use 'getter' functions in a similar way, for example, if I wanted to
        self.hair = hair                        ]       get the name for a given instance of 'Person' I could make a get_name function here
                                                ]       however, in this case i prefer to use lists and for loops to iterate through all
    def set_profession(self, profession):       ] ----- the class instances I store within, for example, the NPC list below.
        self.profession = profession            ]

player = Person("default", 1, 'eye-color', 'hair-color')        ]
npc1 = Person("Jude", 22, 'emerald green', 'strawberry')        ] ----- Here you can see how we construct new instances for the Person class
npc2 = Person("Jake", 52, 'crimson red', 'gremmish')            ]       this just means that they follow the data structure within that
npc3 = Person("Berkley", 24, 'skinny green', 'custard')         ]       class, they call have a name, age and so on added to them, these
npc4 = Person("Trevor", 66, 'sunlit blue', 'low pink')          ] ----- are used at the start to provide the default values.
npc5 = Person("Oscar", 101, 'musk yellow', 'viscount mint')     ]
npc6 = Person("Gunther", 23, 'gremlin brown', 'no')             ]

npc_list = []           ] ----- This creates the list where we are storing all of our NPC instances.

npc_list.append(npc1)   ]
npc_list.append(npc2)   ] ----- and this part appends them to that list, notice how we don't append the player instance,
npc_list.append(npc3)   ]       this is becase the player even though they follow the same data structure within the Person class
npc_list.append(npc4)   ]       they are unique in this program, meaning that we don't need to add them to a list at this point,
npc_list.append(npc5)   ] ----- should you which to add them to a list later on, for example if they join a faction this can be done.
npc_list.append(npc6)   ]

def chara_creation():                                                   ]
    player_name = input('Please enter your NAME: \n')                   ]
    player_age = int(input('Please enter your AGE: \n'))                ] ----- Here we can see the 'setter' functions from the class
    player_eye = input('Please enter your EYE color: \n')               ]       being used to form part of the chara_creation function
    player_hair = input('Please enter your HAIR color: \n')             ]       this is done to allow the user to personalize their
    player_profession = input('Please enter your PROFESSION: \n')       ]       charater in which ever way they want.
    player.set_name(player_name.title())                                ]
    player.set_age(player_age)                                          ]       also take note that we are also calling the x.title()
    player.set_eye(player_eye.title())                                  ]       function here to make sure they fit within the text
    player.set_hair(player_hair.title())                                ]       formatting we want, x.title() is a funtion within the
    player.set_profession(player_profession.title())                    ] ----- string class

def player_info(obj):                                           ]
    print(f'''                                                  ]
    Hello! {obj.name}                                           ] ----- Finally here is a function that has been built around modularity
    your profession is {obj.profession}                         ]       which is key in OOP as it allows us to pass in objects and extract
    you have loverly {obj.eye} eyes, and {obj.hair} hair        ]       data from them, it is key to try and keep code that can serve a
    You are {obj.age} years old                                 ]       singular yet broad purpose, in doing so it will allow us to pass
    ''')                                                        ] ----- in a variety of diffrent objects later on.

Thank you for coming to me TED talk, Have a great day!