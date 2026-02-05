users = [
    {"hello":12 , "total":123 , "target"="Ram" },
    {"hello":13 , "total":113 , "target"="Sam" },
    {"hello":15 , "total":133 , "target"="Kam" },
    {"hello":16 , "total":1633 , "target"="Pam" }
]

deathType ={
    "Ram":(1,0),
    "Sam":(3,0),
    "Kam":(0,10),
    "Pam":(0,12),
}

for targets in users :
    bullets, stabs = deathType.get(users[targets],(0,0))
    deathTypeFixed = users["total"]
