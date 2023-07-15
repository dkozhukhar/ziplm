# modify the code to work with a list of words

```{python}
import urllib.request
import re
from collections import Counter


# Download the part of the novell
data3 = urllib.request.urlopen("https://raw.githubusercontent.com/dkozhukhar/ziplm/main/data.txt").read().decode()


# Replace right single quotation marks with standard ASCII apostrophes
data = data3.lower().replace("’", "'")


# Split the piece into words
words = re.findall(r'\b\w[\w\']*s*\b', data)

# Count the frequency of each word
word_freq = Counter(words)

# Get the ... most common words
vocabulary = [word for word, freq in word_freq.most_common(1000)]


# Print the vocabulary and its length
print("Vocabulary:", vocabulary)
print("Length of vocabulary:", len(vocabulary))

# Create a ZipModels with the vocabulary
model = ZipModel(vocabulary, data)
model_untrained = ZipModel(vocabulary)

# Define the prefix
prefix = """
CHAPTER 87. The Grand Armada. 
""".lower().replace("’", "'")

# Sample a sequence of words
print("UnTrained:", " ".join(model_untrained.sample_sequence(50)))
print("Trained, no prefix:", " ".join(model.sample_sequence(50)))
print("Trained, with a prefix:", " ".join(model.sample_sequence(50, prefix=prefix)))
```

