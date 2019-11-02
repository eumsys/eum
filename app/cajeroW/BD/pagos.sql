-- Table: public."PAGOS"

-- DROP TABLE public."PAGOS";

CREATE TABLE public."PAGOS"
(
  "idPagos" integer NOT NULL DEFAULT nextval('spago'::regclass),
  "idBoleto" integer NOT NULL,
  expedidora integer NOT NULL,
  "fechaExpedicion" timestamp without time zone NOT NULL,
  codigo integer,
  registrado integer,
  monto integer,
  cambio integer,
  monedas character varying(100),
  billetes character varying(100),
  cambio_entregado character varying(100),
  tipo integer,
  CONSTRAINT "PAGOS_pkey" PRIMARY KEY ("idPagos")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."PAGOS"
  OWNER TO postgres;




-- Table: public."CAT_CODIGOS_ERROR"

-- DROP TABLE public."CAT_CODIGOS_ERROR";

CREATE TABLE public."CAT_CODIGOS_ERROR"
(
  "idError" integer NOT NULL DEFAULT nextval('serror'::regclass),
  descripcion character varying(200),
  nombre character varying(200),
  CONSTRAINT "ERROR_pkey" PRIMARY KEY ("idError")
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public."CAT_CODIGOS_ERROR"
  OWNER TO postgres;

