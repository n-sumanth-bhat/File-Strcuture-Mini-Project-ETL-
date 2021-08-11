import time
class json_csv:
    def conversion(self):
        starting_time = time.time()
        heading = []
        j_file = open(r'./json_file_to_be_converted.json', 'r')
        csv_file = open(r'./json_to_csv_converted.csv','w')

        j_lines = j_file.readline()
        while('}' not in j_lines):
            values = j_lines.split(":")
            if(len(values) > 1 ):
                if(values[0] != '\n' and '{' not in values[0] and '}' not in values[0] and '{' not in values[1] ):
                    ans = values[0].replace('"', '')
                    ans = ans.replace('/','')
                    ans = ans.replace('\\','')
                    ans = ans.replace('}', '')
                    ans = ans.replace(" ", "")
                    heading.append(ans)

            j_lines = j_file.readline()
        headingAsCsv = ','.join(heading)
        csv_file.write(headingAsCsv)
        csv_file.write('\n')
        j_file.close()

    ##Writing data to the file
        j_file = open(r'./json_file_to_be_converted.json', 'r')
        j_lines = j_file.readline()
        while(True):
            data_values = []
            while('}' not in j_lines):

                values = j_lines.split(":")
                if(len(values) > 1 ):
                    if(values[1] != '\n' and '{' not in values[1] and '}' not in values[1]):
                        ans = values[1].replace('{', '')
                        ans = ans.replace('"', '')
                        ans = ans.replace('/','')
                        ans = ans.replace('\\','')
                        ans = ans.replace('\n','')
                        ans = ans.replace('}', '')
                        ans = ans.replace(" ","")
                        ans = ans.replace(",",'')
                        data_values.append(ans)

                j_lines = j_file.readline()
            j_lines = j_file.readline()
            data = ','.join(data_values)
            csv_file.write(data)
            csv_file.write('\n')
            if(j_lines == ''):
                break
        csv_file.close()
        j_file.close()
        print("JSON to CSV task Successfully Completed!!!")
        print("-----Time taken to convert is %s seconds---------"%(time.time() - starting_time))


