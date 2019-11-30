import csv

fp = open('/Users/peter/Downloads/ODN_Earnings.csv', 'r', encoding='utf8')
fpcsv = csv.reader(fp)
fpw = open('/Users/peter/Downloads/population.csv', 'w+', encoding='utf8')
fpcsvw = csv.writer(fpw)

title = next(fpcsv)
fpcsvw.writerow([title[1], title[4], title[5]])

zipcodes = ['85001','85002','85003','85004','85005','85006','85007','85008','85009','85010','85011','85012','85013','85014','85015','85016','85017','85018','85019','85020','85021','85022','85023','85024','85025','85026','85027','85028','85029','85030','85031','85032','85033','85034','85035','85036','85037','85038','85039','85040','85041','85042','85043','85044','85045','85046','85048','85050','85051','85053','85054','85060','85061','85062','85063','85064','85065','85066','85067','85068','85069','85070','85071','85072','85073','85074','85075','85076','85078','85079','85080','85082','85083','85085','85086','85087','85097','85098','85251','85253','85254','85281','85304','85306','85307','85308','85310','85331','85339','85353','85383','85392','85709']
dataTypes = ['population','total_earners','median_earnings','percent_with_earnings_1_to_9999','percent_with_earnings_10000_to_14999','percent_with_earnings_15000_to_24999','percent_with_earnings_25000_to_34999','percent_with_earnings_35000_to_49999','percent_with_earnings_50000_to_64999','percent_with_earnings_65000_to_74999','percent_with_earnings_75000_to_99999','percent_with_earnings_over_100000']

for line in fpcsv:
    zipcode = line[1][:5]
    dataType = line[4]
    if zipcode in zipcodes and dataType in dataTypes:
        tmp = [zipcode, line[4], line[5]]
        fpcsvw.writerow(tmp)

