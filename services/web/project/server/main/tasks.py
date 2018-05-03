# services/web/server/main/views.py


try:
    from pyspark import SparkContext, SparkConf
    from operator import add
except:
    print('error')


def tokenize(text):
    return text.split()


def create_task_file():
    conf = SparkConf().setAppName('letter count')
    sc = SparkContext(conf=conf)
    files = sc.textFile("file1.csv")
    words = files.flatMap(tokenize)
    counts = words.map(lambda word: (word, 1)).reduceByKey(add).collect()
    return dict(counts)


def create_task_test():
    conf = SparkConf().setAppName('letter count')
    sc = SparkContext(conf=conf)
    words = 'test teste1 test teste1'
    seq = words.split()
    data = sc.parallelize(seq)
    counts = data.map(lambda word: (word, 1)).reduceByKey(add).collect()
    sc.stop()
    return dict(counts)
