
#Q1 donne la ville qui contient plus de bien?
select ville.id_ville,ville.code_dep, ville.code_postal_ville,ville.nom_ville,count(nbr_plan) from ville 
inner join bien 
on ville.id_ville =bien.id_bien
order by nom_ville desc limit 1;


#Q2Donner les biens  vendu avant 2017 (inclus) et qui ont ete payé plus de 450000 euros (strict).

select bien.id_bien, bien.nbr_plan,bien.surface_bati_bien,transaction.id_trans,transaction.annee_date,transaction.prix_bien from bien
inner join transaction
on bien.id_bien =transaction.id_trans
where  prix_bien > 450000 and  annee_date <=2017 limit 50;

#Q3Donner le bien  le moins chere et son montant vendu sur Paris en 2019. # soucis

select type_bien.id_type,type_bien.code_type,type_bien.local_type,transaction.id_trans,transaction.annee_date,transaction.prix_bien,ville.id_ville,
ville.code_dep,ville.nom_ville from type_bien
inner join transaction
on type_bien.id_type= transaction.id_trans
inner join ville 
on transaction.id_trans = ville.id_ville
where  code_dep = 75 and annee_date =2019
order by prix_bien asc;


#Q4 quel le bien qui a plus de piece

select * from bien order by piece_bien desc limit 3;

#Q5 quel est appartement le plus chere dans tous les bien

select type_bien.id_type,type_bien.code_type,transaction.id_trans,transaction.annee_date,transaction.prix_bien from type_bien
inner join transaction
on type_bien.id_type = transaction.id_trans
where  code_type = 2
order by prix_bien  desc limit 1 ;



