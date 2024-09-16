import csv
data = 'vanamala_jayanth_quality_thought'
with open('kanna.csv', mode='w') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerows(data)

    # csv_reader = csv.reader(file)
    # for row in csv_reader:
    #     print(row)
