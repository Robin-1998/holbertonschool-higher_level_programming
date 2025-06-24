-- script qui créé l'utilisateur du serveur MYSQL user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- on créé un utilisateur avec une conditon et on donne comme mot de passe : user_0d_1_pwd
-- NOTE : il est obligatoire d'intégrer avec l'utilsateur l'hôte à partir duquel il se connecte (localhost)
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- On donne tous les priblèges de la base de donnée à l'utilisateur
FLUSH PRIVILEGES;
-- Les changements prennent effet immédiatement