This gives me
```{python}
Vocabulary: ['the', 'of', 'and', 'in', 'to', 'a', 'that', 'by', 'as', 'at', 'but', 'with', 'from', 'was', 'whales', 'it', 'their', 'for', 'this', 'they', 'now', 'whale', 'had', 'all', 'one', 'which', 'we', 'his', 'on', 'is', 'like', 'so', 'were', 'not', 'be', 'seemed', 'these', 'when', 'us', 'some', 'he', 'our', 'have', 'more', 'up', 'into', 'then', 'time', 'upon', 'been', 'them', 'still', 'him', 'line', 'or', 'straits', 'though', 'you', 'if', 'are', 'two', 'long', 'sea', 'while', 'no', 'through', 'yet', 'other', 'after', 'sperm', 'almost', 'ship', 'three', 'only', 'away', 'herd', 'those', 'such', 'pequod', 'over', 'there', 'might', 'may', 'last', 'circles', 'boat', 'vast', 'being', 'between', 'out', 'has', 'what', 'round', 'java', 'sunda', 'little', 'ahab', 'air', 'her', 'off', 'did', 'an', 'any', 'boats', 'each', 'harpoon', 'queequeg', 'starbuck', 'way', 'lake', 'most', 'islands', 'sumatra', 'among', 'known', 'world', 'before', 'wind', 'day', 'even', 'great', 'would', 'water', 'down', 'another', 'together', 'white', 'host', 'centre', 'who', 'under', 'than', 'tail', 'many', 'ships', 'green', 'head', 'very', 'do', 'cruising', 'here', 'pursuit', 'how', 'crew', 'will', 'himself', 'she', 'whole', 'again', 'heard', 'sometimes', 'sail', 'both', 'distance', 'forward', 'beheld', 'place', 'swimming', 'sudden', 'chase', 'end', 'its', 'side', 'length', 'spring', 'close', 'commotion', 'evinced', 'possibly', 'men', 'cried', 'your', 'can', 'every', 'must', 'first', 'saw', 'drugged', 'i', 'young', 'deep', 'spade', 'narrow', 'point', 'rampart', 'indian', 'oriental', 'chiefly', 'vessels', 'china', 'seas', 'central', 'land', 'should', 'unlike', 'passed', 'malays', 'low', 'sailing', 'present', 'waters', 'fresh', 'where', 'giving', 'battle', 'does', 'running', 'too', 'seen', 'man', 'floating', 'themselves', 'well', 'indeed', 'wide', 'soon', 'single', 'falling', 'cheering', 'owing', 'met', 'seem', 'without', 'thousands', 'broad', 'bows', 'forming', 'half', 'right', 'thick', 'rising', 'spouts', 'rear', 'once', 'suspended', 'chased', 'few', 'could', 'wake', 'sight', 'swift', 'own', 'fro', 'pirates', 'dropping', 'become', 'gallied', 'short', 'occasional', 'creatures', 'shoal', 'about', 'fish', 'heart', 'part', 'fishery', 'thus', 'sides', 'flukes', 'lance', 'surface', 'attached', 'block', 'drugg', 'tossing', 'came', 'further', 'calm', 'outer', 'backs', 'darting', 'mothers', 'also', 'body', 'fast', 'rope', 'leviathan', 'circle', 'carrying', 'cutting', 'itself', 'began', 'oars', 'stand', 'peninsula', 'malacca', 'forms', 'asia', 'continuous', 'dividing', 'several', 'ports', 'west', 'standing', 'seamen', 'opening', 'thousand', 'seems', 'least', 'appearance', 'however', 'western', 'top', 'sails', 'procession', 'freely', 'means', 'renounce', 'solid', 'tribute', 'mind', 'lurking', 'late', 'somewhat', 'occasionally', 'remorselessly', 'drawing', 'nigh', 'sweep', 'far', 'coast', 'season', 'grounds', 'pacific', 'else', 'moby', 'dick', 'presumed', 'drink', 'circus', 'within', 'ring', 'mark', 'foreign', 'carries', 'herself', 'weapons', 'altogether', 'years', 'old', 'nantucket', 'hence', 'gone', 'new', 'back', 'touching', 'grain', 'having', 'carry', 'come', 'captured', 'near', 'fishermen', 'therefore', 'gained', 'look', 'bow', 'descried', 'game', 'entered', 'customary', 'aloft', 'spectacle', 'saluted', 'activity', 'small', 'detached', 'times', 'embracing', 'multitude', 'mutual', 'circumstance', 'best', 'months', 'spout', 'suddenly', 'miles', 'semicircle', 'horizon', 'chain', 'jets', 'playing', 'straight', 'deck', 'curling', 'dense', 'horseman', 'defile', 'perilous', 'gradually', 'contracting', 'crowding', 'harpooneers', 'loudly', 'witness', 'number', 'stun', 'along', 'driving', 'leviathans', 'something', 'completely', 'glass', 'whips', 'till', 'hot', 'make', 'leading', 'chasing', 'watery', 'gate', 'lay', 'route', 'same', 'black', 'steadily', 'astern', 'shot', 'speed', 'shirts', 'drawers', 'token', 'say', 'hitherto', 'rapidly', 'broken', 'going', 'spoutings', 'panic', 'strangely', 'floated', 'dismay', 'human', 'dashing', 'madness', 'said', 'advanced', 'nor', 'making', 'lone', "queequeg's", 'stricken', 'darted', 'steered', 'movement', 'struck', 'less', 'vicissitudes', 'monster', 'deeper', 'frantic', 'fastened', 'tore', 'ice', 'moment', 'locked', 'bit', 'across', 'hand', 'ones', 'instant', 'second', 'gunwale', 'calmly', 'certain', 'called', 'considerable', 'middle', 'kill', 'afterwards', 'killed', 'enormous', 'towing', 'caught', 'carried', 'slid', 'wounded', 'impossible', 'went', 'vanished', 'glided', 'innermost', 'mountain', 'yes', 'enchanted', 'pods', 'swiftly', 'shoulder', 'crowd', 'chance', 'escape', 'afforded', 'wall', 'cows', 'calves', 'inclusive', 'revolving', 'entire', 'cause', 'margin', 'wondrous', 'eyes', 'nursing', 'girth', 'infants', 'suckling', 'looking', 'towards', 'feet', 'maternal', 'parts', 'coils', 'cub', 'loose', 'entangled', 'milk', 'my', 'me', 'wound', 'rest', 'violently', 'prick', 'scrape', 'hat', 'taken', 'chapter', '87', 'grand', 'armada', 'extending', 'south', 'eastward', 'territories', 'birmah', 'southerly', 'stretch', 'bally', 'timor', 'others', 'form', 'mole', 'lengthwise', 'connecting', 'australia', 'unbroken', 'ocean', 'thickly', 'studded', 'archipelagoes', 'pierced', 'sally', 'convenience', 'conspicuous', 'bound', 'emerge', 'divide', 'midway', 'buttressed', 'bold', 'promontory', 'correspond', 'gateway', 'walled', 'empire', 'considering', 'inexhaustible', 'wealth', 'spices', 'silks', 'jewels', 'gold', 'ivory', 'enriched', 'significant', 'provision', 'nature', 'treasures', 'formation', 'bear', 'ineffectual', 'guarded', 'grasping', 'shores', 'unsupplied', 'domineering', 'fortresses', 'guard', 'entrances', 'mediterranean', 'baltic', 'propontis', 'danes', 'orientals', 'demand', 'obsequious', 'homage', 'lowered', 'endless', 'centuries', 'past', 'night', 'freighted', 'costliest', 'cargoes', 'east', 'waive', 'ceremonial', 'claim', 'piratical', 'proas', 'shaded', 'coves', 'islets', 'sallied', 'fiercely', 'demanding', 'spears', 'repeated', 'bloody', 'chastisements', 'received', 'hands', 'european', 'cruisers', 'audacity', 'corsairs', 'repressed', 'hear', 'english', 'american', 'boarded', 'pillaged', 'fair', 'purposing', 'pass', 'javan', 'thence', 'northwards', 'frequented', 'inshore', 'philippine', 'gain', 'japan', 'whaling', 'circumnavigating', 'previous', 'descending', 'everywhere', 'foiled', 'firmly', 'counted', 'frequent', 'reasonably', 'haunting', 'zoned', 'quest', 'touch', 'surely', 'stop', 'nay', 'sun', 'raced', 'fiery', 'needs', 'sustenance', "what's", 'whaler', 'hulls', 'loaded', 'alien', 'stuff', 'transferred', 'wharves', 'wandering', 'cargo', 'wants', "lake's", 'contents', 'bottled', 'ample', 'hold', 'ballasted', 'utilities', 'unusable', 'pig', 'lead', 'kentledge', 'clear', 'prime', 'afloat', 'nantucketer', 'prefers', 'brackish', 'fluid', 'yesterday', 'rafted', 'casks', 'peruvian', 'streams', 'york', 'score', 'interval', 'sighted', 'soil', 'news', 'flood', 'answer', 'boys', "here's", 'ark', 'vicinity', 'ground', 'roundabout', 'generally', 'recognised', 'excellent', 'spot', 'outs', 'repeatedly', 'hailed', 'admonished', 'keep', 'awake', 'palmy', 'cliffs', 'loomed', 'starboard', 'delighted', 'nostrils', 'cinnamon', 'snuffed', 'jet', 'renouncing', 'thought', 'hereabouts', 'cry', 'ere', 'singular', 'magnificence', 'premised', 'unwearied', 'hunted', 'four', 'oceans', 'instead', 'invariably', 'companies', 'former', 'frequently', 'extensive', 'herds', 'numerous', 'nations', 'sworn', 'solemn', 'league', 'covenant', 'assistance', 'protection', 'aggregation', 'immense', 'caravans', 'imputed', 'weeks', 'greeted', 'level', 'sparkling', 'noon', 'perpendicular', 'twin', 'fall', 'branches', 'cleft', 'drooping', 'boughs', 'willow', 'slanting', 'presents', 'curled', 'bush', 'mist', 'continually', 'leeward', "pequod's", 'rise', 'high', 'hill', 'vapory', 'individually', 'blending', 'atmosphere', 'bluish', 'haze', 'showed', 'cheerful', 'chimneys', 'metropolis', 'balmy', 'autumnal', 'morning', 'height', 'marching', 'armies', 'approaching', 'unfriendly', 'mountains', 'accelerate', 'march', 'eagerness', 'passage', 'expand', 'comparative', 'security', 'plain', 'fleet', 'hurrying', 'wings', 'crescentic', 'pressed', 'handling', 'heads', 'held', 'doubt', 'deploy', 'capture', 'tell', 'whether', 'congregated', 'caravan', 'temporarily', 'worshipped', 'elephant', 'coronation', 'siamese', 'piled', 'sailed', 'voice', 'tashtego', 'directing', 'attention', 'corresponding', 'crescent', 'van', 'formed', 'vapors', 'go', 'constantly', 'hovered', 'finally', 'disappearing', 'levelling', 'quickly', 'revolved', 'pivot', 'hole', 'crying', 'rig', 'buckets', 'wet', 'sir', 'behind', 'headlands', 'fairly', 'rascally', 'asiatics', 'cautious', 'delay', 'kind', 'tawny', 'philanthropists', 'assist', 'speeding', 'chosen', 'mere', 'riding', 'rowels', 'arm', 'paced', 'turn', 'beholding', 'monsters', 'bloodthirsty', '_him_', 'fancy', 'above', 'glanced', 'walls', 'bethought', 'vengeance', 'deadly', 'remorseless', 'wild', 'inhuman', 'atheistical', 'devils', 'infernally', 'curses', 'conceits', 'brain', "ahab's", 'brow', 'left', 'gaunt', 'ribbed', 'sand', 'beach', 'stormy', 'tide', 'gnawing', 'able', 'drag', 'firm', 'thing', 'thoughts', 'troubled', 'reckless', 'vivid', 'cockatoo', 'emerging', 'beyond', 'grieve', 'gaining', 'rejoice', 'victoriously', 'abating', 'neared', 'dying', 'word', 'sooner', 'wonderful', 'instinct', 'notified', 'keels', 'mile', 'rallied', 'ranks', 'battalions', 'looked', 'flashing', 'lines', 'stacked', 'bayonets', 'moved', 'redoubled', 'velocity', 'stripped', 'sprang', 'ash', 'hours', 'pulling', 'disposed', 'general', 'pausing', 'gave', 'animating', 'influence', 'strange', 'perplexity', 'inert', 'irresolution', 'perceive', 'compact', 'martial', 'columns', 'measureless', 'rout', 'king', 'porus', 'elephants', 'alexander', 'mad', 'consternation', 'directions', 'expanding', 'irregular', 'aimlessly', 'hither', 'thither', 'plainly', 'betrayed', 'distraction', 'paralysed', 'helplessly', 'logged', 'dismantled', 'flock', 'simple', 'sheep', 'pursued', 'pasture', 'fierce', 'wolves', 'excessive', 'timidity', 'characteristic', 'herding', 'banding', 'tens', 'lion', 'maned']
Length of vocabulary: 1000
UnTrained: i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i i
Trained, no prefix: us i boat was no yes a tens of the about him oars is at out him oars a tens i starbuck to the less a lake it both a oars i in the harpoon spring oars i it of whales came i boat was i as will he back
Trained, with a prefix: as soon heard i me you carry them i go shot in only of if from some a out an this vast i me near the head by the a the nursing me its mind i though the go as to up i now an vast black times they them
```

