from csv_json import csv_json
from json_csv import json_csv
from sql_csv import sql_csv

class driver_code:
    def main(self):
        print("Enter the corresponding number for the operation you want to perform.")
        print("1. Convert CSV to JSON ")
        print("2. Convert JSON to CSV")
        print("3. Convert SQL to CSV")
        choice = input()
        if(choice == '1'):
            c2j = csv_json()
        elif(choice == '2'):
            j2c = json_csv()
            j2c.conversion()
        elif(choice == '3'):
            s2c = sql_csv()
            s2c.conversion()
        else:
            print("Please Enter a valid input!!!")

if __name__ == '__main__':
    driver_code().main()
