import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

teamwise_home_away=pd.read_csv('C:/Users/VAMSHI/Downloads/teamwise_home_and_away.csv')
teamwise_home_away

Players=pd.read_excel('C:\\Users\\VAMSHI\\Downloads\\Players.xlsx')
Players

Matches=pd.read_csv('C:\\Users\\VAMSHI\\Downloads\\matches.csv')
Matches

ASR=pd.read_csv('C:\\Users\\VAMSHI\\Downloads\\most_runs_average_strikerate.csv')
ASR

Teams = pd.read_csv('C:\\Users\\VAMSHI\\Downloads\\teams.csv')
Teams

Deliveries=pd.read_csv('C:\\Users\\VAMSHI\\Desktop\\project\\deliveries.csv')
Deliveries

teamwise_home_away.isna().sum().sum()

Players.isna().sum()
len(Players)
Players['DOB'].fillna(Players['DOB'].mode()[0],inplace=True)
Players['Batting_Hand'].fillna(Players['Batting_Hand'].mode()[0],inplace=True)
Players['Bowling_Skill'].fillna(Players['Bowling_Skill'].mode()[0],inplace=True)
Players['Country'].fillna(Players['Country'].mode()[0],inplace=True)
Players.isna().sum().sum()

Matches.isna().sum()
len(Matches)
Matches.drop('umpire3',axis=1,inplace=True)
Matches['umpire2'].fillna(Matches['umpire2'].mode()[0],inplace=True)
Matches['umpire1'].fillna(Matches['umpire1'].mode()[0],inplace=True)
Matches['player_of_match'].fillna(Matches['player_of_match'].mode()[0],inplace=True)
Matches['winner'].fillna(Matches['winner'].mode()[0],inplace=True)
Matches['city'].fillna(Matches['city'].mode()[0],inplace=True)

ASR.isna().sum()
ASR['average'].fillna(ASR['average'].median(),inplace=True)

teamwise_home_away.replace(np.NaN,-99999,inplace=True)
Matches.replace(np.NaN,-99999,inplace=True)
Deliveries.replace(np.NaN,-99999,inplace=True)

Deliveries.isna().sum()
len(Deliveries)
Deliveries.dropna(axis=1,inplace=True)

X1=teamwise_home_away['team']
Y1=teamwise_home_away['home_win_percentage']
plt.bar(X1,Y1)
plt.xticks(rotation=90)

Y2=teamwise_home_away['away_win_percentage']
X2=teamwise_home_away['team']
plt.bar(X2,Y2)
plt.xticks(rotation=90)

Y_tot=Y1+Y2
X_tot=X1
plt.bar(X_tot,Y_tot)
plt.xticks(rotation=90)

hmtswn=len(Matches[Matches['team1']==Matches['toss_winner']])
print('won toss at home ground',str(round(hmtswn/len(Matches)*100,2))+'%')

awtswn=len(Matches[Matches['team2']==Matches['toss_winner']])
print('won toss at away ground',str( round(awtswn/len(Matches)*100,2))+'%')

win_df=Matches[Matches['win_by_runs']!=0]
team_won1=win_df['winner']
by_runs=win_df['win_by_runs']
plt.scatter(team_won1,by_runs)
plt.xticks(rotation=90)

wick_df=Matches[Matches['win_by_wickets']!=0]
team_won2=wick_df['winner']
wick=wick_df['win_by_wickets']
plt.scatter(team_won2,wick,color='r')
plt.xticks(rotation=90)

from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
Matches['team1'] = lb.fit_transform(Matches['team1'])
Matches['team2'] = lb.fit_transform(Matches['team2'])
Matches['winner'] = lb.fit_transform(Matches['winner'])
Matches['Season'] = lb.fit_transform(Matches['Season'])
win__df=Matches[Matches['win_by_runs']!=0]
win__df

wick__df=Matches[Matches['win_by_wickets']!=0]
wick__df


team = Teams['team1']
print('\nAverage win run trail\n')
for i in range(15):
    val=win__df[win__df['winner']==i]
    tot_run=sum(val['win_by_runs'])
    print(team[i],'-->',str(round(tot_run/len(val),2))+'%')

