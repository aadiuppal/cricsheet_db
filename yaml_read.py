import yaml
import os
from collections import defaultdict
def get_id(myfile):
    fil = myfile.strip().split("/")[-1]
    return fil.strip().split(".")[0]

def get_umpires(dat):
    ump = [None,None,None]
    for i in range(len(dat)):
        ump[i] = dat[i]
        if i == 2:
            break
    return ump

def get_win_details(dat):
    res = ""
    for k in dat:
        if str(type(dat[k])) == "<type 'dict'>":
            res += str(k)+" "+get_win_details(dat[k])
        elif k != 'winner':
            res += str(k)
            res += " "+str(dat[k])+" "
    return res

class YamlReader:
    def getMatchDetails(self,myfile):
        stream = file(myfile,'r')
        data = yaml.load(stream)
        matchid = get_id(myfile)
        #print data['info'].keys()
        data = defaultdict(str,data)
        if 'city' in data['info']:
            venue_city = data['info']['city']
        else:
            venue_city = ""
        date = data['info']['dates'][0]
        match_type = data['info']['match_type']
        gender = data['info']['gender']
        venue_stadium = data['info']['venue']
        team1,team2 =  data['info']['teams']
        umpire1,umpire2,umpire3 = get_umpires(data['info']['umpires'])
        toss_winner = data['info']['toss']['winner']
        toss_decision = data['info']['toss']['decision']
        if 'winner' in data['info']['outcome']:
            winner = data['info']['outcome']['winner']
        else:
            winner = data['info']['outcome']['result']
        win_by = get_win_details(data['info']['outcome'])
        if 'overs' in data['info']:
            max_overs = data['info']['overs']
        else:
            max_overs = None
        if 'player_of_match' in data['info']:
            player_of_match =  data['info']['player_of_match'][0]
        else:
           player_of_match = None

        return [matchid,team1,team2,win_by,winner,player_of_match,max_overs,venue_city,
                venue_stadium,date,gender,match_type,toss_winner,toss_decision,umpire1,umpire2,umpire3]

    def getBallDetails(self,myfile):
        stream = file(myfile,'r')
        balls_data = []
        matchid = get_id(myfile)
        data = yaml.load(stream)
        #print data.keys()
        for i in range(len(data['innings'])):
            innings = data['innings'][i].keys()[0]
            batting_team = data['innings'][i][innings]['team']
            for j in range(len(data['innings'][i][innings]['deliveries'])):
                ball_num = j+1
                over,batsman,bowler,non_striker,runs_batsman,runs_extras,runs_total,wicket_player,wicket_kind,wicket_fielder = self.get_ball_data(data['innings'][i][innings]['deliveries'][j])
                balls_data.append([matchid,innings,batting_team,ball_num,over,batsman,
                    bowler,non_striker,runs_batsman,runs_extras,runs_total,wicket_player,wicket_kind,wicket_fielder])
        #print data['innings'][0]['1st innings']['deliveries'][0]
        #print data['innings'][0]['1st innings']['team']
        return balls_data

    def get_ball_data(self,dat):
        over = dat.keys()[0]
        batsman = dat[over]['batsman']
        bowler = dat[over]['bowler']
        non_striker = dat[over]['non_striker']
        runs_batsman = dat[over]['runs']['batsman']
        runs_extras = dat[over]['runs']['extras']
        runs_total = dat[over]['runs']['total']
        if 'wicket' in dat[over]:
            wicket_player = dat[over]['wicket']['player_out']
            wicket_kind = dat[over]['wicket']['kind']
            if 'fielders' in dat[over]['wicket']:
                wicket_fielder = dat[over]['wicket']['fielders'][0]
            else:
                wicket_fielder = None
        else:
            wicket_fielder,wicket_kind,wicket_player = None,None,None
        return [over,batsman,bowler,non_striker,runs_batsman,runs_extras,runs_total,wicket_player,wicket_kind,wicket_fielder]

y = YamlReader()
#y.getMatchDetails("data/1003273.yaml")
#y.getBallDetails("data/1003273.yaml")
