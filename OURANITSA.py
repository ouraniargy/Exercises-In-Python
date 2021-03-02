import urllib.request
import json
import datetime


def getUrl():
    for day in range(1, Day + 1):
        if day < 10:
            url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + month + "-0" + str(
                day) + "/" + month + "-0" + str(day)
            #ΠΑΙΡΝΟΥΜΕ ΤΟ ΣΗΜΕΡΙΝΟ URL
        else:
            url = "https://api.opap.gr/draws/v3.0/1100/draw-date/" + month + "-" + str(
                day) + "/" + month + "-" + str(day)

        FREQ(url, day)


def FREQ(url, day):
    counter = []
    for i in range(81):
        counter.append(0)

    r = urllib.request.urlopen(url)
    html = r.read()
    html = html.decode()
    data = json.loads(html, strict=False)

    for draw in data["content"]:
        t = draw["winningNumbers"]["list"]
        # PAIRNOYME TH LISTA ME TOUS ARI8MOUS
        for indice in t:
            counter[indice] += 1

    max = counter[0]
    maxNum = 0

    for num in range(81):
        if max < counter[num]:
            max = counter[num]
            maxNum = num

    print("ΟΙ ΠΙΟ ΣΥΧΝΑ ΕΜΦΑΝΙΖΟΜΕΝΟΙ ΑΡΙΘΜΟΙ ΤΗΝ ΗΜΕΡΑ %s-%s ΕΙΝΑΙ:" % (month, day), end=" ")

    for num in range(maxNum, 81):
        if counter[num] == max:
            print("%s" % (num), end=' ')

    print("\n")


month = datetime.date.today().strftime("%Y-%m")

Day = datetime.date.today().day

getUrl()