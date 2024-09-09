def last_animal_name_length(animal_sequence):
    # Write your code here
    name = ''
    l = []
    endofword = 0
    print(animal_sequence)
    for i in range(len(animal_sequence)):
        if endofword == 1 and len(name) != 0:
            l.append(len(name))
            name = ''
            endofword = 0
        if animal_sequence[i] == '-' or animal_sequence[i] == '|':
            l.append(len(name))
            name = ''
            continue
        else:
            name += animal_sequence[i]
            
        if i == len(animal_sequence)-1:
            print('yes')
            endofword = 1
            l.append(len(name))
            name = ''
    if len(l) > 0:
        return l[len(l)-1]

last_animal_name_length('tiger-lion-')