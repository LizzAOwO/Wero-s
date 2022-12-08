USE restaurante_db; 

INSERT INTO alimento(alim_nombre, alim_precio, alim_categoria,alim_comida_categoria)
           #TACOS (4)
	VALUES ('Taco de pastor',10.00,'Comida','Taco'),
           ('Taco de Bistec',10.00,'Comida','Taco'),
           ('Taco de chorizo',10.00,'Comida','Taco'),
           ('Taco de suadero',10.00,'Comida','Taco'),
           ('Taco de tripa',12.00,'Comida','Taco'),
		#QUESADILLAS
	       ('Quesadilla de pastor',20.00,'Comida','Taco'),
           ('Quesadilla de Bistec',20.00,'Comida','Taco'),
           ('Quesadilla de chorizo',20.00,'Comida','Taco'),
           ('Quesadilla de suadero',20.00,'Comida','Taco'),
           ('Quesadilla de tripa',23.00,'Comida','Taco'),
           
           #VOLCANES
	       ('Volcan de pastor',15.00,'Comida','Taco'),
           ('Volcan de Bistec',15.00,'Comida','Taco'),
           ('Volcan de chorizo',15.00,'Comida','Taco'),
           ('Volcan de suadero',15.00,'Comida','Taco'),
           ('Volcan de tripa',17.00,'Comida','Taco'),
            #VOLCANES
	       ('Torta de pastor',25.00,'Comida','Taco'),
           ('Torta de Bistec',25.00,'Comida','Taco'),
           ('Torta de chorizo',25.00,'Comida','Taco'),
           ('Torta de suadero',25.00,'Comida','Taco'),
           ('Torta de tripa',28.00,'Comida','Taco');
INSERT INTO alimento(alim_nombre, alim_precio, alim_categoria,alim_bebida_categoria)
           #Bebidas
   VALUES  ('Coca-Cola',18.00,'Bebida','Refresco'),
           ('Mundet',18.00,'Bebida','Refresco'),
           ('Fresca',18.00,'Bebida','Refresco'),
           ('Sprite',18.00,'Bebida','Refresco'),
           ('Fanta',18.00,'Bebida','Refresco'),
           ('Boing de Mango',18.00,'Bebida','Refresco'),
           ('Boing de Guayaba',18.00,'Bebida','Refresco'),
           ('Boing de Uva',18.00,'Bebida','Refresco'),
           
           #Agua de sabor
           ('Horchata',15.00,'Bebida','Agua de Sabor'),
           ('Agua de Jamaica',15.00,'Bebida','Agua de Sabor'),
           ('Agua de Tamarindo',15.00,'Bebida','Agua de Sabor');
           
INSERT INTO alimento(alim_nombre, alim_precio, alim_categoria,alim_extras_categoria)
           #TACOS (4)
	VALUES ('Limon',0.00,'Extra','Verdura'),
           ('Cilantro',0.00,'Extra','Verdura'),
           ('Cebolla',0.00,'Extra','Verdura'),
           ('Piña',0.00,'Extra','Verdura'),
           ('Encurtidos',0.00,'Extra','Verdura'),
           ('Salsa Roja',0.00,'Extra','Salsa'),
           ('Salsa Verde',0.00,'Extra','Salsa'),
           ('Salsa Guacamole',0.00,'Extra','Salsa');
  