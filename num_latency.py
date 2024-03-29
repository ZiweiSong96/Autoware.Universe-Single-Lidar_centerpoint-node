import csv
import matplotlib.pyplot as plt

def calculate_drawing(csv_file1,csv_file2,save_path):
    x_values=[]
    y_values=[]

    with open(csv_file1,'r') as csvfile1:
        reader1=csv.reader(csvfile1)
        next(reader1)
        for row1 in reader1:
            x_values.append(float(row1[0]))
    
    with open(csv_file2,'r') as csvfile2:
        reader2=csv.reader(csvfile2)
        next(reader2)
        for row2 in reader2:
            y_values.append(float(row1[1])/(float(row2[1])*1000))
    plt.plot(x_values,y_values)
    plt.xlabel('Time stamp')
    plt.ylabel('Num/Latency')

    #x_ticks=range(10800,11051,10)
    #x_ticks_labels=[str(x) for x in x_ticks]
    #plt.xticks(x_ticks,x_ticks_labels)
    #plt.xlim(min(x_values),max(x_values))
    #plt.ylim(0,20000)
    plt.savefig(save_path)
    plt.close()

csv_file1='/home/mlabszw/autoware_singlenode/evaluate/input_pointcloud_num.csv'
csv_file2='/home/mlabszw/autoware_singlenode/evaluate/latency.csv'
save_path='/home/mlabszw/autoware_singlenode/evaluate/Num_vs_Latency.png'

calculate_drawing(csv_file1,csv_file2,save_path)
print('Down!')
