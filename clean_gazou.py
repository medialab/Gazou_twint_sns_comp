import csv

with open("holdup_gazou.csv") as f1, open("clean_holdup_gazou.csv",'w') as f2:
    file_content1_reader = csv.reader(f1)
    file2_writer = csv.writer(f2)
    while True:
        try:
            row = file_content1_reader.__next__()
            file2_writer.writerow(row)
        except csv.Error:
            print("Error")
        except StopIteration:
            print("Iteration End")
            break
