CREATE SCHEMA IF NOT EXISTS `testepy` DEFAULT CHARACTER SET utf8 ;
USE `testepy` ;

-- -----------------------------------------------------
-- Table `mydb`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `testepy`.`equipamento` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(45) NOT NULL,
  `fornecedor` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `nome_UNIQUE` (`nome` ASC) VISIBLE)
ENGINE = InnoDB;

INSERT into equipamento (nome,fornecedor) values

('SIN-MCA', 'teste1'),
('SIN-MCA2', 'teste2'),
('SIN-MCA3', 'teste3'),
('SIN-MCA4', 'teste4'),
('SIN-MCA5', 'teste5'),
('SIN-MCA6', 'teste6');

select * from equipamento;
