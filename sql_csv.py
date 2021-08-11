import time
class sql_csv:
    def conversion(self):
        initial_time = time.time()

        #open sql file
        sql_file = open('./sql_file_to_be_converted.sql','r')
        lines = sql_file.readline()
        #parsing till the Insert line is found
        while True:
            if("INSERT" in lines or "insert" in lines):
                break
            lines = sql_file.readline()

        headings = lines.split("(")                             #Splitting using open paranthesis
        headings = headings[1].split(")")                       #previously splitted is again splitted using closing paranthesis
        headings = headings[0].replace("`", "")                 #removing backtics
        headings = headings.replace(" ", "")                    #removing backspaces
        write_file = open(r'./sql_to_csv_converted.csv','w')    #opening file to write
        write_file.write(headings)                              #writing the first row(headings)
        write_file.write('\n')                                  #making cursor to go to next line

        lines = sql_file.readline()                             #reading the data
        while lines:
            values = lines.split("(")                           #spliting the actual values using paranthesis
            values = values[1].split(")")
            values = values[0].replace("'", "")                 #removing single quotes
            values = values.replace(" ", "")                    #removing white spaces

            write_file.write(values)                            #writing the files
            write_file.write('\n')                              #inserting the new line character

            lines = sql_file.readline()                         #reading next line from the file

        write_file.close()                                      #output file is closed
        sql_file.close()                                        #input file is closed
        print("SQL to CSV Conversion is Successfully Completed!!!")
        print("--------Time taken for this conversion is %s seconds-------" %(time.time()-initial_time))
