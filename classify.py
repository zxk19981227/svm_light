from sklearn.datasets import fetch_20newsgroups
from tqdm import tqdm
import nltk
def find_ngrams(input_list, n):
  return zip(*[input_list[i:] for i in range(n)])
train_data=fetch_20newsgroups(subset='train')
news=fetch_20newsgroups(subset='test')
dataset=['./']
word_dict={}
bi_dict={}
glove_dict={}
data_set=[train_data,news]
file_path=['./learn/train/','./learn/test/']
for data,path in zip(data_set,file_path):
    bi_file=open(path+'bigram.txt','w',encoding='utf-8')
    uni_file=open(path+'unigram.txt','w',encoding='utf-8')
    glove_file=open(path+'glove.txt','w',encoding='utf-8')
    labels=data.target
    papers=data['data']
    for paper,label in tqdm(zip(papers,labels)):
        sentences=nltk.sent_tokenize(paper.lower())
        for sen in sentences:
            words=nltk.word_tokenize(sen)
            for word in words:
                if word not in word_dict.keys():
                    word_dict[word]=len(word_dict.keys())+1
            bi_word=find_ngrams(words,2)
            for bigr in bi_word:
                if bigr not in bi_dict.keys():
                    bi_dict[bigr]=len(bi_dict.keys())+1
    with open('glove.840B.300d.txt','r',encoding='utf-8') as f:
        for line in tqdm(f):
            infos=line.strip().split(' ')
            word=infos[0]
            if word=='unk' and word not in word_dict.keys():
                glove_dict[word]=[float(i) for i in infos[1:]]
            elif word in word_dict.keys():
                glove_dict[word] = [float(i) for i in infos[1:]]
    for paper,label in tqdm(zip(papers,labels)):
        sentences=nltk.sent_tokenize(paper.lower())
        curr_bi={}
        curr_un={}
        current_value=[0]*300
        word_num=0
        for sen in sentences:
            words=nltk.word_tokenize(sen)
            bis=find_ngrams(words,2)
            for word in words:
                if word in curr_un.keys():
                    curr_un[word]+=1
                else:
                    curr_un[word]=1
                if word in glove_dict.keys():
                    for i in range(300):
                        current_value[i]+=glove_dict[word][i]
                else:
                    for i in range(300):
                        current_value[i]+=glove_dict['unk'][i]
                word_num+=1
            for bi in bis:
                if bi not in curr_bi.keys():
                    curr_bi[bi]=1
                else:
                    curr_bi[bi]+=1
        for i in range(300):
            current_value[i]/=word_num
        res=[str(label+1)]
        res1=[str(label+1)]
        for key in sorted(curr_un.keys()):
            res1.append("{}:{}".format(word_dict[key],curr_un[key]))
        uni_file.write(' '.join(res1))
        uni_file.write('\n')
        res1=[str(label+1)]
        for key in sorted(curr_bi.keys()):
            res1.append("{}:{}".format(bi_dict[key], curr_bi[key]))
        bi_file.write(' '.join(res1))
        bi_file.write('\n')
        res=[str(label+1)]
        for i in range(300):
            res.append("{}:{}".format(i+1,current_value[i]))
        glove_file.write(' '.join(res))
        glove_file.write('\n')






