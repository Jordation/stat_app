from sqlalchemy import Column, create_engine, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import declarative_base, relationship

engine = create_engine(r"sqlite:///static/myScripts/the_database/test_db.db", echo=True, future=True)
base = declarative_base()

class TBL_Events(base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True)
    event = Column(String(128))


    matches_played = relationship("TBL_Match", back_populates="event")

    def __repr__(self) -> str:
        return f"event: {self.event}"


class TBL_Match(base):
    __tablename__ = "matches_played"
    id = Column(Integer, primary_key=True)
    matchname = Column(String(64))
    winner = Column(String(64))
    bestof = Column(Integer)

    event_id = Column(Integer, ForeignKey("events.id"))
    event = relationship("TBL_Events", back_populates="matches_played")

    maps_played = relationship("TBL_Map", back_populates="match")

    def __repr__(self):
        return f"match: {self.matchname}, event: {self.event}"


class TBL_Map(base):
    __tablename__ = "maps_played"
    id = Column(Integer, primary_key=True)
    mapname = Column(String(16), nullable=False)
    team1 = Column(String(32))
    team2 = Column(String(32))
    winner = Column(String(32))

    match_id = Column(Integer, ForeignKey("matches_played.id"))
    match = relationship("TBL_Match",
                         back_populates="maps_played")

    player_stats_combined = relationship("TBL_Stats",
                                         back_populates="map_id_link",
                                         foreign_keys='TBL_Stats.map_id')
    player_stats_defence = relationship("TBL_Stats_DEF",
                                        back_populates="map_id_link",
                                        foreign_keys='TBL_Stats_DEF.map_id')
    player_stats_attack = relationship("TBL_Stats_ATK",
                                       back_populates="map_id_link",
                                       foreign_keys='TBL_Stats_ATK.map_id')
    comb_map = relationship("TBL_Stats",
                            back_populates="map_name_link",
                            foreign_keys='TBL_Stats.mapname')
    def_map = relationship("TBL_Stats_DEF",
                           back_populates="map_name_link",
                           foreign_keys='TBL_Stats_DEF.mapname')
    atk_map = relationship("TBL_Stats_ATK",
                           back_populates="map_name_link",
                           foreign_keys='TBL_Stats_ATK.mapname')

    def __repr__(self):
        return f"{self.team1=}, {self.team2=}, {self.match=}, {self.mapname=}, {self.id=}, {self.match_id=}"


class TBL_Stats(base):
    __tablename__ = "player_stats_combined"
    id = Column(Integer, primary_key=True)
    player = Column(String(32))
    agent = Column(String(32))
    team = Column(String(32))
    acs = Column(Integer)
    k = Column(Integer)
    d = Column(Integer)
    a = Column(Integer)
    kast = Column(Integer)
    adr = Column(Integer)
    hsp = Column(Integer)
    fb = Column(Integer)
    fd = Column(Integer)

    map_id = Column(Integer, ForeignKey("maps_played.id"))
    map_id_link = relationship("TBL_Map",
                               back_populates="player_stats_combined",
                               foreign_keys='TBL_Stats.map_id')
    mapname = Column(String(16), ForeignKey("maps_played.mapname"))
    map_name_link = relationship("TBL_Map",
                                 back_populates="comb_map",
                                 foreign_keys='TBL_Stats.mapname')

    def __repr__(self):
        return f"{self.player=}, {self.agent=}, {self.team=}"


class TBL_Stats_DEF(base):
    __tablename__ = "player_stats_defence"
    id = Column(Integer, primary_key=True)
    player = Column(String(32))
    agent = Column(String(32))
    team = Column(String(32))
    acs = Column(Integer)
    k = Column(Integer)
    d = Column(Integer)
    a = Column(Integer)
    kast = Column(Integer)
    adr = Column(Integer)
    hsp = Column(Integer)
    fb = Column(Integer)
    fd = Column(Integer)

    map_id = Column(Integer, ForeignKey("maps_played.id"))
    map_id_link = relationship("TBL_Map",
                               back_populates="player_stats_defence",
                               foreign_keys='TBL_Stats_DEF.map_id')
    mapname = Column(String(16), ForeignKey("maps_played.mapname"))
    map_name_link = relationship("TBL_Map",
                                 back_populates="def_map",
                                 foreign_keys='TBL_Stats_DEF.mapname')

    def __repr__(self):
        return f"{self.player=}, {self.agent=}, {self.team=}"

class TBL_Stats_ATK(base):
    __tablename__ = "player_stats_attack"
    id = Column(Integer, primary_key=True)
    player = Column(String(32))
    agent = Column(String(32))
    team = Column(String(32))
    acs = Column(Integer)
    k = Column(Integer)
    d = Column(Integer)
    a = Column(Integer)
    kast = Column(Integer)
    adr = Column(Integer)
    hsp = Column(Integer)
    fb = Column(Integer)
    fd = Column(Integer)

    map_id = Column(Integer, ForeignKey("maps_played.id"))
    map_id_link = relationship("TBL_Map",
                               back_populates="player_stats_attack",
                               foreign_keys='TBL_Stats_ATK.map_id')
    mapname = Column(String(16), ForeignKey("maps_played.mapname"))
    map_name_link = relationship("TBL_Map",
                                 back_populates="atk_map",
                                 foreign_keys='TBL_Stats_ATK.mapname')

    def __repr__(self):
        return f"{self.player=}, {self.agent=}, {self.team=}"


base.metadata.create_all(engine)

