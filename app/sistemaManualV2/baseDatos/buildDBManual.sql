/*Creacion de la Base de datos*/
DROP DATABASE IF EXISTS dbeum_manual;
CREATE DATABASE dbeum_manual WITH OWNER postgres;

\c dbeum_manual;

/*Creacion de las tablas de la BD */
\i /home/pi/Documents/eum/app/sistemaManualV2/baseDatos/DBTables.sql

/*Insercion de datos en los catalogos*/
\i /home/pi/Documents/eum/app/sistemaManualV2/baseDatos/catalogo.sql
