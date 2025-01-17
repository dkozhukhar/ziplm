import gzip
import bz2
import lzma
import urllib.request
import re
import numpy as np
import scipy.special
from collections import Counter

class ZipModel:
    def __init__(self, vocabulary, training="", compressor=gzip, conversion=np.log(256)):
        self.vocabulary = vocabulary
        self.training = training
        self.compressor = compressor
        self.conversion = conversion
        self.index = {v:i for i, v in enumerate(self.vocabulary)}

    def logprobs(self, prefix="", temperature=1):
        code_lengths = np.array([
            len(self.compressor.compress(" ".join([self.training, prefix, v]).encode()))
            for v in self.vocabulary
        ])
        return scipy.special.log_softmax(-code_lengths*self.conversion*(1/temperature))
                                         
    def sequence_logprob(self, sequence, prefix="", temperature=1):
        score = 0.0
        for x in sequence.split():
            scores = self.logprobs(prefix, temperature=temperature)
            score += scores[self.index[x]]
            prefix += " " + x
        return score

    def sample(self, prefix="", temperature=1):
        scores = self.logprobs(prefix, temperature=temperature)
        i = np.random.choice(range(len(self.vocabulary)), p=np.exp(scores))
        return self.vocabulary[i]

    def sample_sequence(self, maxlen, prefix="", temperature=1):
        sequence = prefix
        for k in range(maxlen):
            result = self.sample(sequence, temperature=temperature)
            yield result
            sequence += " " + result

