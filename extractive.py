import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
import en_core_web_sm
from heapq import nlargest

def extract(text):
    try:
        stopwords =list(STOP_WORDS)
        nlp = en_core_web_sm.load()
        doc=nlp(text)

        tokens=[token.text for token in doc]

        word_freq={}
        for word in doc:
            if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text] = 1
                else:
                    word_freq[word.text] +=1

        max_freq= max(word_freq.values())

        for word in word_freq.keys():
            word_freq[word]=word_freq[word]/max_freq

        sent_tokens=[sent for sent in doc.sents]

        sent_scores={}
        for sent in sent_tokens:
            for word in sent:
                if word.text in word_freq.keys():
                    if sent not in sent_scores.keys():
                        sent_scores[sent]=word_freq[word.text]
                    else:
                        sent_scores[sent]+=word_freq[word.text]

        select_len=int(len(sent_tokens)*0.3)
        if select_len<1:
            select_len=1


        summary=nlargest(select_len,sent_scores,key=sent_scores.get)
    except Exception as e:
        print('exception occured')
    result=''
    for i in summary:
        result +=str(i)
    if(len(result.split())>800):
        res_words=result.split()
        res_words=res_words[0:800]
        result=' '.join(res_words)
    return result