print('\nAverage win wicket trail\n')
for i in range(15):
    val1=wick_df[wick__df['winner']==i]
    tot_run1=sum(val1['win_by_wickets'])
    print(team[i],'-->',tot_run1//len(val1))
    

teamwise_home_away['team'] = lb.fit_transform(teamwise_home_away['team'])

wins=[]
team_1=[]
tot_wins=sum(teamwise_home_away['home_wins'],teamwise_home_away['away_wins'])
for i in range(14):
    val2=teamwise_home_away[teamwise_home_away['team']==i]
    if i!=6:
        wins.append(int(val2['home_wins']+val2['away_wins']))
        team_1.append(team[i])
plt.pie(wins,labels=team_1,startangle=100)

#Batsman vs Total runs

btmn=ASR['batsman'].head(50)
tot_runs1=ASR['total_runs'].head(50)
plt.bar(btmn,tot_runs1,label=np.array(50),color='rgbym')
plt.xticks(rotation=90,fontsize=7)

#strike rate vs batsman

strike_rate=ASR['strikerate'].head(50)
print(strike_rate.shape,btmn.shape)
plt.scatter(btmn,strike_rate)
plt.xticks(rotation=90,fontsize=7)


Deliveries.columns
Deliveries['batting_team'] = lb.fit_transform(Deliveries['batting_team'])
Deliveries['bowling_team'] = lb.fit_transform(Deliveries['bowling_team'])


# 4's by a team

arr1=[]
team_temp=[]
delv_temp=Deliveries[Deliveries['batsman_runs']>=4]
delv=delv_temp[delv_temp['batsman_runs']<=5]
for i in range(15):
    d=delv[delv['batting_team']==i]
    if len(d)!=0:
        team_temp.append(team[i])
        arr1.append(len(d))
plt.pie(arr1,labels=team_temp,startangle=125)

# 6's by a team

arr1=[]
team_temp=[]
delv_temp=Deliveries[Deliveries['batsman_runs']>=6]
delv=delv_temp[delv_temp['batsman_runs']<=7]
for i in range(15):
    d=delv[delv['batting_team']==i]
    if len(d)!=0:
        team_temp.append(team[i])
        arr1.append(len(d))
plt.pie(arr1,labels=team_temp,startangle=125)

# total number of boundaries

arr1=[]
team_temp=[]
delv_temp=Deliveries[Deliveries['batsman_runs']>=4]
delv=delv_temp[delv_temp['batsman_runs']<=7]
for i in range(15):
    d=delv[delv['batting_team']==i]
    if len(d)!=0:
        team_temp.append(team[i])
        arr1.append(len(d))
plt.pie(arr1,labels=team_temp,startangle=125)


# Dot Balls by a team

arr1=[]
team_temp=[]
delv=Deliveries[Deliveries['batsman_runs']==0]
# delv=delv_temp[delv_temp['batsman_runs']<=7]
for i in range(15):
    d=delv[delv['batting_team']==i]
    if len(d)!=0:
        team_temp.append(team[i])
        arr1.append(len(d))
plt.bar(team_temp,arr1)
plt.xticks(rotation=90)
plt.pie(arr1,labels=team_temp,startangle=100)

# Total number of extras
extras=Deliveries['wide_runs']+Deliveries['bye_runs']+Deliveries['legbye_runs']+Deliveries['noball_runs']+Deliveries['penalty_runs']
print(extras.sum())

Matches.columns
max(Matches['Season'])

ses=max(Matches['Season'])
for i in range(int(ses)):
    print(i)
    sess=Matches[Matches['Season']==i]
    for j in range(15):
        prt_tm=len(sess[sess['winner']==j])
        tot_mt=len(sess[sess['team1']==j])
        tot_mt+=len(sess[sess['team2']==j])
        if tot_mt !=0:
            print(team[j],'won :',prt_tm)
            print('effective win: ',prt_tm/tot_mt)
    print('\n')


    