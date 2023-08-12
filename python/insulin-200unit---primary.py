# Victor W Zhong, Juhaeri Juhaeri, Stephen R Cole, Christian M Shay, Carolyn A Chew-Graham, Penny Gordon-Larsen, Evangelos Kontopantelis, Elizabeth J Mayer-Davis, 2023.

import sys, csv, re

codes = [{"code":"10001","system":"gprdproduct"},{"code":"10067","system":"gprdproduct"},{"code":"10175","system":"gprdproduct"},{"code":"10207","system":"gprdproduct"},{"code":"10208","system":"gprdproduct"},{"code":"10225","system":"gprdproduct"},{"code":"10229","system":"gprdproduct"},{"code":"10243","system":"gprdproduct"},{"code":"10244","system":"gprdproduct"},{"code":"10245","system":"gprdproduct"},{"code":"10259","system":"gprdproduct"},{"code":"10264","system":"gprdproduct"},{"code":"10277","system":"gprdproduct"},{"code":"10547","system":"gprdproduct"},{"code":"10572","system":"gprdproduct"},{"code":"11055","system":"gprdproduct"},{"code":"11056","system":"gprdproduct"},{"code":"11107","system":"gprdproduct"},{"code":"11337","system":"gprdproduct"},{"code":"12035","system":"gprdproduct"},{"code":"12297","system":"gprdproduct"},{"code":"12299","system":"gprdproduct"},{"code":"12638","system":"gprdproduct"},{"code":"12654","system":"gprdproduct"},{"code":"12818","system":"gprdproduct"},{"code":"13277","system":"gprdproduct"},{"code":"13416","system":"gprdproduct"},{"code":"13516","system":"gprdproduct"},{"code":"13622","system":"gprdproduct"},{"code":"13729","system":"gprdproduct"},{"code":"13819","system":"gprdproduct"},{"code":"13837","system":"gprdproduct"},{"code":"14270","system":"gprdproduct"},{"code":"14290","system":"gprdproduct"},{"code":"14299","system":"gprdproduct"},{"code":"14301","system":"gprdproduct"},{"code":"14313","system":"gprdproduct"},{"code":"14330","system":"gprdproduct"},{"code":"14339","system":"gprdproduct"},{"code":"14340","system":"gprdproduct"},{"code":"14345","system":"gprdproduct"},{"code":"14357","system":"gprdproduct"},{"code":"14362","system":"gprdproduct"},{"code":"14505","system":"gprdproduct"},{"code":"14619","system":"gprdproduct"},{"code":"14644","system":"gprdproduct"},{"code":"14649","system":"gprdproduct"},{"code":"14918","system":"gprdproduct"},{"code":"14925","system":"gprdproduct"},{"code":"14928","system":"gprdproduct"},{"code":"14930","system":"gprdproduct"},{"code":"14933","system":"gprdproduct"},{"code":"14938","system":"gprdproduct"},{"code":"14944","system":"gprdproduct"},{"code":"15484","system":"gprdproduct"},{"code":"15710","system":"gprdproduct"},{"code":"1587","system":"gprdproduct"},{"code":"1594","system":"gprdproduct"},{"code":"1595","system":"gprdproduct"},{"code":"16129","system":"gprdproduct"},{"code":"16142","system":"gprdproduct"},{"code":"16152","system":"gprdproduct"},{"code":"16160","system":"gprdproduct"},{"code":"16682","system":"gprdproduct"},{"code":"16700","system":"gprdproduct"},{"code":"17336","system":"gprdproduct"},{"code":"17712","system":"gprdproduct"},{"code":"1805","system":"gprdproduct"},{"code":"18224","system":"gprdproduct"},{"code":"1840","system":"gprdproduct"},{"code":"1842","system":"gprdproduct"},{"code":"1843","system":"gprdproduct"},{"code":"1844","system":"gprdproduct"},{"code":"18461","system":"gprdproduct"},{"code":"18590","system":"gprdproduct"},{"code":"18592","system":"gprdproduct"},{"code":"18593","system":"gprdproduct"},{"code":"18931","system":"gprdproduct"},{"code":"19491","system":"gprdproduct"},{"code":"19513","system":"gprdproduct"},{"code":"19877","system":"gprdproduct"},{"code":"19878","system":"gprdproduct"},{"code":"20995","system":"gprdproduct"},{"code":"21110","system":"gprdproduct"},{"code":"21232","system":"gprdproduct"},{"code":"21235","system":"gprdproduct"},{"code":"21374","system":"gprdproduct"},{"code":"21395","system":"gprdproduct"},{"code":"21422","system":"gprdproduct"},{"code":"21583","system":"gprdproduct"},{"code":"21590","system":"gprdproduct"},{"code":"2221","system":"gprdproduct"},{"code":"22697","system":"gprdproduct"},{"code":"22983","system":"gprdproduct"},{"code":"23099","system":"gprdproduct"},{"code":"23231","system":"gprdproduct"},{"code":"23992","system":"gprdproduct"},{"code":"23993","system":"gprdproduct"},{"code":"24002","system":"gprdproduct"},{"code":"2455","system":"gprdproduct"},{"code":"2456","system":"gprdproduct"},{"code":"2459","system":"gprdproduct"},{"code":"24593","system":"gprdproduct"},{"code":"24795","system":"gprdproduct"},{"code":"24800","system":"gprdproduct"},{"code":"24846","system":"gprdproduct"},{"code":"24993","system":"gprdproduct"},{"code":"25133","system":"gprdproduct"},{"code":"25479","system":"gprdproduct"},{"code":"25735","system":"gprdproduct"},{"code":"25736","system":"gprdproduct"},{"code":"25812","system":"gprdproduct"},{"code":"26060","system":"gprdproduct"},{"code":"26098","system":"gprdproduct"},{"code":"26498","system":"gprdproduct"},{"code":"27177","system":"gprdproduct"},{"code":"27280","system":"gprdproduct"},{"code":"27396","system":"gprdproduct"},{"code":"27402","system":"gprdproduct"},{"code":"27461","system":"gprdproduct"},{"code":"28096","system":"gprdproduct"},{"code":"28101","system":"gprdproduct"},{"code":"2812","system":"gprdproduct"},{"code":"28183","system":"gprdproduct"},{"code":"28185","system":"gprdproduct"},{"code":"28442","system":"gprdproduct"},{"code":"28588","system":"gprdproduct"},{"code":"29567","system":"gprdproduct"},{"code":"29837","system":"gprdproduct"},{"code":"29953","system":"gprdproduct"},{"code":"30209","system":"gprdproduct"},{"code":"30686","system":"gprdproduct"},{"code":"30819","system":"gprdproduct"},{"code":"31205","system":"gprdproduct"},{"code":"31258","system":"gprdproduct"},{"code":"322","system":"gprdproduct"},{"code":"33167","system":"gprdproduct"},{"code":"33232","system":"gprdproduct"},{"code":"33966","system":"gprdproduct"},{"code":"34031","system":"gprdproduct"},{"code":"34097","system":"gprdproduct"},{"code":"35253","system":"gprdproduct"},{"code":"35260","system":"gprdproduct"},{"code":"35468","system":"gprdproduct"},{"code":"35701","system":"gprdproduct"},{"code":"36031","system":"gprdproduct"},{"code":"36066","system":"gprdproduct"},{"code":"36146","system":"gprdproduct"},{"code":"36194","system":"gprdproduct"},{"code":"36430","system":"gprdproduct"},{"code":"36513","system":"gprdproduct"},{"code":"36853","system":"gprdproduct"},{"code":"36920","system":"gprdproduct"},{"code":"38986","system":"gprdproduct"},{"code":"39006","system":"gprdproduct"},{"code":"39086","system":"gprdproduct"},{"code":"4093","system":"gprdproduct"},{"code":"41120","system":"gprdproduct"},{"code":"4129","system":"gprdproduct"},{"code":"4163","system":"gprdproduct"},{"code":"41959","system":"gprdproduct"},{"code":"4198","system":"gprdproduct"},{"code":"4199","system":"gprdproduct"},{"code":"42395","system":"gprdproduct"},{"code":"4247","system":"gprdproduct"},{"code":"42954","system":"gprdproduct"},{"code":"43950","system":"gprdproduct"},{"code":"43953","system":"gprdproduct"},{"code":"43991","system":"gprdproduct"},{"code":"44251","system":"gprdproduct"},{"code":"44378","system":"gprdproduct"},{"code":"44480","system":"gprdproduct"},{"code":"45158","system":"gprdproduct"},{"code":"46001","system":"gprdproduct"},{"code":"46666","system":"gprdproduct"},{"code":"4706","system":"gprdproduct"},{"code":"4715","system":"gprdproduct"},{"code":"47360","system":"gprdproduct"},{"code":"4760","system":"gprdproduct"},{"code":"4784","system":"gprdproduct"},{"code":"47856","system":"gprdproduct"},{"code":"49108","system":"gprdproduct"},{"code":"49831","system":"gprdproduct"},{"code":"5021","system":"gprdproduct"},{"code":"50633","system":"gprdproduct"},{"code":"50691","system":"gprdproduct"},{"code":"51743","system":"gprdproduct"},{"code":"5214","system":"gprdproduct"},{"code":"5250","system":"gprdproduct"},{"code":"52522","system":"gprdproduct"},{"code":"52722","system":"gprdproduct"},{"code":"52748","system":"gprdproduct"},{"code":"53118","system":"gprdproduct"},{"code":"53251","system":"gprdproduct"},{"code":"53710","system":"gprdproduct"},{"code":"54462","system":"gprdproduct"},{"code":"55234","system":"gprdproduct"},{"code":"55462","system":"gprdproduct"},{"code":"55517","system":"gprdproduct"},{"code":"55603","system":"gprdproduct"},{"code":"55618","system":"gprdproduct"},{"code":"55687","system":"gprdproduct"},{"code":"55907","system":"gprdproduct"},{"code":"55910","system":"gprdproduct"},{"code":"56115","system":"gprdproduct"},{"code":"56489","system":"gprdproduct"},{"code":"56495","system":"gprdproduct"},{"code":"56502","system":"gprdproduct"},{"code":"56691","system":"gprdproduct"},{"code":"56857","system":"gprdproduct"},{"code":"57529","system":"gprdproduct"},{"code":"57564","system":"gprdproduct"},{"code":"57620","system":"gprdproduct"},{"code":"57622","system":"gprdproduct"},{"code":"5845","system":"gprdproduct"},{"code":"5891","system":"gprdproduct"},{"code":"5892","system":"gprdproduct"},{"code":"5933","system":"gprdproduct"},{"code":"59500","system":"gprdproduct"},{"code":"59533","system":"gprdproduct"},{"code":"6061","system":"gprdproduct"},{"code":"60933","system":"gprdproduct"},{"code":"60938","system":"gprdproduct"},{"code":"60951","system":"gprdproduct"},{"code":"61845","system":"gprdproduct"},{"code":"6209","system":"gprdproduct"},{"code":"62180","system":"gprdproduct"},{"code":"62276","system":"gprdproduct"},{"code":"6958","system":"gprdproduct"},{"code":"6965","system":"gprdproduct"},{"code":"7228","system":"gprdproduct"},{"code":"7231","system":"gprdproduct"},{"code":"7237","system":"gprdproduct"},{"code":"7266","system":"gprdproduct"},{"code":"7267","system":"gprdproduct"},{"code":"7300","system":"gprdproduct"},{"code":"7318","system":"gprdproduct"},{"code":"7319","system":"gprdproduct"},{"code":"7349","system":"gprdproduct"},{"code":"7350","system":"gprdproduct"},{"code":"7393","system":"gprdproduct"},{"code":"7400","system":"gprdproduct"},{"code":"7402","system":"gprdproduct"},{"code":"7537","system":"gprdproduct"},{"code":"7793","system":"gprdproduct"},{"code":"8322","system":"gprdproduct"},{"code":"8841","system":"gprdproduct"},{"code":"8895","system":"gprdproduct"},{"code":"9341","system":"gprdproduct"},{"code":"9376","system":"gprdproduct"},{"code":"9503","system":"gprdproduct"},{"code":"9521","system":"gprdproduct"},{"code":"9565","system":"gprdproduct"},{"code":"9618","system":"gprdproduct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('insulin-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["insulin-200unit---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["insulin-200unit---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["insulin-200unit---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
