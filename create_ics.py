from ics import Calendar, Event
import json
from datetime import datetime


def main():
    with open("calendar.json", "r") as f:
        data = json.load(f)
    
    calendar = Calendar()
    data = data.get("data")
    for item in data:
        event = Event()
        tip = item.get("tip")
        predmet = item.get("predmet").split(" (")[0]
        if tip.lower() == "predavanje":
            event.name = f"{predmet} - Predavanje"
        elif tip.lower() == "vježbe":
            event.name = f"{predmet} - Vježbe"
        else:
            raise ValueError(f"Unknown tip: {tip}")
        date = item.get("datum")
        start_time = item.get("terminPocetak") + ":00"
        end_time = item.get("terminKraj") + ":00"
        date = datetime.strptime(date, "%d.%m.%Y.").strftime("%Y-%m-%d")
        event.begin = f"{date} {start_time}"
        event.end = f"{date} {end_time}"
        event.location = item.get("dvorana")
        event.organizer = item.get("nastavnik")
        event.duration = {"minutes": item.get("terminTrajanje")}
        calendar.events.add(event)
        # print(event)

    with open("calendar.ics", "w") as f:
        f.write(str(calendar))
    
    


if __name__ == "__main__":
    main()