import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Match(Base):
    __tablename__ = 'match'
    matchid = Column(Integer,primary_key=True)
    team1 = Column(String(250),nullable=False)
    team2 = Column(String(250),nullable=False)
    win_by = Column(String(250))
    winner = Column(String(250))
    player_of_match = Column(String(250))
    max_overs = Column(Integer)
    venue_city = Column(String(250))
    venue_stadium = Column(String(250))
    date = Column(String(250),nullable=False)
    gender = Column(String(250),nullable=False)
    match_type = Column(String(250),nullable=False)
    toss_winner = Column(String(250))
    toss_decision = Column(String(250))
    umpire1 = Column(String(250))
    umpire2 = Column(String(250))
    umpire3 = Column(String(250))

class Details(Base):
    __tablename__ = 'details'
    id = Column(Integer,primary_key = True)
    matchid = Column(Integer,ForeignKey('match.matchid'))
    match = relationship(Match)
    innings = Column(String(250),nullable=False)
    batting_team = Column(String(250),nullable=False)
    ball_num = Column(Integer)
    over = Column(String(250),nullable=False)
    batsman = Column(String(250),nullable=False)
    bowler = Column(String(250),nullable=False)
    non_striker = Column(String(250),nullable=False)
    runs_batsman = Column(Integer,nullable=False)
    runs_extras = Column(Integer,nullable=False)
    runs_total = Column(Integer,nullable=False)
    wicket_player = Column(String(250))
    wicket_kind = Column(String(250))
    wicket_fielder = Column(String(250))
