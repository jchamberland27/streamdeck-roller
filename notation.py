#/usr/bin/python3

def dice_notation_to_list(dice_notation):
    """Convert a dice notation string to a list of dice strings."""
    number_of_dice, dice_type = map(int, dice_notation.split('d'))
    result = [f'd{dice_type}' for _ in range(number_of_dice)]
    return result


def check_if_die(part):
    """determine if a part is a number or a die"""
    if part[0] == 'd':
        return True
    else:
        return False


def prepare_roll(roll):
    """Prepare a roll for output."""
    json = {'set':[], 'constant':0}
    set = []
    for die in roll:
        set.append({'type':die,'diecolor':'#202020', 'labelColor':'#aaaaaa'})
    json['set'] = set
    return json