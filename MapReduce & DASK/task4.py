from mrjob.job import MRJob
from mrjob.step import MRStep
import time

start_time = time.time()

class Sort_ID(MRJob):

    # This maps text and id to one key
    def mapper(self, _, line):
        line_arr = line.split(",")
        text = line_arr[1]
        id = int(line_arr[0])
        yield '', (id, text)
    
    # This reducer sorts tweets base on id
    def reducer(self, key, list):
        sorted_list = sorted(list, reverse=False)
        for text in sorted_list:
            _id, _text = text       
            yield _id, _text

end_time = time.time()
running_time = end_time - start_time
print('Running time:', running_time, 'seconds')
if __name__ == '__main__':
   Sort_ID.run()