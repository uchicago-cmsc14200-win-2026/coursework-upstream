The data source for this data is

    https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results/data?select=athlete_events.csv

The data from the repository named above has been rearranged and
slightly altered from its original form. More specifically, notes have
been removed from the NOC regions dataset, and the file names of flags
have been added to that dataset.

Each datafile in this directory can be understood by inspection of the
file itself, up to a point. Each file contains a header row on its
first line, which pandas uses for column headers. The fields (column
names) in these data files are described thoroughly at the site linked
above. Here, we will provide some basic descriptions of relevant
columns.

athlete_events.csv: contains data relating to the identity and
performance of athletes who have competed in the olympic games.

    ID: an ID value that uniquely identifies each athlete
    
    NOC: a code which identifies the team/country the athlete was
    representing
    
    Season: the season the game was for, Winter or Summer

    Year: the year the game took place in (note that at the beginning
    of the Olympics, the winter and summer Olympics took place in the
    same year)

    Medal: the medal the athlete won, NA, Bronze, Silver, or Gold

noc_regions.csv: contains a mapping between NOC codes, country names,
and the file name of images of these country's flags. Multiple NOC
codes may map to one country name.

    NOC: a code which identifies a team/country

    region: the country name in current year, to which multiple NOC
    may map

    image: the file name for the flag image located in
    ../../resources/images/flags

Please note that a substantial fraction of this data is not needed for
HW5; you only need to consult some of the data in each of these files
to perform HW5 tasks.

Please do not rename or change any of the files in this
directory. Doing so will likely result in test failures.
