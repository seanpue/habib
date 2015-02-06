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
';haalaa;nkih',
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
'apnaa'
'phir',
'bah',
'pah',
'milnaa',
'phir',
'aanaa'

]


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

dictionary = corpora.Dictionary(texts)

# <codecell>

dictionary.save('tmp/ghalib.dict')

# <codecell>

print(dictionary)

# <codecell>

print(dictionary.token2id)

# <codecell>

corpus = [dictionary.doc2bow(text) for text in texts]

# <codecell>

lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=10, update_every=1, chunksize=1, passes=5)

# <codecell>

lda.print_topics(10)

# <codecell>


