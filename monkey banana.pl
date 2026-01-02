move(monkey, box).
move(box, banana).
get_banana :-
    move(monkey, box),
    move(box, banana),
    write('Monkey got the banana').
