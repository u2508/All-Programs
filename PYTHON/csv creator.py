header = ['serial no.', 'description', 'amount']
data = [['taxi',640], ['auto', 300], ['taxi',632],['auto', 350],['train', 2500],['tiffin & supplies', 800],
        ['snacks', 200],['daily auto', 800],['meals', 5000],['daily milk &snacks', 1250],['laundry', 300],
        ['snacks',280],['team dinner',600],]
filename = 'excel.csv'
sum=0
with open(filename, 'w+') as file:
    for head in header:
        if head==header[-1]:
            file.write(str(head).title())
        else:
            file.write(str(head).title()+', ')
    file.write('\n')
    for row in range(len(data)):
        file.write(str(row+1)+', ')
        for x in data[row]:
            if x==data[row][-1]:
                file.write(str(x))
                sum+=x
            else:
                file.write(str(x).title()+', ')
        if row==len(data)-1:
            file.write(f"\nTotal ,  {sum}")
        else:
            file.write('\n')
