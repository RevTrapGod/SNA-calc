yeast_nut = {'71b': 'low', 'd47': 'low', 'ec1118': 'low', 'd21': 'low', 'd80': 'med', 'rc212': 'med', 'qa23': 'low', 'us05': 'high', 's04': 'high', 'kv11116': 'med', 'montrachet': 'low', 'cote de blancs': 'med', 'premier cuvee': 'med', 'pasteur red': 'med', 'pasteur champagne': 'med', 'bcs103': 'low', 'vr44': 'low', 'bm4x4': 'high', 'bm45': 'high', 'cy3079': 'high', 'brl97': 'med', 'dv10': 'low', 'd254': 'med', 'r2': 'high', 'rhone 2056': 'med', 'enoferm 2226': 'high', 'bo213': 'low', 'rose': 'low', 'f33': 'low', 'f5': 'med', 'rms2': 'low', 'f15': 'med', 'fx10': 'low', 'rx60': 'high', 'x16': 'med', 'ch9': 'med', 'delta': 'high', 'rb2': 'low', 'vl1': 'high', 'vl2': 'med', 'vl3': 'high', 'xpure': 'low', 'x5': 'high', 'spark': 'low', 'st': 'high', 'f83': 'med'}

yeast_abv = {'71b': 0.14, 'd47': 0.14, 'ec1118': 0.18, 'd21': 0.16, 'd80': 0.16, 'rc212': 0.16, 'qa23': 0.16, 'us05': 0.13, 's04': 0.11, 'v1116': 0.18, 'montrachet': 0.15, 'cote de blancs': 0.16, 'premier cuvee': 0.17, 'pasteur red': 0.15, 'pasteur champagne': 0.18, 'bcs103': 0.18, 'vr44': 0.16, 'bm4x4': 0.15, 'bm45': 0.15, 'cy3079': 0.15, 'brl97': 0.16, 'dv10': 0.18, 'd254': 0.16, 'r2': 0.16, 'rhone 2056': 0.16, 'enoferm 2226': 0.18, 'bo213': 0.18, 'rose': 0.15, 'f33': 0.16, 'f5': 0.16, 'rms2': 0.17, 'f15': 0.16, 'fx10': 0.16, 'rx60': 0.17, 'x16': 0.17, 'ch9': 0.16, 'delta': 0.15, 'rb2': 0.15, 'vl1': 0.15, 'vl2': 0.16, 'vl3': 0.15, 'xpure': 0.16, 'x5': 0.16, 'spark': 0.17, 'st': 0.15, 'f83': 0.16}

yeast_check = ['lalvin', 'zymaflore', 'actiflore', 'redstar', ' ', 'fermemtis', 'lallemand', 'safale', 'bourgoblanc', 'bourgorouge', 'k1','icv', '-']

yeast_input = input('enter yeast type:')

def yeast_convert(yeast_input):
    for  in yeast_input:
        yeast_input = yeast_input.replace(yeast_check, '')
        return yeast_input
        


    
