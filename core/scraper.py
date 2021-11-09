from bs4 import BeautifulSoup
import requests

currency_codes = {
    "دلار": "usd",
    "یورو": "eur",
    "پوند انگلیس": "gbp",
    "درهم امارات ": "aed",
    "لیر ترکیه ": "try",
    "یوان چین ": "cny",
    "ین ژاپن ( 100 ین ) ": "jpy",
    "دلار کانادا ": "cad",
    "دلار استرالیا ": "aud",
    "دلار نیوزیلند ": "nzd",
    "فرانک سوئیس ": "chf",
    "افغانی ": "afn",
    "کرون سوئد ": "sek",
    "روبل روسیه ": "rub",
    "منات آذربایجان ": "azn",
    "درام ارمنستان ": "amd",
    "دینار کویت ": "kwd",
    "ریال عربستان ": "sar",
    "ریال قطر ": "qar",
    "ریال عمان ": "omr",
    "لاری گرجستان ": "gel",
    "دینار عراق ": "iqd",
    "دینار بحرین ": "bhd",
    "لیر سوریه ( 10 لیر )": "syp",
    "کرون دانمارک ": "dkk",
    "کرون نروژ ": "nok",
    "روپیه هند ": "inr",
    "روپیه پاکستان ": "pkr",
    "دلار سنگاپور ": "sgd",
    "دلار هنگ کنگ ": "hkd",
    "رینگیت مالزی ": "myr",
    "بات تایلند ": "thb",
}


def get_currencies(base_url="https://www.tgju.org/currency"):

    res = requests.get(base_url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "lxml")
        tables = soup.find_all("tbody")[:2]
        result = {}
        for table in tables:
            rows = table.find_all("tr")
            for row in rows:
                try:
                    title = row.th.text
                    title = currency_codes[title]
                    price = row.find("td", attrs={"class": "nf"})
                    price = int("".join(price.text.split(",")))
                    result[title] = price
                except Exception as e:

                    return False
        return result
    else:
        return False


def main():
    return print(get_currencies())


if __name__ == "__main__":
    main()
