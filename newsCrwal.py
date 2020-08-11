import csv

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

titleList = []
dateList = []
summaryList = []
sourceList = []


def getNewsCount(term, begDate, endDate):
    global titleList
    global dateList
    global summaryList
    global sourceList
    # chrome_path = "chromedriver.exe"
    # driver = webdriver.Chrome(chrome_path)
    count = 0
    bDate = begDate.split('/')

    eDate = bDate
    index = 1
    totalCount = 0
    proxies = {
        'http': 'http://185.93.3.123',
        'https': 'http://10.10.1.10:1080',
    }
    while index != 0:
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(chrome_options=chrome_options)

        site = 'https://www.google.com/search?q=Dow Jones&tbs=cdr:1,cd_min:' + bDate[0] + '/' + bDate[1] + '/' + bDate[
            2] + ',cd_max:' + bDate[0] + '/' + bDate[1] + '/' + bDate[
                   2] + '&tbm=nws&sxsrf=ALeKk01YnPYYTSzH7Vz2bgUltLs-c-Wj6g:1582791155826&ei=83lXXvH8MYualwTls5CwDQ&start=' + str(
            count) + '&sa=N&ved=0ahUKEwixwuLEpPHnAhULzYUKHeUZBNYQ8tMDCFE&biw=819&bih=618&dpr=1'
        # hdr = {
        #     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        #     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        #     'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        #     'Accept-Encoding': 'none',
        #     'Accept-Language': 'en-US,en;q=0.8',
        #     'Connection': 'keep-alive'}
        # site2 = 'https://www.google.com/search?q=Dow Jones&tbs=cdr:1,cd_min:3/6/2013,cd_max:3/6/2013&tbm=nws&sxsrf=ALeKk01YnPYYTSzH7Vz2bgUltLs-c-Wj6g:1582791155826&ei=83lXXvH8MYualwTls5CwDQ&start=10&sa=N&ved=0ahUKEwixwuLEpPHnAhULzYUKHeUZBNYQ8tMDCFE&biw=819&bih=618&dpr=1'
        # req = urllib.request.Request(site2, headers=hdr)
        # req=requests.get(site, proxies=proxies)
        # print(req.text)
        driver.get(site)
        try:
            # page = urllib.request.urlopen(req)
            row = driver.find_elements_by_class_name('gG0TJc')
            for i in range(len(row)):
                title = (row[i].find_element_by_tag_name('a')).text
                tempSource = row[i].find_element_by_class_name('dhIWPd')
                source = ((tempSource.find_elements_by_tag_name('span'))[0]).text
                date = ((tempSource.find_elements_by_tag_name('span'))[2]).text
                summary = (row[i].find_element_by_class_name('st')).text
                with open('newsPart1.csv', 'a', newline='', encoding='utf-8') as f:
                    rowList = [title, source, date, summary]
                    tempDic = []
                    w = csv.writer(f)
                    w.writerow(rowList)
                    f.close()
                titleList.append(title)
                sourceList.append(source)
                dateList.append(begDate)
                summaryList.append(summary)
            index = len(row)
            # html = page.read()
            # index = str(html).count("class=\"gG0TJc\"")
            totalCount = totalCount + index

            if (index != 0):
                count = count + 10
        except Exception as e:
            if 'Too Many Requests' in str(e):
                return 'error'
            return 0

        driver.quit()
        # html = page.read()
        # index = str(html).count("class=\"gG0TJc\"")
        # totalCount = totalCount + index
        # if (index != 0):
        #     print(index)
        #     count=count+10
    print(begDate + ',' + str(totalCount))
    return totalCount
    # print(index)
    # return html[index:index + 100].partition(' ')[0]


# print(getNewsCount("AAPL", "3/4/2013", "3/4/2013"))
df = pd.read_csv('C:/Users/TanzeelKhan/PycharmProjects/AAPL_Stock_news/News_AAPL/Scrape2Dates.csv')
dates = df['date'].tolist()

CountList = []
dateCount = []
for i in range(len(dates)):
    print(str(dates[i]).split(' ')[0])
    newscount = getNewsCount("AAPL", str(dates[i]).split(' ')[0], str(dates[i]).split(' ')[0])
    if 'error' in str(newscount):
        break
    dateCount.append(dates[i])
    CountList.append(newscount)
df2 = pd.DataFrame()
df2['dates'] = dateList
df2['source'] = sourceList
df2['titles'] = titleList
df2['summary'] = summaryList

df2.to_csv('newscheck.csv')
