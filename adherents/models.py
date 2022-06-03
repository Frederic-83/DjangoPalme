from django.db import models
""""""

class Adherent(models.Model):
    Prenom = models.CharField(max_length=50)
    Nom = models.CharField(max_length=50)
    Adresse_Rue = models.CharField(max_length=50)
    Adresse_CP = models.CharField(max_length=50)
    Adresse_Ville = models.CharField(max_length=50)
    Telephone = models.CharField(blank=False, max_length=10)
    Mail = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Niveau = models.CharField(max_length=20)
    Numero_Licence = models.CharField(max_length=20)
    Date_Naissance = models.DateField()
    Certificat_Medical = models.CharField(max_length=50)
    Pointure = models.CharField(max_length=50)
    Taille = models.CharField(max_length=50)
    def str(self):
        return self.id



class Entraineur(models.Model):
    adherent = models.OneToOneField(
        Adherent, on_delete=models.CASCADE, related_name="entraineur", primary_key= True,
    )
    def str(self):
        return self.adherent.Prenom


class Coach(models.Model):
    entraineur = models.OneToOneField(
        Entraineur, on_delete=models.CASCADE, primary_key= True,
    )
    def str(self):
        return self.entraineur.adherent.Prenom



class Entrainement(models.Model):
    Dates = models.DateField()
    Lien_fichier = models.CharField(max_length=300)
    entraineurs = models.ManyToManyField(Entraineur)
    coach = models.ForeignKey(Coach, related_name="coachs_entrainement", on_delete=models.CASCADE)


class Role(models.Model):
    Nom = models.CharField(max_length=50)
    adherents = models.ManyToManyField(Adherent)
    def str(self):
        return self.Nom

