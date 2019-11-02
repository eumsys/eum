
-- Catalogos de la Plaza --
---
--INSERT INTO cat_continente(idcontinente, nombre) VALUES
--			(1, 'Americano'),
--			(2, 'Europa'),
--			(3, 'Africa'),
--			(4, 'Asia'),
--			(5, 'Antartida');

-- Catalogos Codigos de error--

INSERT INTO "CAT_CODIGOS_ERROR"("idError", descripcion, nombre)VALUES 
			(1,'Operacion registrada y completada sin incidencias','Exitoso'),
			(2,'Operacion registrada, cambio incompleto','Cambio incompleto'),
			(3,'Operacion registrada, cambio incompleto, cajero suspendido','Cajero suspendido sin cambio'),
			(4,'Operacion registrada y completada, cajero suspendido','Cajero suspendido'),
			(5,'Operacion cancelada y completada sin incidencias','.'),
			(6,'Operacion cancelada, cambio incompleto','.'),
			(7,'Operacion cancelada, cambio incompleto, cajero suspendido','.'),
			(8,'Operacion cancelada y completada, cajero suspendido','.');