# ziplm

Useless but mildly interesting language model using compressors built-in to Python.

## Usage

You can "train" it using some training data:

```{python}
data = open(my_favorite_text_file).read().lower()
alphabet = "qwertyuiopasdfghjklzxcvbnm,.;1234567890 "
model = ziplm.ZipModel(alphabet, training=data)
"".join(model.sample_sequence(10)) # sample 10 characters from the alphabet
```

You can also run it without any training data, and just forward sample to see what kinds of patterns gzip likes:
```{python}
alphabet = "abc"
model = ziplm.ZipModel(alphabet)
"".join(model.sample_sequence(100)) # I get 'ccabcabcabcabcabcabcabcabcabcabcabcabcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbcbccabcbcbcbc'
```

You can also get the probability for a sequence:
```{python}
alphabet = "qwertyuiopasdfghjklzxcvbnm "
model = ziplm.ZipModel(alphabet)
model.sequence_logprob("this is my favorite string") # I get -83.8
```

You can also try using `bz2` and `lzma` as language models by passing them as the `compressor` argument to the model

```{python}
import lzma
model = ziplm.ZipModel(alphabet, compressor=lzma)
"".join(model.sample_sequence(100)) # I get 'cccbaaaaacccccabcacccbaaaaabaacaabaacaabaacaabaabacaaaaaaaaaaacccbabacaaaaaaaaaaaccccacaaccbaaaaaccc'
```

