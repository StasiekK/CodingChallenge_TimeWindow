#Coding Challenge from https://www.youtube.com/watch?v=kbwk1Tw3OhE 10.X.2020.
#My solution, time about 60 minutes
#

#sample data, 
calendar_inter = [['9:00','10:30'],['12:00','13:00'],['16:00','18:00']]
daybound_inter = ['9:00','20:00']
calendar_me = [['10:00','11:30'],['12:30','14:30'],['14:30','15:00'],['16:00','17:00']]
daybound_me = ['10:00','18:30']
timeneed = 30

def stasunix(ctime,way):
    if way == 'tounix':
        ctime = ctime.split(':')
        return int(ctime[0])*60 + int(ctime[1])
    elif way == 'totime':
        return f'{notpossibletime[j][1]//60}:{notpossibletime[j][1]%60:02}'

inttimechanged, metimeschanged = list(), list()

for blok in calendar_inter:
        inttimechanged.append([stasunix(blok[0],'tounix'),stasunix(blok[1],'tounix')])
for blok in calendar_me:
        metimeschanged.append([stasunix(blok[0],'tounix'),stasunix(blok[1],'tounix')])

timewindowinter = [stasunix(daybound_inter[0],'tounix'),stasunix(daybound_inter[1],'tounix')]
timewindowme = [stasunix(daybound_me[0],'tounix'),stasunix(daybound_me[1],'tounix')]
daystart, dayend = max(timewindowinter[0], timewindowme[0]),min(timewindowinter[1], timewindowme[1])

possibletime, notpossibletime = list(), list()
for i in inttimechanged:
    notpossibletime.append(i)
for i in metimeschanged:
    notpossibletime.append(i)
notpossibletime.append([daystart,daystart])
notpossibletime.append([dayend,dayend])
notpossibletime.sort()

j = 0
while j < len(notpossibletime)-1:
    if notpossibletime[j][1]+ timeneed <=notpossibletime[j+1][0]:
        possibletime.append([stasunix(notpossibletime[j][1],'totime'), stasunix(notpossibletime[j+1][0],'totime')])
    j+=1

print('possibletime:\n', possibletime)