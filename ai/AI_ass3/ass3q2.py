import pandas as pd
i={
    'Subjects':["Maths","Maths","Physics","Chemistry","Physics","Chemistry","Physics","Maths"],
    'Book_Authors':["Tewani","R.S.Agarwal","D.C.Pandey","O.P.Tandon","H.C.Verma","Narendra Awasti","R.D.Sharma","Euclid"],
    'Count':[2,3,4,6,1,5,3,2]
}
IIIT_Library=pd.DataFrame(i)
t=IIIT_Library.groupby('Subjects')['Count'].sum()
print(IIIT_Library,"\n")
print(t)
