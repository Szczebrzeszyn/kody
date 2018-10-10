Drop table  if exists miasta;
drop table if exists dane_demograficzne;
drop table if exists dane_powierzchniowe;
Create TABLE miasta (
    id_miasta INTEGER PRIMARY KEY AUTOINCREMENT,
    nazwa_miasta TEXT(30),
    wojewodztwo TEXT(30)

);

Create table dane_demograficzne (
    id integer primary key autoincrement,
    liczba_mieszkancow integer,
    liczba_kobiet integer,
    grupa_wiekowa text(15),
    data_aktualizacji date,
    id_miasta integer,
    Foreign key (id_miasta) References miasta(id_miasta)
);

Create table dane_powierzchniowe (
    id integer primary key autoincrement,
    powierzchnia_miasta decimal,
    powierchnia_zielone decimal,
    data_akutalizacji date,
    id_miasta integer,
    foreign key (id_miasta) references miasta(id_miasta)
);