## Why does this "work"?

This works because of two facts:
1. A language model is nothing but a distribution on the next token given previous tokens, $p(x \mid c)$.
2. There is a general equivalence between *probability distributions* and *codes*.

The second point is what makes this interesting. Information theory tells us that we can derive codes from probability distributions. That is, if I have some datapoints $x$, and I know that they follow probability distribution $p(x)$, I can come up with a lossless binary code to encode the $x$ where the length of each code is $-\log_2 p(x)$. This code minimizes the average code length: the only way to get shorter average code length would be to go into the realm of lossy compression. This is called the Shannon Limit.

Since I can convert probability distributions to codes in this way, I can also convert codes to probability distributions. If I have a code (like gzip) that describes my datapoint with length $l(x)$ in binary, then that corresponds to a probability distribution $p(x) = 2^{-l(x)}$. If the code is $K$-ary, then the corresponding distribution is 
$$p(x) = K^{-l(x)}.$$ 

The ZipLM model works by converting code lengths to probabilities in this way. If I have a vocabulary of size $K$, and a string $c$, then the probability distribution for continuations $x$ is:
$$p(x \mid c) \propto K^{-l(cx)},$$
where the proportionality reflects the fact that we have to sum over the compressed lengths of $cx^\prime$ for all $x^\prime$ in the vocabulary. That's all there is to it.

## How well does it work?

It's pretty bad, but it doesn't generate total junk. Here I trained the gzip model in Moby Dick---from the [Project Gutenberg text](https://www.gutenberg.org/files/2701/2701-0.txt)---and the output at least has some recognizable parts:
```{python}
data = open("mobydick.txt").read().lower()
alphabet = "qwertyuiopasdfghjkl;'zxcvbnm,. "
model = ziplm.Model(alphabet, data)
"".join(model.sample_sequence(100)) 
```
This gives me
```{python}
"'theudcanvas. ;cm,zumhmcyoetter toauuo long a one aay,;wvbu.mvns. x the dtls and enso.;k.like bla.njv'"
```
which at least seems to have "long a one" in it.




