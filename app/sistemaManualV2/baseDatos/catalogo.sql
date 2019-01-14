INSERT INTO cat_estadoimpresora(idcatalogo, estado, descripcion) VALUES
			(0, 'sin uso','no se ha mandado impresion'),
			(1, 'impresion mandada','la impresora esta intentado imprimir algo'),
			(2, 'error','no se pudo imprimir nada');
INSERT INTO usuario(nombre, apaterno, amaterno, nomusuario, rol, passwd, idhorario, puesto) VALUES 
		   ('ingenieria','EUM','Parking Tip','Susuario',0,'Ingenieria3UM',0,'admin'),
		   ('ingenieria','EUM','Parking Tip','3868737',0,'3867793',0,'admin');

INSERT INTO sesion (idsesion,estado,descripcion) VALUES
(1,1,'sinIniciarSesion'),
(2,2,'sesionIniciada');