1) Create output dataframe with headings "easy, marathon, threshold, interval, rep"
    - rep = about 1-mile pace
2) Read in VDOT table
3) Loop through a list of 10k finish times, in 10 sec increments
4) Feed times to `VDOT()` function
5) Feed VDOT() result to `training_paces()` function
    - This will return a `dict()` of the form:`"easy: [pace],
    "marathon": [pace]...` etc
6) Add each `dict` value to the output dataframe (as m/s)
7) Then, we want to divide each value in each row, by that row's `"threshold"` column, to find out each training pace's per cent of threshold value
    - This isn't a perfect replication of Daniels' training values, but it should be close enough
