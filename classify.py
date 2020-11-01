from sklearn.datasets import fetch_20newsgroups
from tqdm import tqdm
import nltk
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])
news=fetch_20newsgroups(subset='test')
set_name=list(news.target_names)
set_dict={name:i for i,name in enumerate(set_name)}
dataset=['./']
word_dict={}
bi_dict={}

for data in tqdm(news.data):
    sentences=nltk.sent_tokenize(data)
    for sentence in sentences:
        words=nltk.word_tokenize(sentence)
        for word in words:
            if word not in word_dict.keys():
                word_dict[word]=len(word_dict.keys())+1
        pairs=find_ngrams(words,2)
        for pair in pairs:
            if pair not in bi_dict.keys():
                bi_dict[pair]=len(bi_dict.keys())+1
with open("20newsword_dict.txt",'w',encoding='utf-8') as f:
    for word in word_dict.keys():
       f.write('{} {}\n'.format(word,word_dict[word]))
glove_dict={}
with open('glove.840B.300d.txt', 'r', encoding='utf-8') as f:
    info = f.readline()
    cou=0
    while info !='':
        infos = info.split(' ')
        word = infos[0]
        if word=='unk':
            glove_dict[word]=infos[1:]
        elif word in word_dict.keys():
            glove_dict[word]=infos[1:]
        cou+=1
        info=f.readline()
        # if cou%1000==0:
        #     print(cou)
        # print(word)
with open('20newsglove_test.txt','w') as f:
    for name,data in tqdm(zip(news.filenames,news.data)):
        current_sum=[0]*300
        cou=0
        name=name.split('\\')[-2]
        sentences = nltk.sent_tokenize(data)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            for word in words:
                if word in glove_dict.keys():
                    cur_word=word
                else:
                    cur_word='unk'
                for i in range(300):
                    current_sum[i]+=float(glove_dict[cur_word][i])
                    cou+=1
        res=[str(set_dict[name]+1)]
        for i in range(300):
            current_sum[i]/=cou
            res.append(" {}:{}".format(i+1,str(current_sum[i])))
        f.write(' '.join(res))
        f.write('\n')
with open('20newsunigram_test.txt','w') as f:
    for name,data in tqdm(zip(news.filenames,news.data)):
        current_dict={}
        name=name.split('\\')[-2]
        sentences = nltk.sent_tokenize(data)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            for word in words:
                if word_dict[word] not in current_dict.keys():
                    current_dict[word_dict[word]]=1
                else:
                    current_dict[word_dict[word]]+=1
        res=[str(set_dict[name]+1)]
        for key in sorted(current_dict.keys()):
            res.append(" {}:{}".format(key,current_dict[key]))
        f.write(' '.join(res))
        f.write('\n')
current_bi={}
with open('20newsbigram_test.txt','w',encoding='utf-8') as f:
    for name,data in tqdm(zip(news.filenames,news.data)):
        current_bi={}
        name=name.split('\\')[-2]
        sentences = nltk.sent_tokenize(data)
        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            res=find_ngrams(words,2)
            for pars in res:
                if pars not in current_bi.keys():
                    current_bi[bi_dict[pars]]=1
                else:
                    current_bi[bi_dict[pars]]+=1
        res=[str(set_dict[name]+1)]
        for key in sorted(current_bi.keys()):
            res.append(" {}:{}".format(key,current_bi[key]))
        f.write(' '.join(res))
        f.write('\n')