# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from gensim import corpora, models, similarities

# <codecell>

documents=[]
for line in open('ghalib-concordance/output/lemma_documents.txt').readlines():
    documents.append(line.strip())

# kii should not be there
stoplist=['lenaa','honaa','karnaa','ko','jis','jo','kih','kyaa','me;n','par','to','nahii;n','kaa','har','kis','kii','nah',          'aur',
'tamaam',
'bhii',

'chaahiye',
'hogaa',
'rahnaa',
'kabhii',
'tujhe',
'kisii',
'ham',
'lagnaa',
'ik',
'in',
':tara;h',
'liye',
'ne',
'kyuu;n',
'bahut',
'mat',
'yuu;n',
'so',
'magar',
'hotaa',
'pahle',
'ek',
'kahaa;n',
'ko))ii',
'yih',
'dast',
'honaaa',##### ERRROR
'jise',
'tuu',
'yaa;n',
'mai;n',
'teraa',
'haa;n',
'denaa',
'yaa',
'ab',
'ay',
'az',
'itnaa',
'tumhaaraa',
'agar',
'vale',
'kuchh',
'abhii',
'kyuu;nkar',
'lekin',
'hote',
'kab',
'hii',
'aap',
'gar',
'yihii',
'aisaa',
'us',
'un',
'vuhii',
'dekho', #### <- ERROR
'use',
'taa',
'tab',
'se',
'ho',
'jab',
'jaa',
'hotii', ##### <— ERROR
'tujh',
'vaa;n',
'varnah',
'achchhaa',
'jitnaa',
'saknaa',
'meraa',
'apnaa']


texts = [[word for word in document.lower().split() if word not in stoplist]
           for document in documents]
texts[0:5]

# <codecell>

all_tokens = sum(texts, [])
tokens_once = set(word for word in set(all_tokens) if all_tokens.count(word) == 1)
texts = [[word for word in text if word not in tokens_once]
         for text in texts]

# <codecell>

tokens_once # interesting...

# <codecell>

print(texts[0:5])

# <codecell>

s=set(word for word in set(all_tokens))

# <codecell>

for x in s:
    count = all_tokens.count(x)
    if count>5:
        print "'"+x+"',"

# <codecell>


