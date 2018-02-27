import urllib.request
import feedparser
import Testmod


#it may be a better idea to use cusips instead of company names
# Filings may have to be adjusted because of column 7 
# could use equity long bias barclay index
# '0001166309' has strange table name
listOfFunds=['0001336528','0001103804','0000921669','0001569049','0001214822','0001277050','0001401388','0001510589','0001316622','0001107310','0001517857','0001656456','0001062589', '0001499066', '0001469026', '0001340614', '0001592476', '0001569064','0000934639', '0001166850', '0001569175']
base_url = 'http://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&'
n='nameOfIssuer'
a='sshPrnamt'
allowable_filings=['13F-HR', '13F-HR/A']
l=[]
for fund in listOfFunds:
    CIK=fund
    CIKs='CIK=%s&CIK=%s' %(CIK,CIK)
    end_url = '&type=&dateb=&owner=exclude&start=0&count=40&output=atom'
    query=base_url+CIKs+end_url    
    response = urllib.request.urlopen(query).read()
    feed = feedparser.parse(response)
    for i in range(19):
        if feed.entries[i]['filing-type'] not in allowable_filings:
            break
        s=feed.entries[i]['filing-href']
        date=feed.entries[i]['filing-date']
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:10])
        info=Testmod.Filing(year, month, day,CIK)
        s2=s[:len(s)-30]+'infotable.xml'
        s3=s[:len(s)-30]+'form13fInfoTable.xml'
        try:
            file = urllib.request.urlopen(s3).read()
        except urllib.error.HTTPError:
            file= urllib.request.urlopen(s2).read()
        #file = urllib.request.urlopen(s2).read()
        f=file.decode('utf8')
        reduced_f=f
        info.d={}
        while reduced_f.find(n)!=-1:
            cstart=reduced_f.find(n)
            cend=reduced_f[cstart+12:].find(n)
            cname=reduced_f[cstart+13:cstart+12+cend-2]
            reduced_f=reduced_f[cstart+24+cend:]
            astart=reduced_f.find(a)
            aend=reduced_f[astart+9:].find(a)
            amt=reduced_f[astart+10:astart+9+aend-2]
            info.addToD(cname, int(amt))
        l.append(info)
