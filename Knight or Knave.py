def knight_or_knave(said):
    return 'Knight!' if eval(str(said)) else 'Knave! Do not trust.'

print(knight_or_knave(True))