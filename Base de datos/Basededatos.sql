DROP DATABASE INDICES;
CREATE DATABASE INDICES;

USE INDICES;

CREATE TABLE INDICES_ECONOMICOS (
	ID_INDICES INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	NOMBRE VARCHAR(100) NOT NULL UNIQUE,
	TAG VARCHAR(20) NOT NULL UNIQUE,
	DESCRIPCION VARCHAR (500)	
);

CREATE TABLE DATOS (
	ID_DATOS INTEGER NOT NULL AUTO_INCREMENT,
	ID_INDICES INTEGER,
	DATE_TIME DATETIME,
	OPEN_ DECIMAL,
	HIGH FLOAT,
	LOW FLOAT,
	CLOSE_ FLOAT,
	VOLUME INTEGER,
	DIVIDENS INTEGER,
	STOCK_SPLITS INTEGER,
	PRIMARY KEY (ID_DATOS),
	FOREIGN KEY (ID_INDICES) REFERENCES INDICES_ECONOMICOS(ID_INDICES)	
);

-- Observación:
-- Aün quedan valores repetidos en la tabla datos en el DATETIME

-- Agregamos datos en indices_economicos

INSERT INTO indices_economicos(NOMBRE, TAG, DESCRIPCION)
VALUES 
	("CSI300", "000300.SS", "El CSI 300 es un índice bursátil ponderado por capitalización diseñado para replicar el desempeño de las 300 principales acciones negociadas en la Bolsa de Shanghai y la Bolsa de Shenzhen."),
	("Dow Jones", "^DJI", "El Dow Jones Industrial Average® (El Dow), es una medida ponderada por precio de 30 empresas blue chip de Estados Unidos. El índice cubre todos los sectores, excepto transporte y servicios públicos." ),
	("Indice de Precios y Cotizaciones", "^MXX", "El Índice de Precios al Consumidor es un indicador que mide la evolución promedio de los precios de un conjunto de bienes y servicios representativos del gasto de consumo de los hogares residentes en un área determinada"),
	("National Association of Secirities Dealers Automated", "^NDX", "El Nasdaq es el acrónimo de National Association of Securities Dealers Automated Quotation y es la segunda bolsa de valores electrónica automatizada más grande de Estados Unidos. "),
	("Nikkei", "^N255", "El índice Nikkei, también conocido como Nikkei 225, es el principal índice bursátil de referencia de la evolución del mercado japonés. Es un índice ponderado por precio, formado por las 225 empresas con mayor liquidez que cotizan en la Bolsa de Valores de Tokio."),
	("Standard & Poor's 500", "^GSPC", "El índice Standard & Poor's 500, o más conocido como S&P 500, recoge 500 empresas estadounidenses seleccionadas por su tamaño, liquidez y representatividad por actividad económica, incluyendo 400 industriales, 20 del sector transporte, 40 de servicios y 40 financieras."),
	("EuroStoxx 50", "^STOXX50E", "El EuroStoxx 50 es un índice de referencia en la Eurozona y que incluye a las 50 compañías más importantes por capitalización bursátil, incluyendo actualmente empresas de España, Francia, Alemania, Bélgica, Irlanda, Italia y Holanda.");
