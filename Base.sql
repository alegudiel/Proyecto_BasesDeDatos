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
on bitacora (id, fecha, hora, updated_by, accion)

create index indexcuenta 
on Cuenta(id_usuario, user_type,update_by)

create index indenxplaylist 
on Playlist(id_playlist, dueño,update_by)

create index indexcancion 
on Cancion(id_cancion, album,genero,artista,fecha_lanzamiento,nombre,update_by)