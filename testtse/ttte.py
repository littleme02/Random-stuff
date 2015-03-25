
import requests
import csv

urltaken= "https://www.geekevents.org/seatmap/taken_seats/75/"
url = "https://www.geekevents.org/seatmap/seat_info/75/"

seatsx = 12
seatsy = 44
seatstart = 49867

payload = {"row_name":"8", "seat_name": "25"}
cookies = {"sessionid": "v6k3vocixdtgqog2hb8wl5yqc8yovgpj"}




t = (requests.post(urltaken, cookies=cookies)).json()

totalseat = len(t)
seated = 0
unseated = 0

x = 0
y = 0

with open('name.csv', 'w',encoding='utf-8', newline='') as fp:
    a = csv.writer(fp, delimiter=',')
    data = [["Name","Tag","Row","Seat"]]
    for x in range (seatsx):
        for y in range (seatsy):

            seatnumber = (seatstart + ((x * seatsy) + y+1))

            if str(seatnumber) in t:

                payload = {"row_name":str(x+1), "seat_name": str(y+1)}

                r = requests.post(url, data =payload, cookies=cookies)

                if  (r.json()["taken"]) == 1:
                    name = (r.json()["taken_by"])
                    row = (r.json()["row"])
                    seat = (r.json()["seat"])
                    sname = (name.split(" a.k.a "))
                    name = sname[0]
                    if (len(sname)== 2):
                        tag = sname[1]
                    else:
                        tag = " "
                data.append([name,tag, row, seat])
                #print("Row " +str(row) + " Seat " + str(seat))
                seated = seated + 1
            else:
                #print("Row " + str(x+1) + "  Seat " + str(y+1) + " is empty")
                unseated = unseated + 1
            print("% " + str(seated/totalseat*100))
            #print("seated " + str(seated) + " vacant seats " + str(unseated))
        y = y + 1
    x = x + 1
    a.writerows(data)
    print("seated " + str(seated))
    print("vacant seats " + str(unseated))
    print("total " +str(seated+unseated))

