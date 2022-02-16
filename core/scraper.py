from bs4 import BeautifulSoup
import time

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
                    if title in currency_codes:
                        title = currency_codes[title]
                        price = row.find("td", attrs={"class": "nf"})
                        price = int("".join(price.text.split(",")))
                        result[title] = price

                except Exception as e:
                    print(e)
                    return False
        return result
    else:
        return False


def get_pair_rate_manualy(base, target):
    if base.lower() == "irr" or target.lower() == "irr":
        exchanges = get_currencies()
        if base.lower() == "irr":
            return "{:.6f}".format(round(1 / exchanges[target], 6))
        else:
            return "{:.6f}".format(round(exchanges[base], 6))
    else:
        res = requests.get(f"https://www.tgju.org/diff")
        soup = BeautifulSoup(res.content, "lxml")
        table = soup.find("table", attrs={"id": "diff-table"})
        trs = table.find_all("tr")[1:]
        exchanges = {}
        for tr in trs:
            title = tr.find("th").text.split()[0]
            rate = tr.find("td").text
            exchanges[title] = rate
        return "{:.6f}".format(float(exchanges[f"{base}/{target}"]))


def get_pair_rate_automaticaly(base, target):
    res = requests.get(f"https://www.tgju.org/diff")


def main():
    # return print(get_currencies())
    print(get_pair_rate_manualy("usd", "eur"))
    print(get_pair_rate_manualy("irr", "eur"))
    print(get_pair_rate_manualy("eur", "irr"))
    # print(get_pair_rate_manualy("sek", "usd"))
    # print(get_pair_rate_manualy("kwd", "usd"))


if __name__ == "__main__":
    main()
