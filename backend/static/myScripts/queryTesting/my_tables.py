from select import select
from sqlalchemy import Column, create_engine, ForeignKey, Integer, String, ForeignKey, select
from sqlalchemy.orm import declarative_base, relationship, Session

#
# START SETUP
#
ENGINE = create_engine(r"sqlite:///static\myScripts\queryTesting\made_up_data.db", echo=True, future=True)
BASE = declarative_base()


class TBL_Tourney(BASE):
    __tablename__ = "tournaments"
    id = Column(Integer, primary_key=True)
    tournament = Column(String(64))
    
    matches_played = relationship("TBL_Match", back_populates="tournament")

    def __repr__(self) -> str:
        return f"Tournament: {self.tournament}"


class TBL_Match(BASE):
    __tablename__ = "matches_played"
    id = Column(Integer, primary_key=True) 
    tournament_id = Column(Integer, ForeignKey("tournaments.id"))
    matchname = Column(String(64))

    tournament = relationship("TBL_Tourney", back_populates="matches_played")
    maps_played = relationship("TBL_Map", back_populates="match")

    def __repr__(self):
        return f"match: {self.matchname}, tournament: {self.tournament}"


class TBL_Map(BASE):
    __tablename__ = "maps_played"
    id = Column(Integer, primary_key=True)
    match_id = Column(Integer, ForeignKey("matches_played.id"))
    mapname = Column(String(20))
    
    match = relationship("TBL_Match", back_populates="maps_played")
    player_stats = relationship("TBL_Stat", back_populates="map_")

    def __repr__(self):
        return f"match: {self.match}, mapname = {self.mapname}, map id, match id = {self.id},{self.match_id}"


class TBL_Stat(BASE):
    __tablename__ = "player_stats"
    id = Column(Integer, primary_key=True)
    map_id = Column(Integer, ForeignKey("maps_played.id"))
    name = Column(String(20))
    k = Column(Integer)
    d = Column(Integer)
    a = Column(Integer)
    
    map_ = relationship("TBL_Map", back_populates="player_stats")

    def __repr__(self):
        return f"{self.name} stats for map {self.map_.mapname}: k {self.k}, d {self.d}, a {self.a}"


BASE.metadata.create_all(ENGINE)
