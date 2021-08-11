import time
import json

class csv_json:
    def __init__(self):
        start_time = time.time()
        self.csv_file = open(r'./csv_file_to_be_converted.csv', 'r')
        self.lines = self.csv_file.readline()
        self.fie = self.lines.split(",")
        self.fields = []
        self.data = {}
        for x in self.fie:
            self.fields.append(x.replace("\n", ""))
        self.conversion()
        self.csv_file.close()
        print("CSV to JSON Successfully Completed!!!")
        print("-----Time taken to convert is %s seconds---------"%(time.time() - start_time))

    def convert_dict (self, a):
        init = iter(a)
        res_dct = dict(zip(init, init))
        return res_dct

    def conversion(self):

        self.lines = self.csv_file.readline()

        while self.lines:
            self.val = self.lines.split(",")
            self.values = []
            for x in self.val:
                self.values.append(x.replace("\n", ""))
            self.values_as_list = []
            for i in range(0, len(self.fields)):
                self.values_as_list.append(self.fields[i])
                self.values_as_list.append(self.values[i])
                row_dict = self.convert_dict(self.values_as_list)
            self.data[self.values[0]] = row_dict

            with open(r'./csv_to_json_converted.json', 'w') as jsonf:
                jsonf.write(json.dumps(self.data, indent=4))
            self.lines = self.csv_file.readline()









