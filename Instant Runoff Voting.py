def runoff(voters):
    cand = len(voters[0])
    vlen = len(voters)
    fail = {}
    all_cand = {}
    for voter in voters:
        for vote in voter:
            all_cand[vote] = 0
    while True:
        vsum = {}
        for voter in voters:
            for vote in voter:
                if fail.get(vote) is None:
                    vsum[vote] = vsum.get(vote, 0) + 1
                    break
        for k in vsum:
            min = max = k
            break
        for k in vsum:
            if vsum[min] > vsum[k]:
                min = k
            if vsum[max] < vsum[k]:
                max = k
        if vsum[max] > vlen // 2:
            return max
        for k in vsum:
            if vsum[min] == vsum[k]:
                fail[k] = 1
        for k in all_cand:
             if fail.get(k) is None:
                if vsum.get(k) is None:
                    fail[k] = 1
        if len(fail) == cand:
            return None


voters =    [['Reinhard von Musel', 'Frank Underwood', 'Daisuke Aramaki', 'Lex Luthor'],
             ['Lex Luthor', 'Daisuke Aramaki', 'Reinhard von Musel', 'Frank Underwood'],
             ['Lex Luthor', 'Daisuke Aramaki', 'Frank Underwood', 'Reinhard von Musel'],
             ['Lex Luthor', 'Reinhard von Musel', 'Daisuke Aramaki', 'Frank Underwood'],
             ['Frank Underwood', 'Reinhard von Musel', 'Daisuke Aramaki', 'Lex Luthor'],
             ['Daisuke Aramaki', 'Frank Underwood', 'Lex Luthor', 'Reinhard von Musel'],
             ['Daisuke Aramaki', 'Reinhard von Musel', 'Lex Luthor', 'Frank Underwood'],
             ['Lex Luthor', 'Reinhard von Musel', 'Daisuke Aramaki', 'Frank Underwood']]

print(runoff(voters))