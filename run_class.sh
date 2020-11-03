./svm_multiclass_learn -c 0.01 ./learn/train/bigram.txt1 ./learn/bigram.bin > ./learn/bigramlearn.txt
./svm_multiclass_learn -c 0.01 ./learn/train/unigram.txt1 ./learn/unigram.bin > ./learn/unigramlearn.txt
./svm_multiclass_learn -c 0.01 ./learn/train/glove.txt ./learn/glove.bin > ./learn/glovelearn.txt
./svm_multiclass_classify ./learn/test/bigram.txt1 ./learn/bigram.bin > ./learn/bigram_predict.txt
./svm_multiclass_classify ./learn/test/unigram.txt1 ./learn/unigram.bin > ./learn/unigram_predict.txt
./svm_multiclass_classify ./learn/test/glove_test.txt ./learn/glove.bin > ./learn/glove_predict.txt