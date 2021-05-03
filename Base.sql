create table usuario (
    username VARCHAR(30), primary key(username),
    password varchar(30),
    email, varchar(30)
);

create table cuenta (
    id_user int, primary key(id_user),
    userName VARCHAR(30), foreign key(userName) references usuario(username),
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