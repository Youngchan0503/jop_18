import requests
from bs4 import BeautifulSoup

def search_incruit(keyword, pages=1):

    jobs = []
    for page in range(pages):
        page1 = page * 30

        url1 = f"https://search.incruit.com/list/search.asp?col=job&kw={keyword}&startno={page1}"
        response = requests.get(url1)
        soup = BeautifulSoup(response.text, 'html.parser')
        lis = soup.find_all("li", class_="c_col")
        for li in lis:
            company = li.find("a", class_="cpname").text
            title = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").text
            location = li.find("div", class_="cl_md").find_all("span")[0].text
            link = li.find("div", class_="cell_mid").find("div", class_="cl_top").find("a").get("href")

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": link,
                "site" : "인크루트"
            }
            jobs.append(job_data)

        url2 = f"https://m.work24.go.kr/wk/a/b/1200/retriveDtlEmpSrchList.do?basicSetupYn=&careerTo=&keywordJobCd=&occupation=&seqNo=&cloDateEndtParam=&payGbn=&templateInfo=&rot2WorkYn=&shsyWorkSecd=&resultCnt=30&keywordJobCont=&cert=&moreButtonYn=&minPay=&codeDepth2Info=11000&currentPageNo=1&eventNo=&mode=&isChkLocCall=&major=&resrDutyExcYn=&eodwYn=&sortField=DATE&staArea=&sortOrderBy=DESC&keyword={keyword}&termSearchGbn=&carrEssYns=&benefitSrchAndOr=O&disableEmpHopeGbn=&actServExcYn=&keywordStaAreaNm=&maxPay=&locRegionCd=&emailApplyYn=&codeDepth1Info=11000&keywordEtcYn=&regDateStdtParam=&publDutyExcYn=&keywordJobCdSeqNo=&viewType=&exJobsCd=&templateDepthNmInfo=&region=&employGbn=&empTpGbcd=1&computerPreferential=&infaYn=&cloDateStdtParam=&siteClcd=all&searchMode=Y&birthFromYY=&indArea=&careerTypes=&subEmpHopeYn=&tlmgYn=&academicGbn=&templateDepthNoInfo=&foriegn=&entryRoute=&mealOfferClcd=&basicSetupYnChk=&station=&holidayGbn=&srcKeyword=%EA%B0%84%ED%98%B8%EC%82%AC&academicGbnoEdu=noEdu&enterPriseGbn=&cloTermSearchGbn=&birthToYY=&keywordWantedTitle=&stationNm=&benefitGbn=&isUseIframe=&keywordFlag=&notSrcKeyword=&essCertChk=&depth2SelCode=&keywordBusiNm=&preferentialGbn=&rot3WorkYn=&regDateEndtParam=&pfMatterPreferential=&pageIndex={page+1}&termContractMmcnt=&careerFrom=&laborHrShortYn=#scrollLoc"
        response = requests.get(url2)
        soup = BeautifulSoup(response.text, 'html.parser')
        company_lis = soup.find_all("td", class_="al_left pd24")
        location_lis = soup.find_all("td", class_="link pd24")
        print(company_lis)
        for i in range(len(company_lis)):
            company = company_lis[i].find("a", class_="cp_name underline_hover").text.replace("\r", "").replace("\n", "").replace("\t", "")
            title = company_lis[i].find_all("div", class_="cell")[1].find("a", class_="t3_sb underline_hover").text.replace("\r", "").replace("\n", "").replace("\t", "")
            link = company_lis[i].find_all("div", class_="cell")[1].find("a").get("href")
            location = location_lis[i].find("li", class_="site").find("p").text.replace("\r", "").replace("\n", "").replace("\t", "")

            job_data = {
                "company": company,
                "title": title,
                "location": location,
                "link": "https://www.work24.go.kr" + link,
                "site" : "고용24"
            }
            
            jobs.append(job_data)   
    
    return jobs