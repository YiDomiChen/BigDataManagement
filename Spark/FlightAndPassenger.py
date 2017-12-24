from pyspark import SparkConf, SparkContext
import sys

def map_passenger(info):
    return (("%02d" % int(info[1].split("/")[0]) + "/" + info[1].split("/")[2].split(' ')[0], info[3], info[4]), int(info[5]))
def map_flights(info):
    return (("%02d" % int(info[1].split("/")[0]) + "/" + info[1].split("/")[2].split(' ')[0], info[3], info[4]), int(info[5]))

def print_res(result):
    for r in result:
        print r


def flight_and_passenger(flightfile, passengerfile):
    sc=SparkContext()
    passenger_lines = sc.textFile(flightfile)
    flight_lines = sc.textFile(passengerfile)

    passenger_info = passenger_lines.map(lambda s: s.split(',')).map(map_passenger).reduceByKey(lambda x, y: x + y)
    flight_info = flight_lines.map(lambda s: s.split(',')).map(map_flights).reduceByKey(lambda x, y: x + y)

    joint_info = flight_info.join(passenger_info)
    print "===============Start================="
    print_res(joint_info.sortByKey(True).map(lambda ((x, y, z), (a, b)): (x, y, z, b, a)).collect())
    print "===============End================="


def main():
    if len(sys.argv) != 3:
        print 'invalid parameters'
        exit(1)
    flight_and_passenger(sys.argv[1], sys.argv[2])

if __name__ == '__main__':
    main()