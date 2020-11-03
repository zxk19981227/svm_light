./svm_learn -c 0.01 ./imdb_for_zijun/train/bi.txt1 ./imdb_for_zijun/bi.bin >log.txt
./svm_learn -c 0.01 ./imdb_for_zijun/train/single.txt1 ./imdb_for_zijun/single.bin >log.txt
./svm_learn -c 0.01 ./imdb_for_zijun/train/glove.txt ./imdb_for_zijun/glove.bin >log.txt
./svm_classify ./imdb_for_zijun/test/bi.txt1 ./imdb_for_zijun/bi.bin ./imdb_for_zijun/bi_pre.txt>log.txt
./svm_classify ./imdb_for_zijun/test/single.txt1 ./imdb_for_zijun/single.bin ./imdb_for_zijun/single_pre.txt>log.txt
./svm_classify  ./imdb_for_zijun/test/glove.txt ./imdb_for_zijun/glove.bin