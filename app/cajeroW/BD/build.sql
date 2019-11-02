
/*Creacion de la Base de datos*/
/*DROP DATABASE IF EXISTS dbeum_tecamac;*/
/*CCREATE DATABASE dbeum_tecamac WITH OWNER eumdb;*/

\c CajerOk;

/*Creacion de las tablas de la BD */
\i pagos.sql

/*Insercion de datos en los catalogos*/
\i catalogos.sql


