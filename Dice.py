import random


def roll_dice(dice_code):
    dice_code = dice_code.strip().upper()

    if 'D' not in dice_code:
        return "Invalid input format. Please use 'xDy+z' format."

    d_pos = dice_code.find('D')

    num_part = dice_code[:d_pos]
    dice_part = dice_code[d_pos + 1:]

    if num_part == '':
        num_part = 1
    else:
        try:
            num_part = int(num_part)
        except ValueError:
            return "Invalid number of dice."

    valid_dice_types = ['3', '4', '6', '8', '10', '12', '20', '100']
    if dice_part not in valid_dice_types:
        return f"Invalid dice type: D{dice_part}. Valid types are: D3, D4, D6, D8, D10, D12, D20, D100."

    modifier = 0
    if '+' in dice_part or '-' in dice_part:
        if '+' in dice_part:
            dice_part, modifier = dice_part.split('+')
            modifier = int(modifier)
        elif '-' in dice_part:
            dice_part, modifier = dice_part.split('-')
            modifier = -int(modifier)

    total = 0
    for _ in range(num_part):
        total += random.randint(1, int(dice_part))

    total += modifier

    return f"Roll result: {total} (Dice rolled: {num_part}D{dice_part}, Modifier: {modifier})"


print(roll_dice("2D10+10"))

