from mrjob.job import MRJob
import re

class Count_City(MRJob):
    def mapper(self, _, line):
            yield line, 1
    def reducer(self, city, counts):
        yield city, sum(counts)

if __name__ == "__main__":
    Count_City.run()