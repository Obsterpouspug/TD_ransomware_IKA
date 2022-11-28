 ## TD-ransomware-IK



# Chiffrement
Question n°1: Quel est le nom de l'algorithme de chiffrement ? Est-il robuste et pourquoi ?

Il s'agit d'un chiffrement complètement symétrique ce qui signifie qu'a même opération est appliquée au message final pour retrouver le message initial, c'est robuste mais il existe des moyens de le casser. Il peut être attaqué par "Bruteforce" pour trouver la clé. Le partage de la clé est aussi un problème car il faut la partager avec le serveur de la victime pour qu'il puisse décrypter les fichiers et il faut donc que le serveur soit sécurisé et que la clé soit bien protégée pour éviter que quelqu'un d'autre ne puisse la récupérer et décrypter les fichiers de la victime sans son accord et sans qu'il le sache (ce qui est le but de ce ransomware).

# Génération des secrets

Question n°2: Pourquoi ne pas hacher le sel et la clef directement ? Et avec un hmac ?

Car le sel et la clé sont déjà hachés, on ne peut pas les hacher deux fois sinon on ne pourra plus les utiliser pour décrypter les fichiers car on ne pourra plus les retrouver dans le fichier de configuration du ransomware (qui contient le sel et la clé hachés).
Et il est mieux de faire les deux séparément pour augmenter le temps d'exécution pour rendre très longues les attaques brutes force.
Le hmac est utilisé pour vérifier l'intégrité des données, il est donc inutile de l'utiliser pour hacher le sel et la clé.

# Setup

Question n°3: Pourquoi il est préférable de vérifier qu'un fichier token.bin n'est pas déjà présent ?

Pour éviter que le ransomware ne s'exécute plusieurs fois sur le même ordinateur et qu'il ne chiffre plusieurs fois les mêmes fichiers, ainsi demandants plusieurs fois le paiement de la rançon.

# Vérifier et utiliser la clef

Question n°4: Comment vérifier que la clef la bonne ?

La clef est hachée avec un hmac, il faut donc hacher la clef fournie avec le même hmac que celui utilisé pour hacher la clef du fichier de configuration du ransomware (qui contient la clef hachée) et comparer les deux hachages. Si ils sont identiques alors la clef est bonne.
On peut également vérifier que la clef est bonne en la décodant en base64 et en vérifiant que la taille de la clé est bien de 32 octets (256 bits) et que la clé est bien composée de caractères alphanumériques (caractères alphanumériques = chiffres et lettres de l'alphabet) et de caractères spéciaux (caractères spéciaux = caractères qui ne sont pas des chiffres ni des lettres de l'alphabet).
Par conséquent si on a la bonne clé, une méthode beaucoup plus simple serait de décrypter les fichiers et vérifier que les fichiers déchiffrés sont bien les mêmes que les fichiers chiffrés. En ce qui concerne le token, on peut vérifier que ce dernier est valide, en utilisant la fonction verify token qui va vérifier que le token n'est pas expiré et qu'il est bien signé par le serveur.


# Question bonus

B1 : Expliquez ce que vous faite et pourquoi?
On ajoute une fonction leak_files qui va envoyer les fichiers au CNC. 
On va envoyer les fichiers au CNC pour qu'il puisse les stocker sur son serveur et les rendre publics pour que la victime ne puisse plus les utiliser et qu'elle soit obligée de payer la rançon pour les récupérer. 


B2 : Expliquez comment le casser et écrivez un script pour récupérer la clef à partir d’un fichier
chiffré et d’un fichier clair.
On peut casser le chiffrement en utilisant une attaque par dictionnaire. On va utiliser un dictionnaire de mots de passe courants et on va essayer de décrypter le fichier avec chacun des mots de passe du dictionnaire. Si le fichier est décrypté alors le mot de passe est bon et on a trouvé la clé.


B3 : Quelle(s) option(s) vous est(sont) offerte(s) fiable(s) par la bibliothèque cryptographie ?
Justifiez votre choix.

On peut utiliser la fonction derive_key_from_password qui permet de dériver une clé à partir d'un mot de passe. Cette fonction utilise la fonction PBKDF2HMAC qui permet de dériver une clé à partir d'un mot de passe et d'un sel. Cette fonction est fiable car elle est utilisée pour dériver une clé à partir d'un mot de passe et d'un sel et elle est utilisée pour dériver une clé à partir d'un mot de passe et d'un sel. Elle est donc fiable car elle est utilisée pour dériver une clé à partir d'un mot de passe et d'un sel et elle est utilisée pour dériver une clé à partir d'un mot de passe et d'un sel. 


B4 : Quelle ligne de commande vous faut-il avec pyinstaller pour créer le binaire ?

On utilise la commande :
pyinstaller --onefile --noconsole --icon=icon.ico --add-data

B5 : Où se trouve le binaire créer ?
Le binaire se trouve dans le dossier dist.

B4 : Quelle(s) option(s) vous avez choisi(s) pour vous aider à décrypter un fichier?




