ops=['./svm_multiclass_learn','./svm_multiclass_classify']
model_name=['20newsbigram.bin','20newsunigram.bin','20newsglove.bin']
train_data_file=['20newsbigram.txt','20newsunigram.txt','20newsglove.txt']
test=['20newsbigram_test.txt','20newsunigram_test.txt','20newsglove_test.txt']
predict=['20newsbigram_predict.txt','20newsunigram_predict.txt','20newsglove_predict.txt']
outs=['20newsbigramlearn.txt','20newsunigramlearn.txt','20newsglovelearn.txt']
with open('run.sh','w') as f:
    op=ops[0]
    for model,train,te,pre,out in zip(model_name,train_data_file,test,predict,outs):
        re=[op,'-c 0.001',train,model,'>',out]
        print(' '.join(re))
    op=ops[1]
    for model,train,te,pre,out in zip(model_name,train_data_file,test,predict,outs):
        re=[op,te,model,'>','./predict/'+pre]
        print(' '.join(re))