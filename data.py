#!/usr/bin/env python3 
"""Fetches data from variou APIs and adds it to the MySQL storage"""
from api.v1 import db
from models.skills import *
from models.locations import *
from models.creatives import *
from models.projects import *
import uuid
import requests


#db
db.create_all()

#skills
sk1 = Skills(id=str(uuid.uuid4()), name="Photography")
sk2 = Skills(id=str(uuid.uuid4()), name="Illustration")
sk3 = Skills(id=str(uuid.uuid4()), name="Sketching")
sk4 = Skills(id=str(uuid.uuid4()), name="Graphic Design")
sk5 = Skills(id=str(uuid.uuid4()), name="Digital Art")
sk6 = Skills(id=str(uuid.uuid4()), name="Fashion Design")
sk7 = Skills(id=str(uuid.uuid4()), name="Video Editing")
sk8 = Skills(id=str(uuid.uuid4()), name="UI/UX Design")
sk9 = Skills(id=str(uuid.uuid4()), name="Sculpting")
sk10 = Skills(id=str(uuid.uuid4()), name="Make-up Arts")
sk11 = Skills(id=str(uuid.uuid4()), name="Game Design")
sk12 = Skills(id=str(uuid.uuid4()), name="Concept Art")
sk13 = Skills(id=str(uuid.uuid4()), name="Constume Design")
sk14 = Skills(id=str(uuid.uuid4()), name="Product Design")
sk15 = Skills(id=str(uuid.uuid4()), name="Painting")

db.session.add_all([sk1, sk2, sk3, sk4, sk5, sk6, sk7, sk8, sk9, sk10, sk11, sk12, sk13, sk14, sk15])
db.session.commit()



#creatives-photography
url = "https://api.unsplash.com/search/users"
params = {"query": "photographer", "per_page": 100}
headers = {"Authorization": "Client-ID 3DhRLr1G3QpT6DESnxy7bxb1gibJ_MTO97-KFqt75-w"}
r = requests.get(url, params=params, headers=headers).json()["results"][:10]

locs = []
for item in r:
    cr = Creative(id=str(uuid.uuid4()), username=item["username"], first_name=item["first_name"], last_name=item["last_name"], profile_img_url=item["profile_image"]["medium"], about=requests.get(item["links"]["self"], headers=headers).json()["bio"])
    location = requests.get(item["links"]["self"], headers=headers).json()["location"]
    count = 0
    for l in locs:
        if l.name == location:
            cr.location = l
            count += 1
            break
        else:
            continue
    if count == 0:
        loc = Location(id=str(uuid.uuid4()), name=location)
        db.session.add(loc)
        cr.location = loc
        locs.append(loc)
    db.session.add(cr)
    photos = requests.get(item["links"]["photos"], headers=headers).json()[:6]
    for item in photos:
        p = Portfolio(id=str(uuid.uuid4()), image_url=item["urls"]["full"], description=item["description"], creative=cr)
        db.session.add(p)
    cr.cover_photo_url = photos[0]["urls"]["small"]

    cr.c_skills.append(sk1)

db.session.commit()