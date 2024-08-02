import pandas as pd
data = {'TimeStamp': ['2024-02-02 08:30:00', '2024-02-02 14:45:00', '2024-02-02 19:15:00']}
df = pd.DataFrame(data)
df['TimeStamp'] = pd.to_datetime(df['TimeStamp'])
df['Hour'] = df['TimeStamp'].dt.hour
print(df)
