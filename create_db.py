from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sql_declare import Match,Base,Details

import glob
from yaml_read import YamlReader

engine = create_engine('sqlite:////home/aaditya/Desktop/code/my_git/cricsheet_db/cricsheet_data.db')
Base.metadata.create_all(engine)
Base.metadata.bind  = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

yaml_reader = YamlReader()
count = 1



def update_match_data(match_data):
    print match_data[0]
    tmp = session.query(Match).filter(Match.matchid == match_data[0]).all()
    if tmp and tmp[0].matchid == int(match_data[0]):
        return tmp
    match = Match(matchid = match_data[0],
                  team1 = match_data[1],
                  team2 = match_data[2],
                  win_by = match_data[3],
                  winner = match_data[4],
                  player_of_match = match_data[5],
                  max_overs = match_data[6],
                  venue_city = match_data[7],
                  venue_stadium = match_data[8],
                  date = match_data[9],
                  gender = match_data[10],
                  match_type = match_data[11],
                  toss_winner = match_data[12],
                  toss_decision = match_data[13],
                  umpire1 = match_data[14],
                  umpire2 = match_data[15],
                  umpire3 = match_data[16])
    session.add(match)
    session.commit()
    return match

def update_ball_details(count,ball_data,match):
    tmp = session.query(Details).filter(Details.id == count).all()
    if tmp and tmp[0].id == count:
        return tmp
    ball = Details(id = count,
                   matchid = ball_data[0],
                   match = match,
                   innings = ball_data[1],
                   batting_team = ball_data[2],
                   ball_num = ball_data[3],
                   over = ball_data[4],
                   batsman = ball_data[5],
                   bowler = ball_data[6],
                   non_striker = ball_data[7],
                   runs_batsman = ball_data[8],
                   runs_extras = ball_data[9],
                   runs_total = ball_data[10],
                   wicket_player = ball_data[11],
                   wicket_kind = ball_data[12],
                   wicket_fielder = ball_data[13])
    session.add(ball)
    session.commit()
    return ball

data_files = glob.glob('data/*.yaml')

for myfile in data_files:
    match_data = yaml_reader.getMatchDetails(myfile)
    match = update_match_data(match_data)
    ball_details = yaml_reader.getBallDetails(myfile)
    for ball in ball_details:
        update_ball_details(count,ball,match)
        count += 1


