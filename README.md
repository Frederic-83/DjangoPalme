# DjangoPalme

# Projet Lyon Palme 

## 1. Présentation d’ensemble du projet 

  *Définition du besoin* : organiser les listes des prets des adherents

on decide de creer un tableau qui comprenne les prets des materieaux par les adherents de lyon palmes, ainsi que les dates de chaques prets.
Cela permet a la societe Lyon palme de savoir quelles materielles sont encore disponibles, ou sinon qui l'a maintenant et quand il devra etre retournée

ceci est creer sur C# par l'application Microsoft Visuel Studios.

---

## 2. Processus de la creation du projet

### *1. Avant la creation du projet*

Au debut du projet, on a deja au debut deux page de code qui nous sert comme guide a nous aider avec le devellopement du client lourd. ces pages sont Adherents.cs et DAO.cs.

La page Adherents.cs est un page complete qui permet de creer la table Adherent dans le programme. Il se sert aussi comme guide en quoi la page de l'initialisation d'un table se ressemble. 

voici un extrait du page Adherent.cs:
```
      public int AdherentID { get; set; }
        public string AdherentIDString { get { return AdherentID.ToString(); } }
        public string AdherentNom { get; set; }
        public string AdherentPrenom { get; set; }
        public string Rue { get; set; }
        public string Ville { get; set; }
        public string Cp { get; set; }
        public string Telephone { get; set; }
        public string Mail { get; set; }
        public string Genre { get; set; }
        public string Niveau { get; set; }
        public int Pointure { get; set; }
        public string PointureString { get { return Pointure.ToString(); } }
        public string Taille { get; set; }
```

La page DAO.cs est un page qui permet d'inserer et d'initialiser les données de chaque champs des tables dans le base de données qu'on créer. Au debut, seul le partie qui inclut les données concernant les adherents.

voici un exemple de la page DAO.cs:
```
var adherents = new ObservableCollection<Adherent>();
try
  {
    using (SqlConnection conn = new SqlConnection(connectionString))
    {
      conn.Open();
      if (conn.State == System.Data.ConnectionState.Open)
      {
        using (SqlCommand cmd = conn.CreateCommand())
        {
          cmd.CommandText = GetAdherentsQuery;
          using (SqlDataReader reader = cmd.ExecuteReader())
          {
            while (reader.Read())
            {
              var adherent = new Adherent();
              adherent.AdherentNom = reader.GetString(0);
              adherent.AdherentPrenom = reader.GetString(1);
              adherent.Rue = reader.GetString(2);
              adherent.Cp = reader.GetString(3);
              adherent.Ville = reader.GetString(4);
              adherent.Telephone = reader.GetString(5);
              adherent.Mail = reader.GetString(6);
              adherent.Genre = reader.GetString(7);
              adherent.Niveau = reader.GetString(8);
              adherent.Pointure = reader.GetInt32(9);
              adherent.Taille = reader.GetString(10);
              adherents.Add(adherent);
[...]
```

### *2. lors du creation du projet*

pour commencer, on doit ouvrir Visuel Studios et de créer un nouvelle repertoire pour le projet. dés que le projet est créer, on a le choix d'inserer les pages Adherents et DAO, ou on peut creer des nouveaux pages de memes noms et coller les codes a l'interieur. On prefer de mettre le page Adherent dans un sous repertoire intitulée Model.

Puis, on cherche a ajouter les tables et les champs qu'on a besoins pour le projet. Dans ce cas, il s'agit des tables Prêts, Materiels et ses deux tables-enfants: palmes et combinaison. Afin de faire cela, on creer leurs pages dans Visuel Studio. Ensuite, afin d'officialiser ces nouveaux champs, on ajouts les nouveaux tables dans la Page DAO.cs, dans la meme maniere qu'on a initialiser le table Adherent.

voici un exemple du page Materiel.cs:
```
  public class Materiel
    {
      //atributs
      private int _codeMat;
      private string _type;
      private string _marque;
      private string _etat;

      public Materiel(int _codeMat, string _type, string _marque, string _etat)
      {
        this._codeMat = _codeMat;
        this._type = _type;
        this._marque = _marque;
        this._etat = _etat;
      }

      public override string ToString()
      {
        // return base.Tostring
        string _materiel;
        _materiel = string.Concat("_codeMat : ", _codeMat, "_type : ", _type, "_marque : ", _marque, "_etat :", _etat);
        return base.ToString();
      }
    }
```

exemple du page prêts:
```
public class Pret
{
  //attributs
  private int idpret;
  private DateTime datepret;
  private int idAdherent;

  public Pret(int idpret, DateTime datepret, int idAdherent)
  {
    this.idpret = idpret;
    this.datepret = datepret;
    this.idAdherent = idAdherent;
  }

  public override string ToString()
  {
    // return base.Tostring
    string _combinaison;
    _combinaison = string.Concat("idpret : ", idpret, "datepret : ", datepret, "idAdherent : ", idAdherent);
    return base.ToString();
  }
}
```

