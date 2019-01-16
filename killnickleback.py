
# Define a set that contains tuples. Each tuple should contain two strings:
songs = {
    ('Nickelback', 'How You Remind Me'),
    ('Will.i.am', 'That Power'),
    ('Miles Davis', 'Stella by Starlight'),
    ('Nickelback', 'Animals')
}


#Using a set comprehension, create a new set that contains all songs that were not performed by Nickelback.
new_list = [f' {k}, {i} ' for k,i in songs if k != 'Nickelback']

print(songs)
print(new_list)