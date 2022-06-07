if __name__ == '__main__': print('blahhhh')

def meet_and_greet_people(names):
    meet_and_greet_speech = 'Let me introduce you all!'
    introductions = 0

    for name in names:
        is_first = name == names[0]
        is_last = name == names[len(names) -1]

        if is_first: meet_and_greet_speech = f"{meet_and_greet_speech} First up we have {name}!"
        elif is_last: meet_and_greet_speech = f"{meet_and_greet_speech} Last but not least {name}."
        else: meet_and_greet_speech = f"{meet_and_greet_speech} {name}, welcome!"
        
        for target in names:
            if name == target: continue
            meet_and_greet_speech = f"{meet_and_greet_speech} {name}, this is {target}."
            introductions = introductions + 1

    meet_and_greet_speech = f"{meet_and_greet_speech} Phew! Glad to get those {introductions} introductions out of the way!"
    return meet_and_greet_speech
