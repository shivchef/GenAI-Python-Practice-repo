player = {"Shivam","Rahul" ,"Sumit", "Suraj" , "Dinesh"}
spectator = {"Suraj", "Nilu","Mummy"}

only_player = player-spectator
print(f"Only players in the sets are {only_player}")
Both_ = player & spectator
print(f"Both in the sets are {Both_}")
total = player | spectator
print(f"Union of them are {total}")