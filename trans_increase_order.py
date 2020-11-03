file_names=["D:/prog/python/gitlab/svm/imdb_for_zijun/test/bi.txt","D:/prog/python/gitlab/svm/imdb_for_zijun/test/single.txt"]
for file in file_names:
    with open(file,'r',encoding='utf-8') as f:
        raw=f.readlines()
    with open(file+'1','w',encoding='utf-8') as f:
        for line in raw:
            cur_di={}
            info=line.split()
            label=info[0]
            for each in info[1:]:
                eachs=each.split(':')
                cur_di[int(eachs[0])]=int(eachs[1])
            res=[label]
            for key in sorted(cur_di.keys()):
                res.append("{}:{}".format(key,cur_di[key]))
            f.write(' '.join(res))
            f.write('\n')
