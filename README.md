# convid-tn-collector
Collects CONVID-19 Data from tn.gov and saves it to csv

## This was quick and dirty - just to capture some stats.  
I know it is brittle and hardcoded but it works (right now).  
Why not switch to using a proper html processor? Because we are under lockdown and this is more fun. 
Fun like trying wo win a StarCraft ][ by only using marines.

### To Run ###

Requires Python 3.7


```shell
python get_convid_tn.py
```

outputs (in convid_tn.csv):

|Timestamp|County|Number of Cases|
| --- | --- | --- |
|20-Mar-2020 (16:45:02.164976)|DAVIDSON|101|
