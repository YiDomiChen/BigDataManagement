from pyspark import SparkConf, SparkContext
import sys

def map_flights(info):
    return ((info[0][0].split("/")[1], info[0][1]), int(info[1]))
def map_flights_month(info):
    return (("%02d" % int(info[1].split("/")[0]) + "/" + info[1].split("/")[2].split(' ')[0], info[3]), int(info[5]))

def print_res(result):
    for r in result:
        print r

def avg_num_flights(filename):
    sc=SparkContext()
    lines = sc.textFile(filename)

    flights_info = lines.map(lambda s: s.split(',')).map(map_flights_month).reduceByKey(lambda x, y: x + y)
    sum_info = flights_info.map(map_flights).aggregateByKey((0, 0), lambda a, b: (a[0] + b, a[1] + 1), lambda a, b: (a[0] + b[0], a[1] + b[1]))
    print("==========Start=================")
    avg_info = sum_info.map(lambda ((a, b), (x, y)): ((a, b), int(float(x) / y)))
    print_res(avg_info.sortByKey(True).map(lambda ((x,y), z): (x, y, z)).collect())
    print("==========End=================")


def main():
    if len(sys.argv) != 2:
        print 'invalid parameters'
        exit(1)
    avg_num_flights(sys.argv[1])

if __name__ == '__main__':
    main()