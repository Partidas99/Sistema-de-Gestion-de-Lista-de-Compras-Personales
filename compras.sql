CREATE TABLE IF NOT EXISTS `Categoria` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Tienda` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`correo` TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS `Producto` (
	`id` integer primary key NOT NULL UNIQUE,
	`nombre` TEXT NOT NULL,
	`cantidad` INTEGER NOT NULL,
	`comprada` INTEGER NOT NULL,
	`categoria_id` INTEGER NOT NULL,
	`tienda_id` INTEGER NOT NULL,
FOREIGN KEY(`categoria_id`) REFERENCES `Categoria`(`id`),
FOREIGN KEY(`tienda_id`) REFERENCES `Tienda`(`id`)
);


FOREIGN KEY(`categoria_id`) REFERENCES `Categoria`(`id`)
FOREIGN KEY(`tienda_id`) REFERENCES `Tienda`(`id`)