import requests
import datetime
import sys


def book_clc_room(weekday):
    def get_next_weekday(current_date, target_weekday):
        days_ahead = (target_weekday - current_date.weekday() + 7) % 7
        if days_ahead == 0:
            days_ahead = 7 
        return current_date + datetime.timedelta(days=days_ahead)

    def create_payload(date):
        return f'csrf_token=8d18a87176a2516a7d306d6e97bc1f2741ab31e55353fe056eadcdfc821fdd8f&returl=https%3A%2F%2Fbooking.sauder.ubc.ca%2Fclc%2Findex.php%3Fview%3Dday%26page_date%3D{date}%26area%3D6%26room%3D30&rep_id=0&edit_type=series&create_by=dennis34&name=STUDY&description=STUDY&start_date={date}&start_seconds=45000&end_date={date}&end_seconds=52200&area=6&rooms%5B%5D=30'

    today = datetime.date.today()
    target = get_next_weekday(today, weekday)

    url = "https://booking.sauder.ubc.ca/clc/edit_entry_handler.php"

    payload = create_payload(target)

    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'MRBS_SESSID=nqns1fuhotoufmen7ungllpgb3; _shibsession_636c6368747470733a2f2f626f6f6b696e672e7361756465722e7562632e63612f636c632f73686962626f6c6574682d7370=_474cd76e575f97d7b82b1f5187755e09; MRBS_SESSID=i1dbqhfbctl4uhrun8b9kuuke5',
    'DNT': '1',
    'Origin': 'https://booking.sauder.ubc.ca',
    'Referer': 'https://booking.sauder.ubc.ca/clc/edit_entry.php?drag=1&area=6&start_seconds=45000&end_seconds=52200&rooms[]=30&start_date=2025-01-09',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response)

if __name__ == "__main__":

    if len(sys.argv) >= 2:
        target_weekday = int(sys.argv[1])
        book_clc_room(target_weekday)
    else:
        book_clc_room(1)
        book_clc_room(3)