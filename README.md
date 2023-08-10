# Railway_Scheduling

## Bhavini Madhuranath

This project is done as a part of the build round of Swym technologies placement process

### Tech stack used

Python

- pandas to manipulate given csv
- streamlit to create a user interface
  MySQL

---

### How to run

`Note: This currently runs only on my local machine as i have set up the database on it`
on CMD, navigate to the directory of the repository and run
`streamlit run main.py`

---

### Problems tackled

1. Presence of `00:00:00` in departure and arrival:
   1. The problem statements did not require arrival and departure time as a part of the final database in terms of display. Hence, these columns were not used in the final database
   2. However, these proved to be a good indicator to understand how to frame halt times
   3. using midnight in arrival for Question 3 was required, and by comparing **current** and **destination** stations, the table was constructed
2. Finding timings of halts:
   1. In a real world scenario, the train would arrive well in advance at its departure platform and stay long enough at its arrival platform. In this case, finding `max`, `min` and `avg` time spent by these trains at a station would be heavily skewed data
   2. Hence, to tackle this data skew, I have limited the halt time at **source** and **destination** station to 10 minutes
   3. The halts of each train at each stop are stored in a table called `halts`
3. Finding number of trains to get from one given place to the other:
   1. For this, every stop of every train, along with its sequence is stored in a table
   2. The table is self joined to find the souce and destination pairs where they also match sequentially.

---

### Tables used

1. train - contains a mapping of train number and train name
2. station - contains a mapping of station code and station name
3. halts - contains the amount of time halted (in minutes) at a given station by a given train
4. stops - contains every stop by every train along with sequence
5. midnight - contains all trains that arrive at their destination at midnight
