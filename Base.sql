create table usuario (
    username VARCHAR(30), primary key(username),
    password varchar(30),
    email, varchar(30)
);

create table cuenta (
    id_user int, primary key(id_user),
    userName VARCHAR(30), foreign key(userName) references usuario(username) on delete cascade,
    user_type varchar(30),
    acc_state varchar(2)
);

create table cancion(
    id_cancion int, primary key(id_cancion),
    nombre varchar(30),
    artista varchar(30), 
    genero varchar(30),
    duracion varchar(30),
    album varchar(30),
    fecha_lanzamiento date,
    link varchar(80),
    active varchar(2) 
);

create table playlist(
    id_playist int, primary key(id_playist),
    pl_name varchar(30), 
    pl_owner int, foreign key(pl_owner) references cuenta(id_user)
);

create table pl_songs(
    songNumber int, primary key(songNumber),
    id_playist int, foreign key(id_playist) references playlist(id_playist),
    id_song int, foreign key(id_song) references cancion(id_cancion)
);

create table buscador(
    id_busqueda int, primary key(id_busqueda),
    usuario VARCHAR(30), foreign key(usuario) references usuario(username),
    id_cancion int, foreign key(id_song) references cancion(id_cancion),
    fecha_busqueda date
);

create table bitacora(
    id serial, primary key(id),
    fecha date,
    hora time,
    updated_by int,
    foreign key(updated_by) references cuenta(id_user),
    onTable varchar(40),
    accion varchar(40),
    change varchar(150)
) 

create or replace function updateCuenta()
returns trigger as 
$B0DY$
declare currentDate date;
declare currentTime time;
declare quien int;
declare maxDate date;
declare maxTime time;
begin
select current_date into currentDate;
select current_time into currentTime;
select max(lastupdatedd) from cuenta into maxDate;
select lastupdatedt from cuenta where lastupdatedd  = (select max(lastupdatedd) as maxdate from cuenta) limit 1 into maxTime;
select updated_by from cuenta where lastupdatedd = maxDate and lastupdatedt = maxTime into quien;
insert into bitacora 
values (default, currentDate, currentTime, quien, 'cuenta', TG_OP , concat(cast(old as varchar), 'to ', cast(new as varchar)));
return NEW;
end;
$B0DY$ language 'plpgsql';

create or replace function updateCancion()
returns trigger as 
$B0DY$
declare currentDate date;
declare currentTime time;
declare quien int;
declare maxDate date;
declare maxTime time;
begin
select current_date into currentDate;
select current_time into currentTime;
select max(lastupdatedd) from cancion into maxDate;
select lastupdatedt from cancion where lastupdatedd  = (select max(lastupdatedd) as maxdate from cancion) limit 1 into maxTime;
select updated_by from cancion where lastupdatedd = maxDate and lastupdatedt = maxTime into quien;
insert into bitacora 
values (default, currentDate, currentTime, quien, 'cancion', TG_OP , concat(cast(old as varchar), 'to ', cast(new as varchar)));
return NEW;
end;
$B0DY$ language 'plpgsql';

create or replace function updatePlaylist()
returns trigger as 
$B0DY$
declare currentDate date;
declare currentTime time;
declare maxDate date;
declare maxTime time;
declare quien int;
begin
select current_date into currentDate;
select current_time into currentTime;
select max(lastupdatedd) from playlist into maxDate;
select lastupdatedt from playlist where lastupdatedd  = (select max(lastupdatedd) as maxdate from playlist) limit 1 into maxTime;
select updated_by from playlist where lastupdatedd = maxDate and lastupdatedt = maxTime into quien;
insert into bitacora 
values (default, currentDate, currentTime, quien, 'playlist', TG_OP , concat(cast(old as varchar), 'to ', cast(new as varchar)));
return NEW;
end;
$B0DY$ language 'plpgsql';



CREATE TRIGGER triggerCuenta
AFTER insert or UPDATE or Delete
ON cuenta
FOR EACH ROW
EXECUTE PROCEDURE updateCuenta(); 

CREATE TRIGGER triggerCancion
AFTER insert or UPDATE or Delete
ON cancion
FOR EACH ROW
EXECUTE PROCEDURE updateCancion(); 

CREATE TRIGGER triggerPlaylist
AFTER insert or UPDATE or Delete
ON Playlist
FOR EACH ROW
EXECUTE PROCEDURE updatePlaylist(); 

create index BitacoraIndex
on bitacora (id, fecha, hora, updated_by, accion);

create index indexcuenta 
on Cuenta(id_usuario, user_type,update_by);

