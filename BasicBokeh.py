from bokeh.plotting import figure, show, output_file
import csv
import BasicScrape

output_file("basicPlot.html")

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
humidity = []
high = []
low = []

nan = float('nan')

with open(BasicScrape.weather_csv) as csv_file:
    humidity_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in humidity_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[2][0:2] != "--":
                high.append(int(row[2][0:2]))
            else:
                high.append(nan)

            if row[2][0:2] != "--":
                low.append(int(row[2][3:4]))
            else:
                low.append(int(row[2][2:3]))
            print(row[2][3:5])

            humidity.append(int(row[3][0:2]))

            line_count += 1
    print(f'Processed {line_count} lines.')

p = figure()

width = 5

p.line(x, high, line_width=width, color="red")
p.line(x, low, line_width=width, color="blue")
p.line(x, humidity, line_width=width, color="green")

show(p)
