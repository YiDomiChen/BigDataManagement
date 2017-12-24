from pyspark import SparkConf, SparkContext
import sys


def map_date(info):    
    return ("%02d" % int(info[1].split("/")[0]) + "/" + info[1].split("/")[2].split(' ')[0], int(info[5]))

def print_res(result):
    for r in result:
        print r

def busy_month(filename):    
    sc=SparkContext()
    lines = sc.textFile("lax_passengers.csv")

    terminals = ["Terminal 1", "Terminal 2", "Terminal 3", "Terminal 4", "Terminal 5", "Terminal 6", "Terminal 7", "Terminal 8", "Tom Bradley International Terminal"]

    passenger_info = lines.map(lambda s : s.split(','))
    #print(passenger_info.collect())
    time_info = passenger_info.filter(lambda y: y[2] in terminals).map(map_date)

    # print(time_info.collect())
    res = time_info.reduceByKey(lambda x, y: int(x) + int(y)).filter(lambda y: y[1] > 5000000).sortByKey().collect()
    print("============Start=================")
    print_res(res)
    print("============End=================")

def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    busy_month(sys.argv[1])

if __name__ == '__main__':
    main()