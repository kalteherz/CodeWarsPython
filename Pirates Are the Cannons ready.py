def cannons_ready(gunners):
    for k, v in gunners.items():
        if v == 'nay':
            return 'Shiver me timbers!'
    return 'Fire!'

a = {'Mike':'aye','Joe':'aye','Johnson':'aye','Peter':'aye'}
b = {'Mike':'aye','Joe':'nay','Johnson':'aye','Peter':'aye'}