create index indenxplaylist 
on Playlist(id_playlist, dueño,update_by);

create index indexcancion 
on Cancion(id_cancion, album,genero,artista,fecha_lanzamiento,nombre,update_by);

select c.genero, count(c.genero) as conteo
from buscador b left join cancion c on b.id_cancion = c.id_cancion 
group by c.genero
order by conteo desc

select c.artista, count(c.artista) as conteo
from buscador b left join cancion c on b.id_cancion = c.id_cancion 
group by c.artista
order by conteo desc

select c.nombre, count(c.nombre) as conteo
from buscador b left join cancion c on b.id_cancion = c.id_cancion 
group by c.nombre
order by conteo desc

insert into cuenta values(7, 'Coca', 'premium', 'V', 6, '2021-06-01', '18:13:32'),
(10, 'Paris', 'free', 'V', 6, '2021-06-01', '18:13:32'),
(12, 'Checha', 'premium', 'V', 6, '2021-06-01', '18:13:32'),
(13, 'Lowel', 'free', 'V', 6, '2021-06-01', '18:13:32'),
(14, 'Nukkye', 'premium', 'V', 6, '2021-06-01', '18:13:32'),
(15, 'Derke', 'free', 'V', 6, '2021-06-01', '18:13:32'),
(16, 'Boaster', 'premium', 'V', 6, '2021-06-01', '18:13:32'),
(17, 'RAINMAKER', 'free', 'V', 6, '2021-06-01', '18:13:32');

insert into usuario values
('Coca', 'ElBicho', 'LostVayne@sinonimous.com'),
('Paris', 'bestoCypherCA', 'GilThunder@sinonimous.com'),
('Checha', 'bestoSovaLATAM', 'ChechaCorman@sinonimous.com'),
('Lowel', 'altocapi', 'lowelcs@heretics.es'),
('Nukkye', 'bestoDueristo', 'Nukkye@G2.com.eu'),
('Derke', 'bestoJett', 'NikitaS@FNATIC.eu'),
('Boaster', 'bestoPerson', 'JakeHowlett@FNC.com'),
('RAINMAKER', 'idolo', 'hacedordelluvia@infinity.com.es');

insert into cancion VALUES(10, 'Ay3', 'Ayo & Teo', 'Trap', '3:15', 'Ay3', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(11, 'Glimmer', 'LIONE', 'Chill', '4:21', 'Glimmer', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(12, 'Last Time', 'Lxst', 'Trap', '2:49', 'Lost', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(13, 'When I Get There', 'Big Gigantic', 'Chill', '3:40', 'Invincible EP', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(14, 'Youth', 'Dabin', 'Chill', '4:24', 'Wild Youth', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(15, 'Incomplete', 'Aero Chord', 'Chill', '4:18', 'Incomplete', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(16, 'Get Your Wish', 'Porter Robinson', 'Chill', '3:38', 'Nurture', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(17, 'Do You Understand?', 'Shy Glizzy', 'trap', '4:10', 'Do You Understand?', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(18, 'Rooms', 'WRLD', 'Chill', '3:23', 'Rooms EP', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(19, 'Explore', 'Cosa Ky', 'Trap', '3:36', 'Explore', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(20, 'Lust', 'Lil Skies', 'Trap', '2:36', 'Life of A Dark Rose', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(21, 'MICHUUL', 'Duckwrth', 'Pop', '3:06', 'an XTRA UGLY Mixtape', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(22, 'Stars', 'Sky', 'Pop', '3:50', 'Stars', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(23, 'Brutal', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(24, 'Good 4 u', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(25, 'Traitor', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(26, 'Drivers license', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(27, 'Deja vu', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(28, 'Enough for you', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(29, '1 step forward 3 steps back', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(30, 'Happier', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(31, 'Favorite crime', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(32, 'Hope ur ok', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(33, 'Jealousy jealousy', 'Olivia Rodrigo', 'pop', '3:41', 'sour', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(34, 'Ni bien ni mal', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(35, '200 mph', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(36, 'Quien tu eres', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(37, 'Caro', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(38, 'Tenemos que hablar', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(39, 'Otra noche en Miami', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(40, 'Ser bichote', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(41, 'Si estuviésemos juntos', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(42, 'Solo de mi', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(43, 'Cuando perriabas', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(44, 'La Romana', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(45, 'Como antes', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(46, 'Estamos bien', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(47, 'Mia', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35'),
(48, 'RLNDT', 'Bad Bunny', 'reggaeton', '2:53', 'X100pre', '2021-05-31', 'youtube.com', 'F', 6, '2021-06-01', '20:27:35');