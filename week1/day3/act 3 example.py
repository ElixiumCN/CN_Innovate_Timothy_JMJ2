fav_songs = [
    {
        'artist' : 'lady gaga',
        'song name': 'sour candy',
        'genre' : 'pop',
        'year' : '2020'
    },
    {
        'artist' : 'the midnight',
        'song name': 'change your or die',
        'genre' : 'synthwave',
        'year' : '2022'
    },
    {
        'artist' : 'dua lipa',
        'song name': 'hallucinate',
        'genre' : 'pop',
        'year' : '2020'
    },
    {
        'artist' : 'charli',
        'song name': 'you used to know me',
        'genre' : 'dance',
        'year' : '2022'
    }
]
def print_list_dict(choice_list: list):
    i = 0
    for x in fav_songs:
        print(fav_songs[i])
        i += 1

print_list_dict(fav_songs)