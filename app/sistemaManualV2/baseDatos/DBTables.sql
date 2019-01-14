CREATE TABLE plaza
(
  idplaza integer NOT NULL,
  estado character varying,
  pais character varying,
  continente character varying,
  nombre_plaza character varying,
  calle character varying,
  colonia character varying,
  delegacion character varying,
  cp integer,
  numinterior character varying,
  numexterior character varying,
  telefonolocal character varying,
  extension character varying,
  email character varying,
  celular character varying,
  logo character varying,
  CONSTRAINT plaza_pk PRIMARY KEY (idplaza)
);
CREATE TABLE cat_rol
(
  idrol integer NOT NULL,
  nombre character varying,
  CONSTRAINT cat_rol_pk PRIMARY KEY (idrol)
);
CREATE TABLE usuario
(
  idusuario serial NOT NULL,
  nombre character varying,
  apaterno character varying,
  amaterno character varying,
  nomusuario character varying,
  rol integer,
  passwd character varying,
  idhorario integer,
  puesto character varying,
  CONSTRAINT usuario_pk PRIMARY KEY (idusuario)
);
CREATE TABLE boletos
(
  folio integer NOT NULL,
  expedidora integer NOT NULL,
  fecha timestamp without time zone NOT NULL,
  plaza integer,
  placa character varying(50),
  CONSTRAINT boletos_pk PRIMARY KEY (folio, expedidora, fecha)
);
CREATE TABLE cat_estadoimpresora
(
  idcatalogo integer NOT NULL,
  estado character varying(50),
  descripcion character varying(200),
  CONSTRAINT cat_estadoimpresora_pk PRIMARY KEY (idcatalogo)
);
CREATE TABLE datos_caja
(
  id_caja integer NOT NULL,
  plaza integer,
  num_caja integer,
  CONSTRAINT caja_pk PRIMARY KEY (id_caja)
);
CREATE TABLE datos_expedidora
(
  id_expedidora integer NOT NULL,
  plaza integer,
  num_expedidora integer,
  CONSTRAINT expedidora_pk PRIMARY KEY (id_expedidora)
);
CREATE TABLE estado_impresora
(
  idestadoimpresora integer NOT NULL,
  estado integer,
  fecha timestamp without time zone,
  CONSTRAINT estadoimpresora_pk PRIMARY KEY (idestadoimpresora)
);
CREATE TABLE politicas
(
  idpoliticas integer NOT NULL,
  plaza integer,
  descripcion character varying(1000),
  CONSTRAINT politicas_pk PRIMARY KEY (idpoliticas)
);
CREATE TABLE sesion
(
  idsesion integer NOT NULL,
  estado integer,
  descripcion character varying(100),
  CONSTRAINT sesion_pk PRIMARY KEY (idsesion)
);

ALTER TABLE plaza OWNER TO postgres;
ALTER TABLE boletos OWNER TO postgres;
ALTER TABLE cat_estadoimpresora OWNER TO postgres;
ALTER TABLE datos_caja OWNER TO postgres;
ALTER TABLE datos_expedidora OWNER TO postgres;
ALTER TABLE estado_impresora OWNER TO postgres;
ALTER TABLE politicas OWNER TO postgres;
ALTER TABLE sesion OWNER TO postgres;
alter table boletos add constraint boleto_plaza_fk foreign key (plaza) references plaza (idplaza);
alter table datos_caja add constraint plaza_caja_fk foreign key (plaza) references plaza (idplaza);
alter table datos_expedidora add constraint plaza_expedidora_fk foreign key (plaza) references plaza (idplaza);
alter table politicas add constraint politica_plaza_fk foreign key (plaza) references plaza (idplaza);
alter table estado_impresora add constraint cat_estadoimpresora_fk foreign key (estado) references cat_estadoimpresora (idcatalogo);