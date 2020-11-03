import sys
import os
import nltk
from tqdm import tqdm
def find_ngrams(input_list, n):
    return zip(*[input_list[i:] for i in range(n)])
data_set=['./imdb_for_zijun/train/','./imdb_for_zijun/test/']
setname=['pos/','neg/']
train_data=['']
# label_name=['neg','pos']
word_dict={}
glove_dict={}
bi_dict={}
ibdm_unigram=open('./ibdmunigram.txt','w')
for dir in data_set:
    sing_file = open(dir + 'single.txt', 'w')
    bi_file = open(dir + 'bi.txt', 'w')
    glove_file = open(dir + 'glove.txt', 'w')
    for i in range(len(setname)):
        current_dir=dir+setname[i]
        file_list=os.listdir(current_dir)
        for file in tqdm(file_list):
            with open(current_dir+file,'r',encoding='utf-8') as f:
                single={}
                bi={}
                lines=f.readlines()
                for line in lines:
                    words=nltk.word_tokenize(line.strip().lower())
                    biword=find_ngrams(words,2)
                    for word in words:
                        word=word.strip()
                        if word not in word_dict.keys():
                            word_dict[word]=len(word_dict.keys())+1
                    for bi in biword:
                        if bi not in bi_dict.keys():
                            bi_dict[bi]=len(bi_dict.keys())+1
        with open("glove.840B.300d.txt",'r',encoding='utf-8') as f:
            for line in tqdm(f):
                info=line.strip().split(' ')
                if (info[0] == 'unk') or info[0] in word_dict.keys() and (info[0] not in glove_dict.keys()):
                    glove_dict[info[0]]=[float(i) for i in info[1:]]
        for file in tqdm(file_list):
            with open(current_dir+file,'r',encoding='utf-8') as f:
                single={}
                bigram={}
                lines=f.readlines()
                for line in lines:
                    words=nltk.word_tokenize(line.strip().lower())
                    biword=find_ngrams(words,2)
                    for word in words:
                        if word not in single.keys():
                            single[word]=1
                        else:
                            single[word]+=1
                    for bi in biword:
                        if bi not in bigram.keys():
                            bigram[bi]=1
                        else:
                            bigram[bi]+=1
                if i==0:
                    res=['-1']
                else:
                    res=['1']
                for key in sorted(single.keys()):
                    res.append('{}:{}'.format(word_dict[key],single[key]))
                sing_file.write(' '.join(res))
                sing_file.write('\n')
                if i==0:
                    res=['-1']
                else:
                    res=['1']
                for key in sorted(bigram.keys()):
                    res.append('{}:{}'.format(bi_dict[key],bigram[key]))
                bi_file.write(' '.join(res))
                bi_file.write('\n')
                su=[0]*300
                for key in single.keys():
                    if key in glove_dict.keys():
                        tmp_sum=glove_dict[key]
                    else:
                        tmp_sum=glove_dict['unk']
                    for j in range(300):
                        su[j]+=tmp_sum[j]
                for j in range(300):
                    su[j] /= len(single.keys())
                if i==0:
                    res=['-1']
                else:
                    res=['1']
                for j in range(300):
                    res.append("{}:{}".format(j+1,su[j]))
                glove_file.write(' '.join(res))
                glove_file.write('\n')