Maintenant, on devra faire apparaitre les resultats des qu'on a demarer le code. Pour cela, on créera un page qui permet de les afficher sous forme de tableau. on appelle cet page MainPage.
Il y a plusieur moyen de faire afficher les codes de cet maniere:
1. On met tous les tables dans la page MainPage. Cela a pour consequence de mettre tous les données sur un meme page et, si on ne manipule pas bien l'organisation du page, risque d'etre illisible.
2. On decide de créer plusieur page MainPages (ex: Mainpage; Mainpage(1); Mainpage(1)... etc.). alors que cela risque de rendre plus de temps, on obtiendera un page ou on peut acceder facilement a un autre page ayant un table different.

extrait du code MainPage.xaml:
```
<Page 
  x:Class="TestMateriel.MainPage" 
  xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" 
  xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml" 
  xmlns:local="using:TestMateriel.Model" 
  xmlns:d="http://schemas.microsoft.com/expression/blend/2008" 
  xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006" 
  mc:Ignorable="d" 
  Background="{ThemeResource ApplicationPageBackgroundThemeBrush}"> 

  <Grid Background="{ThemeResource SystemControlAcrylicWindowBrush}"> 
    <RelativePanel> 
      <ListView Name="AdherentList" 
        SelectionMode="Single" 
        ScrollViewer.VerticalScrollBarVisibility="Auto" 
        ScrollViewer.IsVerticalRailEnabled="True" 
        ScrollViewer.VerticalScrollMode="Enabled" 
        ScrollViewer.HorizontalScrollMode="Enabled" 
        ScrollViewer.HorizontalScrollBarVisibility="Auto" 
        ScrollViewer.IsHorizontalRailEnabled="True" 
        Margin="20"> 
          <ListView.HeaderTemplate> 
            <DataTemplate> 
              <StackPanel Orientation="Horizontal"  > 
                <TextBlock Text="Nom" Margin="8,0" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Prenom" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Rue" Width="200" Foreground="DarkRed" /> 
                <TextBlock Text="CP" Width="80" Foreground="DarkRed" /> 
                <TextBlock Text="Ville" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Num Telephone" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Mail" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Genre" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Pointure" Width="150" Foreground="DarkRed" /> 
                <TextBlock Text="Taille" Width="150" Foreground="DarkRed" /> 
              </StackPanel> 
            </DataTemplate> 
          </ListView.HeaderTemplate> 
          <ListView.ItemTemplate> 
            <DataTemplate x:DataType="local:Adherent"> 
              <StackPanel Orientation="Horizontal" > 
                <TextBlock Name="Nom" 
                  Text="{x:Bind MemberNom}" 
                  Width="150" /> 
                <TextBlock Name="Prenom" 
                  Text="{x:Bind MemberPrenom}" 
                  Width="150" /> 
                <TextBlock Name ="rue" 
                  Text="{x:Bind Road}" 
                  Width="200" /> 
                <TextBlock Name ="Code postal" 
                  Text="{x:Bind Cp}" 
                  Width="80" /> 
                <TextBlock Name ="ville" 
                  Text="{x:Bind Town}" 
                  Width="150" /> 
                <TextBlock Name ="Num Telephone" 
                  Text="{x:Bind Telephone}" 
                  Width="150" /> 
                <TextBlock Name ="Mail" 
                  Text="{x:Bind}" 
                  Width="150" /> 
                <TextBlock Name ="Genre" 
                  Text="{x:Bind Gender}" 
                  Width="150" /> 
                <TextBlock Name ="Pointure" 
                  Text="{x:Bind HeelSize}" 
                  Width="150" /> 
                <TextBlock Name ="Taille" 
                  Text="{x:Bind Height}" 
                 Width="150" /> 
                </StackPanel> 
              </DataTemplate> 
            </ListView.ItemTemplate> 
          </ListView>
        [...] 
```

exemple du code MainPage.xaml.cs:
```
using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Runtime.InteropServices.WindowsRuntime;
using Windows.Foundation;
using Windows.Foundation.Collections;
using Windows.UI.Xaml;
using Windows.UI.Xaml.Controls;
using Windows.UI.Xaml.Controls.Primitives;
using Windows.UI.Xaml.Data;
using Windows.UI.Xaml.Input;
using Windows.UI.Xaml.Media;
using Windows.UI.Xaml.Navigation;

// Pour plus d'informations sur le modèle d'élément Page vierge, consultez la page https://go.microsoft.com/fwlink/?LinkId=402352&clcid=0x409

namespace Gestion_Materiel
{
    /// <summary>
    /// Une page vide peut être utilisée seule ou constituer une page de destination au sein d'un frame.
    /// </summary>
    public sealed partial class MainPage : Page
    {
        public MainPage()
        {
            this.InitializeComponent();
        }
    }
}
```

