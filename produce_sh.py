ops=['./svm_multiclass_learn','./svm_multiclass_classify']
model_name=['./learn/bigram.bin','./learn/unigram.bin','./learn/glove.bin']
train_data_file=['./learn/train/bigram.txt1','./learn/train/unigram.txt1','./learn/train/glove.txt']
test=['./learn/test/bigram.txt1','./learn/test/unigram_test.txt1','20newsglove_test.txt']
predict=['./learn/bigram_predict.txt','./learn/unigram_predict.txt','./learn/glove_predict.txt']
outs=['./learn/bigramlearn.txt','./learn/unigramlearn.txt','./learn/glovelearn.txt']
with open('run.sh','w') as f:
    op=ops[0]
    for model,train,te,pre,out in zip(model_name,train_data_file,test,predict,outs):
        re=[op,'-c 0.001',train,model,'>',out]
        print(' '.join(re))
    op=ops[1]
    for model,train,te,pre,out in zip(model_name,train_data_file,test,predict,outs):
        re=[op,te,model,'>','./predict/'+pre]
        print(' '.join(re))