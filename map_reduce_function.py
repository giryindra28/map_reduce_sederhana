from mrjob.job import MRJob
import re

kata_benda = re.compile(r"[\w']+")

class frekuensi_benda(MRJob):
    def mapper(self, _, value):
        for i in kata_benda.findall(value):
            yield (i.lower(),1)
    
    
    def reducer(self, key, values):
        yield (key,sum(values))

if __name__ == '__main__':
    frekuensi_benda.run()