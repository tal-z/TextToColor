import copy

from nltk.corpus import wordnet
from ColorController import ColorController
from ColorController.namelookup import colors_df
from ColorController.helpers import regular_round



def wup_similarity(token1, token2):
    #print(token1)
    print(token2)
    if token1 in wordnet.words() and token2 in wordnet.words():
        syns1 = wordnet.synsets(token1)
        #print(syns1)
        syns2 = wordnet.synsets(token2)
        #print(syns2)
        wup_scores = []
        for syn1 in syns1:
            for syn2 in syns2:
                wup_scores.append((syn1, syn2, syn1.wup_similarity(syn2) or 0))
        #print(wup_scores)
        max_syn = max(wup_scores, key=lambda x: x[2])
        #print(max_syn)
        return max_syn[2]
    else:
        return 0


my_token = "gray"

try:
    test_color = ColorController(name=my_token)
    test_color.show_color()
    print('not a good test name.')

except:

    colors_df_copy = copy.deepcopy(colors_df)
    colors_df_copy['wup_similarity'] = colors_df_copy.NAME.apply(lambda x: wup_similarity(my_token, x.replace("_", " ")))
    #colors_df_copy['wup_similarity'] = wup_similarity(my_token, colors_df_copy.NAME)

    closest_color = colors_df_copy.iloc[colors_df_copy['wup_similarity'].argmax()]
    print(closest_color)

    color = ColorController(name=closest_color.NAME)

    color.show_color()



